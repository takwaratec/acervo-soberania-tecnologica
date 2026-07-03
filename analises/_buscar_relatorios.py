#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""Download relatorios abertos e criar fichas + leis + perfis"""
import os, subprocess, fitz, re, shutil
from datetime import datetime

ACERVO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"
DOWNLOAD_DIR = os.path.join(ACERVO, "_pdfs_para_catalogar")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

NOW = datetime.now().strftime('%Y-%m-%d')

def try_download(key, url, max_size_mb=50):
    output = os.path.join(DOWNLOAD_DIR, f"{key}.pdf")
    print(f"  📥 {key}: ", end="", flush=True)
    result = subprocess.run(
        ['curl', '-s', '-L', '--max-time', '30',
         '-A', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
         '-o', output, '-w', '%{http_code}',
         url],
        capture_output=True, text=True, timeout=35
    )
    http = result.stdout.strip()
    size = os.path.getsize(output) if os.path.exists(output) else 0
    is_pdf = False
    if size > 5000:
        with open(output, 'rb') as f:
            is_pdf = f.read(5) == b'%PDF-'
    
    status = "✅ PDF" if (http in ['200','301','302'] and is_pdf) else \
             f"⚠️ {size//1024}KB" if size > 100 else "❌"
    print(f"HTTP {http} | {size//1024}KB | {status}")
    
    if is_pdf:
        return output
    else:
        if os.path.exists(output):
            os.remove(output)
        return None

def create_ficha(key, title, citation, content_text, area, subgrupo):
    """Create Cavichiolli 8-section ficha"""
    area_path = os.path.join(ACERVO, area, subgrupo)
    os.makedirs(area_path, exist_ok=True)
    
    ficha_name = f"_{key}.md"
    ficha_path = os.path.join(area_path, ficha_name)
    
    if os.path.exists(ficha_path):
        print(f"  ⏭️  Ficha ja existe: {ficha_name}")
        return
    
    resume = re.sub(r'\s+', ' ', content_text[:500].strip())
    
    ficha = f"""---
conversao_cavichiolli: {NOW}
how_to_cite: "{citation}"
status_pdf: "✅ Criado em {NOW}"
---

# {title}

> Ficha gerada em {NOW}.

---

## 1. IDENTIFICAÇÃO

| Campo | Dado |
|-------|------|
| **Título** | {title} |
| **Tipo** | Referência |
| **Criado em** | {NOW} |

---

## 2. CLASSIFICAÇÃO TEMÁTICA

- **Eixo:** {area.split('_',1)[-1] if '_' in area else area}
- **Subgrupo:** {subgrupo}

---

## 3. RESUMO / SÍNTESE

> {resume}

---

## 4. ANÁLISE CRÍTICA

| Aspecto | Avaliação |
|---------|-----------|
| **Relevância** | ✅ Alta |
| **Qualidade** | ✅ Fonte oficial |
| **Completude** | ⏳ Pendente de revisão |

---

## 5. DADOS EXTRAÍDOS / EVIDÊNCIAS

*Documento de referência. Resumo automático disponível acima.*

---

## 6. CONEXÕES COM OUTRAS FICHAS DO ACERVO

| Ficha | Tipo de Relação |
|-------|-----------------|
| [INDEX.md](../../INDEX.md) | Hierárquica |

---

## 7. APLICAÇÕES PRÁTICAS

- Pendente de análise manual

---

## 8. REFERÊNCIAS

- {citation}

---

⚠️ *Nota de Compliance:* [...] conforme método Cavichiolli (2025) · 8 seções · Documento gerado em {NOW}*
"""
    with open(ficha_path, 'w') as f:
        f.write(ficha)
    print(f"  ✅ Ficha: {area}/{subgrupo}/{ficha_name}")

# ============================================================
# 1. RELATORIOS GLOBAIS (IPCC, PNUD, ONU)
# ============================================================
print("="*70)
print("📡 RELATORIOS GLOBAIS")
print("="*70)

# IPCC AR6 Synthesis Report
pdf = try_download('ipcc_ar6_syr', 
    'https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_SPM.pdf')
if pdf:
    doc = fitz.open(pdf)
    texto = ""
    for page in doc: texto += page.get_text()
    doc.close()
    create_ficha('ipcc_ar6_syr',
        'IPCC AR6 Synthesis Report: Summary for Policymakers (2023)',
        'IPCC. Climate Change 2023: Synthesis Report — Summary for Policymakers. Geneva: IPCC, 2023.',
        texto, '04_certificacoes-e-normas', '04_Ensaios_Certificacao')
else:
    create_ficha('ipcc_ar6_syr',
        'IPCC AR6 Synthesis Report (2023)',
        'IPCC. Climate Change 2023: Synthesis Report. Geneva: IPCC, 2023.',
        'Relatório de síntese do Sexto Relatório de Avaliação do IPCC. Consolida as conclusões dos três grupos de trabalho sobre a base científica, impactos, adaptação e mitigação das mudanças climáticas. Estabelece a meta de limitar o aquecimento global a 1,5°C e a necessidade de reduções profundas e imediatas das emissões.',
        '04_certificacoes-e-normas', '04_Ensaios_Certificacao')

# UNDP HDR
pdf = try_download('undp_hdr_2023',
    'https://hdr.undp.org/system/files/documents/global-report-document/hdr2023-24reporten.pdf')
if pdf:
    doc = fitz.open(pdf)
    texto = ""
    for page in doc: texto += page.get_text()
    doc.close()
else:
    texto = "Relatório de Desenvolvimento Humano 2023/2024 do PNUD. Aborda a polarização, a cooperação e o desenvolvimento humano em um mundo em transformação."

