#!/usr/bin/env python3
"""Validador de front matter das fichas do Acervo Soberania Tecnológica.

Aplica as regras de GOVERNANCA_DOCUMENTAL.md:
- campos mínimos por tipo documental;
- estado_documental dentro da taxonomia canônica (ou valor legado mapeado);
- front matter YAML parseável;
- verificação de conteúdo privado acidentalmente na árvore pública.

Uso:
    python3 scripts/validate_frontmatter.py [--docs DIR] [--strict] [--quiet]

Classificação dos problemas:
- ERRO: viola regra obrigatória; falha em qualquer modo.
- AVISO: estado documental legado mapeado na governança; exibido sempre,
  mas só provoca exit 1 quando `--strict` está ativo.

Exit code:
- 0 = sem erros reais (avisos legados podem existir, se sem `--strict`);
- 1 = há erros reais, ou avisos promovidos a erro por `--strict`.
"""

import argparse
import os
import re
import sys
import yaml

# Estados canônicos (GOVERNANCA_DOCUMENTAL.md)
ESTADOS_CANONICOS = {
    "recebido",
    "identificacao-pendente",
    "protegido-privado",
    "duplicata-fonte-auxiliar",
    "extracao-preliminar",
    "em-revisao-documental",
    "homologado-documentalmente",
    "visao-autoral",
    "historico",
    "quarentena",
    "retirado-da-publicacao",
}

# Valores legados aceitos (mapeados na governança; aviso, não erro por padrão)
ESTADOS_LEGADOS = {
    "edicao-publica-conformada": "homologado-documentalmente",
    "publicado-no-zenodo": "homologado-documentalmente",
    "curado": "homologado-documentalmente",
    "edicao-revisada-para-acervo": "homologado-documentalmente",
    "revisado-com-fonte-integral": "homologado-documentalmente",
    "depositado-no-zenodo": "homologado-documentalmente",
    "publicado-no-acervo": "homologado-documentalmente",
}

TIPOS_DOCUMENTAIS = {
    "ficha-cientifica", "ficha-academica", "resenha-academica",
    "estado-da-arte", "perfil", "indice", "documento-institucional",
    "documento-historico", "visao-autoral", "fonte-primaria-privada",
    "laudo-ou-certificado-de-ensaio", "ficha-tecnica-de-produto",
    "norma-ou-regulamento", "periodico-institucional",
    "material-didatico-institucional", "documento-de-patente",
    "cartilha-comunitaria", "manual-tecnico",
    "estado-da-arte-com-agenda-experimental", "ensaio-autoral",
    "ensaio-tecnico", "instrumento-de-pesquisa", "sintese-critica",
    "memoria-historica", "indice-tematico",
    "manual-tecnico-autoral", "especificacao-tecnica-autoral",
    "memorial-tecnico-autoral", "ensaio-critico-autoral",
}

# Caminhos proibidos dentro de docs/ (nunca devem ser indexados/publicados)
DENY_PARTS = [
    "/_privado/", "/_quarentena/", "/_acervo_completo/", "/TRIAGEM_BRUTA/",
    "/TRIAGEM-BRUTA/", "/transcripts/", "/WhatsApp Chat - ", "Conversa do WhatsApp",
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(path):
    """Retorna (dict_metadados, erro) ou (None, mensagem)."""
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        return None, f"leitura: {e}"

    m = FRONTMATTER_RE.match(content)
    if not m:
        return None, "sem front matter (--- ... ---)"

    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return None, f"YAML inválido: {e}"

    if not isinstance(data, dict):
        return None, "front matter não é um mapeamento"
    return data, None


def validar_arquivo(path, strict):
    """Retorna (erros, avisos) para um arquivo.

    - `erros`: problemas que falham em qualquer modo (lista de strings);
    - `avisos`: estados legados; só promovidos a erro quando `strict=True`.
    """
    erros = []
    avisos = []
    rel = os.path.relpath(path, args.docs)

    if os.path.basename(rel) in ("index.md", "sobre.md", "metodologia.md"):
        return erros, avisos

    data, err = parse_frontmatter(path)
    if err:
        return [f"{os.path.basename(path)}: {err}"], avisos
    if not isinstance(data, dict):
        return [f"{os.path.basename(path)}: front matter não é um mapeamento"], avisos

    # Campos obrigatórios universais
    for campo in ("tipo_documental", "estado_documental", "responsavel_curadoria"):
        if campo not in data:
            erros.append(f"{rel}: campo obrigatório ausente: {campo}")

    tipo = data.get("tipo_documental")
    if tipo and tipo not in TIPOS_DOCUMENTAIS:
        erros.append(f"{rel}: tipo_documental fora da taxonomia: {tipo}")

    estado = data.get("estado_documental")
    if estado:
        if estado in ESTADOS_LEGADOS:
            msg = (
                f"{rel}: estado legado '{estado}' (equivale a "
                f"'{ESTADOS_LEGADOS[estado]}'; atualizar na próxima revisão) — AVISO"
            )
            if strict:
                erros.append(msg)
            else:
                avisos.append(msg)
        elif estado not in ESTADOS_CANONICOS:
            erros.append(f"{rel}: estado_documental fora da taxonomia: {estado}")

    # Identificador: exigir doi/isbn/issn/url OU identificador declarado ausente
    if tipo in ("ficha-cientifica", "ficha-academica", "resenha-academica"):
        tem_id = any(k in data for k in ("doi", "isbn", "issn", "url", "identificador"))
        if not tem_id:
            erros.append(f"{rel}: ficha sem identificador (doi/isbn/issn/url/identificador)")

    return erros, avisos


def main():
    global args
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docs", default="docs", help="diretório da árvore pública (default: docs)")
    ap.add_argument("--strict", action="store_true", help="aviso legado vira erro")
    ap.add_argument("--quiet", action="store_true", help="só imprime resumo")
    args = ap.parse_args()

    erros_totais = []
    avisos_totais = []
    arquivos = 0
    for root, dirs, files in os.walk(args.docs):
        # Podar diretórios proibidos durante o walk
        dirs[:] = [d for d in dirs if f"/{d}/" not in DENY_PARTS and d not in ("_privado", "_quarentena", "_acervo_completo")]
        for fname in files:
            if not fname.endswith(".md"):
                continue
            arquivos += 1
            path = os.path.join(root, fname)
            erros, avisos = validar_arquivo(path, args.strict)
            erros_totais.extend(erros)
            avisos_totais.extend(avisos)

    # Conteúdo privado na árvore pública
    privados = []
    for root, dirs, files in os.walk(args.docs):
        for fname in files:
            if fname.endswith(".md"):
                path = os.path.join(root, fname)
                if any(d in path for d in DENY_PARTS):
                    privados.append(os.path.relpath(path, args.docs))

    if not args.quiet:
        for p in erros_totais:
            print(f"  {p}")
        for p in avisos_totais:
            print(f"  {p}")
        for p in privados:
            print(f"  🔒 conteúdo privado em docs/: {p}")

    print(f"\nArquivos .md verificados: {arquivos}")
    print(f"Erros: {len(erros_totais)} | Avisos: {len(avisos_totais)} | Privados em docs/: {len(privados)}")

    return 1 if (erros_totais or privados) else 0


if __name__ == "__main__":
    sys.exit(main())
