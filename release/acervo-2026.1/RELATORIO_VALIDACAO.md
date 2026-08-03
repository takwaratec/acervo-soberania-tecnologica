# Relatório de validação — Edição 2026.1 (pré-corte)

Consolidado em 2026-08-03 (H5-REV-001).

## Validações executadas
1. Front matter: 0 erros (56 avisos legados) — validate_frontmatter.py.
2. Build estrito: mkdocs build --strict → exit 0.
3. Links internos: cobertos pelo build estrito.
4. Arquivos privados: 0 no pacote (_privado/_quarentena ausentes).
5. Credenciais/dados pessoais: nenhum padrão real (falsos positivos: "secretarias"/"resenha").
6. UTF-8: 0 erros.
7. Imagens: 0 PNGs no pacote (coerente com a matriz de direitos).
8. Inventário × staging: 185/185 copiados com hash conferido.
9. CHECKSUMS.sha256: 185 entradas; extração limpa 0 falhas.
10. ZIP reproduzível: SHA-256 638213fc… (registrado).

## Auditorias
- FRENTE-E-REV-001: reconciliação completa (divergência identificada; lista 191 regenerada).
- FRENTE-E-REV-002: parecer ACEITE (8/8 verificações).
- FRENTE-F-REV-001: parecer APTO H5 (8/8 verificações).
- H5-REV-001: prontidão H5 (7/7 confirmações).

## Pendências não bloqueantes
ORCID; DOIs Cadernos 2/5/6/7; novas versões Zenodo Cadernos 1/4; portão PR #15;
126 fichas → matriz de direitos quando selecionadas.