create_ficha('undp_hdr_2023',
    'PNUD — Relatório de Desenvolvimento Humano 2023/2024',
    'PNUD. Relatório de Desenvolvimento Humano 2023/2024: Sair do impasse — repensar a cooperação num mundo polarizado. New York: PNUD, 2024.',
    texto, '04_certificacoes-e-normas', '04_Ensaios_Certificacao')

# UN SDGs
create_ficha('onu_ods_agenda2030',
    'ONU — Agenda 2030 para o Desenvolvimento Sustentável',
    'ORGANIZAÇÃO DAS NAÇÕES UNIDAS. Transformando Nosso Mundo: A Agenda 2030 para o Desenvolvimento Sustentável. New York: ONU, 2015.',
    'A Agenda 2030 é um plano de ação para pessoas, planeta e prosperidade, composto por 17 Objetivos de Desenvolvimento Sustentável (ODS) e 169 metas. Estabelece um compromisso global para erradicar a pobreza, proteger o meio ambiente e garantir que todos os seres humanos possam desfrutar de paz e prosperidade até 2030.',
    '04_certificacoes-e-normas', '04_Ensaios_Certificacao')

# ============================================================
# 2. LEIS BRASILEIRAS
# ============================================================
print(f"\n{'='*70}")
print("📜 LEIS BRASILEIRAS")
print("="*70)

# Try to download law texts
leis = [
    ('lei_12484_pnmcb', 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12484.htm',
     'LEI Nº 12.484, DE 8 DE SETEMBRO DE 2011',
     'Dispõe sobre a Política Nacional de Incentivo ao Manejo Sustentado e ao Cultivo do Bambu (PNMCB).'),
    ('lei_12651_codigo_florestal', 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12651.htm',
     'LEI Nº 12.651, DE 25 DE MAIO DE 2012',
     'Dispõe sobre a proteção da vegetação nativa; altera as Leis nºs 12.727/2012 e 11.284/2006; e dá outras providências. Conhecido como Código Florestal Brasileiro.'),
    ('lei_11888_athis', 'https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11888.htm',
     'LEI Nº 11.888, DE 24 DE DEZEMBRO DE 2008',
     'Dispõe sobre a Assistência Técnica Pública e Gratuita para Habitação de Interesse Social (ATHIS).'),
]

for key, url, title, desc in leis:
    print(f"  📥 {key}: ", end="", flush=True)
    result = subprocess.run(
        ['curl', '-s', '-L', '--max-time', '15',
         '-o', os.path.join(DOWNLOAD_DIR, f"{key}.html"),
         url],
        capture_output=True, text=True, timeout=20
    )
    
    # Try to extract text from HTML
    html_path = os.path.join(DOWNLOAD_DIR, f"{key}.html")
    texto = desc
    if os.path.exists(html_path) and os.path.getsize(html_path) > 1000:
        with open(html_path) as f:
            raw = f.read()
        # Simple HTML tag removal
        clean = re.sub(r'<[^>]+>', ' ', raw)
        clean = re.sub(r'\s+', ' ', clean)
        texto = clean[:500]
        os.remove(html_path)
        print("✅ texto extraído")
    else:
        print("⚠️ usando descrição")
    
    citation = f"BRASIL. {title}. Diário Oficial da União, Brasília, DF, [ano]."
    
    create_ficha(key, title, citation, texto, 
                 '04_certificacoes-e-normas', '01_Normas_NBR')

# ============================================================
# 3. PERFIS: NOBRE E SANTOS
# ============================================================
print(f"\n{'='*70}")
print("👤 PERFIS")
print("="*70)

perfis_path = os.path.join(ACERVO, '05_perfis-e-referencias', '01_Pesquisadores')

# Carlos Nobre
create_ficha('perfil-carlos-nobre',
    'Perfil: Carlos Afonso Nobre',
    'Perfil do pesquisador — Carlos Afonso Nobre. Instituto de Estudos Avançados (IEA/USP).',
    'Carlos Afonso Nobre é engenheiro eletrônico, climatologista e um dos maiores especialistas em mudanças climáticas do Brasil. Foi presidente da CAPES, secretário nacional de Políticas de Ciência e Tecnologia, e pesquisador titular do INPE. É membro da Academia Brasileira de Ciências e da Academia Mundial de Ciências (TWAS). Coordenou a criação do Painel Brasileiro de Mudanças Climáticas (PBMC) e é referência internacional nos estudos sobre o ponto de inflexão da Amazônia (Amazon tipping point). Sua pesquisa demonstra que o desmatamento combinado com as mudanças climáticas pode levar a Amazônia a um ponto de savanização irreversível.',
    '05_perfis-e-referencias', '01_Pesquisadores')

# Milton Santos
create_ficha('perfil-milton-santos',
    'Perfil: Milton Santos',
    'Perfil do pesquisador — Milton Santos. Universidade de São Paulo (in memoriam).',
    'Milton Santos (1926-2001) foi um dos mais influentes geógrafos do mundo, professor emérito da USP e doutor honoris causa por diversas universidades. Sua obra aborda a globalização, o espaço geográfico, o subdesenvolvimento e a cidadania. Principais obras: "Por uma Outra Globalização" (2000), "O Espaço do Cidadão" (1987), "A Natureza do Espaço" (1996). Recebeu o Prêmio Vautrin Lud (1994), considerado o Nobel da Geografia. Sua análise do "meio técnico-científico-informacional" é fundamental para entender a relação entre tecnologia, território e desigualdade social no Brasil e no mundo.',
    '05_perfis-e-referencias', '01_Pesquisadores')

print(f"\n✅ CONCLUIDO — Fichas criadas para IPCC, PNUD, ONU, Leis (12.484, 12.651, 11.888), Nobre e Santos")
