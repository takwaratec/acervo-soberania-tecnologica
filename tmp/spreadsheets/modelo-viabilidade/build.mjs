import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outputDir = path.resolve("../../../outputs/curadoria-cadernos-2026-07-22");
const previewDir = path.resolve("previews");
await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(previewDir, { recursive: true });

const wb = Workbook.create();
const names = ["LEIA-ME", "Premissas", "CAPEX", "OPEX", "Demanda", "Resumo", "Fluxo 12m", "Decisão", "Fontes"];
for (const name of names) wb.worksheets.add(name);

const navy = "#19324D";
const teal = "#2F6F68";
const paleTeal = "#DDEEEB";
const paleBlue = "#E8F0F7";
const paleYellow = "#FFF3BF";
const paleRed = "#FCE8E6";
const paleGreen = "#E3F2E7";
const gray = "#667085";
const line = "#CBD5E1";
const currencyFmt = 'R$ #,##0;[Red](R$ #,##0);-';
const pctFmt = '0.0%;[Red](0.0%);-';
const numberFmt = '#,##0.0;[Red](#,##0.0);-';

function baseSheet(sheet, freezeRows = 3) {
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(freezeRows);
}

function title(sheet, range, text, subtitle) {
  sheet.mergeCells(range);
  const r = sheet.getRange(range);
  r.values = [[text]];
  r.format = { fill: navy, font: { bold: true, color: "#FFFFFF", size: 16 }, verticalAlignment: "center", wrapText: true };
  r.format.rowHeight = 34;
  if (subtitle) {
    sheet.mergeCells(subtitle.range);
    const s = sheet.getRange(subtitle.range);
    s.values = [[subtitle.text]];
    s.format = { fill: paleBlue, font: { color: navy, italic: true }, wrapText: true, verticalAlignment: "center" };
    s.format.rowHeight = 30;
  }
}

function header(range) {
  range.format = {
    fill: teal,
    font: { bold: true, color: "#FFFFFF" },
    wrapText: true,
    verticalAlignment: "center",
    borders: { preset: "outside", style: "thin", color: line },
  };
  range.format.rowHeight = 28;
}

function section(range) {
  range.format = { fill: navy, font: { bold: true, color: "#FFFFFF" }, wrapText: true };
}

function styleInputs(range, numberFormat = undefined) {
  range.format = {
    fill: paleYellow,
    font: { color: "#0000FF" },
    wrapText: true,
    borders: { preset: "outside", style: "thin", color: line },
  };
  if (numberFormat) range.format.numberFormat = numberFormat;
}

function styleFormula(range, numberFormat = undefined) {
  range.format = { font: { color: "#000000" }, borders: { preset: "outside", style: "thin", color: line } };
  if (numberFormat) range.format.numberFormat = numberFormat;
}

function setWidths(sheet, widths) {
  for (const [col, width] of Object.entries(widths)) sheet.getRange(`${col}:${col}`).format.columnWidth = width;
}

// LEIA-ME
{
  const s = wb.worksheets.getItem("LEIA-ME");
  baseSheet(s, 4);
  title(s, "A1:H1", "Modelo de viabilidade econômica e continuidade territorial", {
    range: "A2:H2",
    text: "Instrumento preenchível — versão 0.1 — Fabio Takwara — 22 jul. 2026",
  });
  s.mergeCells("A4:H4");
  s.getRange("A4:H4").values = [["FINALIDADE"]];
  section(s.getRange("A4:H4"));
  s.mergeCells("A5:H7");
  s.getRange("A5:H7").values = [["Organizar dados e cenários antes de investir, contrair dívida ou prometer implantação. O arquivo não contém preços, demanda, produtividade ou rentabilidade presumidos. Célula vazia significa informação pendente. Um resultado legítimo pode ser avançar, redimensionar, compartilhar, adiar, substituir ou encerrar."]];
  s.getRange("A5:H7").format = { wrapText: true, verticalAlignment: "top", fill: "#FFFFFF", borders: { preset: "outside", style: "thin", color: line } };
  s.getRange("A5:H7").format.rowHeight = 26;

  s.mergeCells("A9:H9");
  s.getRange("A9:H9").values = [["ORDEM DE PREENCHIMENTO"]];
  section(s.getRange("A9:H9"));
  const steps = [
    ["1", "Premissas", "Delimite território, produto, unidade funcional, estágio técnico e parâmetros dos três cenários."],
    ["2", "CAPEX", "Registre investimento completo, inclusive instalação, qualidade, segurança e encerramento."],
    ["3", "OPEX", "Registre custos mensais indiretos/fixos e fontes. Custos diretos unitários ficam em Demanda."],
    ["4", "Demanda", "Insira quantidade, preço e custo variável somente quando houver fundamento e condição de conformidade."],
    ["5", "Fluxo 12m", "Preencha o fator mensal de operação; fórmulas projetam caixa sem esconder déficits."],
    ["6", "Decisão", "Documente evidências, responsáveis e portões atendidos, pendentes ou não atendidos."],
    ["7", "Fontes", "Cadastre cotações, medições, contratos, chamadas e datas-base."],
  ];
  s.getRange("A10:C10").values = [["Etapa", "Aba", "Ação"]];
  header(s.getRange("A10:C10"));
  s.getRange(`A11:C${10 + steps.length}`).values = steps;
  s.getRange(`A11:C${10 + steps.length}`).format = { wrapText: true, verticalAlignment: "top", borders: { preset: "inside", style: "thin", color: line } };

  s.mergeCells("E10:H10");
  s.getRange("E10:H10").values = [["LEGENDA"]];
  header(s.getRange("E10:H10"));
  const legend = [
    ["Entrada editável", "texto azul / fundo amarelo"],
    ["Fórmula", "texto preto"],
    ["Referência entre abas", "texto verde"],
    ["Bloqueio ou lacuna", "fundo vermelho claro"],
  ];
  s.getRange("E11:F14").values = legend;
  s.getRange("E11:E14").format.font = { bold: true };
  s.getRange("F11:F14").format.wrapText = true;
  s.getRange("E11:F14").format.borders = { preset: "inside", style: "thin", color: line };
  s.getRange("E11:F11").format = { fill: paleYellow, font: { color: "#0000FF" } };
  s.getRange("E12:F12").format.font = { color: "#000000" };
  s.getRange("E13:F13").format.font = { color: "#008000" };
  s.getRange("E14:F14").format.fill = paleRed;

  s.mergeCells("A20:H20");
  s.getRange("A20:H20").values = [["AVISO: este modelo não é recomendação financeira, orçamento de obra, parecer contábil, autorização de endividamento ou validação técnica. Toda entrada deve indicar fonte e data-base."]];
  s.getRange("A20:H20").format = { fill: paleRed, font: { bold: true, color: "#8A1C1C" }, wrapText: true, verticalAlignment: "center", borders: { preset: "outside", style: "thin", color: "#D14343" } };
  s.getRange("A20:H20").format.rowHeight = 50;
  setWidths(s, { A: 9, B: 18, C: 58, D: 3, E: 24, F: 30, G: 14, H: 14 });
}

// Premissas
{
  const s = wb.worksheets.getItem("Premissas");
  baseSheet(s, 4);
  title(s, "A1:F1", "Premissas e cenários", { range: "A2:F2", text: "Preencha somente valores sustentados por fonte, medição ou hipótese explicitamente identificada." });
  s.getRange("A4:F4").values = [["Variável", "Restritivo", "Base", "Expansão condicionada", "Unidade", "Fonte / nota"]];
  header(s.getRange("A4:F4"));
  const rows = [
    ["Projeto / unidade analisada", null, null, null, "texto", null],
    ["Território", null, null, null, "texto", null],
    ["Produto ou serviço", null, null, null, "texto", null],
    ["Unidade funcional", null, null, null, "texto", null],
    ["Estágio técnico", null, null, null, "texto", null],
    ["Capacidade nominal mensal", null, null, null, "unid./mês", null],
    ["Utilização da capacidade", null, null, null, "%", null],
    ["Rendimento aproveitável", null, null, null, "%", null],
    ["Estoque de matéria-prima", null, null, null, "dias", null],
    ["Processamento e liberação", null, null, null, "dias", null],
    ["Estoque de produto", null, null, null, "dias", null],
    ["Prazo de fornecedores", null, null, null, "dias", null],
    ["Prazo de recebimento", null, null, null, "dias", null],
    ["Caixa mínimo", null, null, null, "R$", null],
    ["Reserva mensal de manutenção", null, null, null, "% do OPEX", null],
    ["Serviço mensal da dívida", null, null, null, "R$", null],
    ["Subvenção/receita pública mensal", null, null, null, "R$", null],
    ["Parcela de custos retida no território", null, null, null, "%", null],
  ];
  s.getRange(`A5:F${4 + rows.length}`).values = rows;
  s.getRange(`A5:A${4 + rows.length}`).format.font = { bold: true };
  styleInputs(s.getRange(`B5:D${4 + rows.length}`));
  styleInputs(s.getRange(`F5:F${4 + rows.length}`));
  s.getRange("B11:D12").format.numberFormat = pctFmt;
  s.getRange("B18:D18").format.numberFormat = currencyFmt;
  s.getRange("B19:D19").format.numberFormat = pctFmt;
  s.getRange("B20:D21").format.numberFormat = currencyFmt;
  s.getRange("B22:D22").format.numberFormat = pctFmt;
  s.getRange(`A5:F${4 + rows.length}`).format.wrapText = true;
  s.getRange(`A5:F${4 + rows.length}`).format.borders = { preset: "inside", style: "thin", color: line };
  setWidths(s, { A: 34, B: 18, C: 18, D: 22, E: 16, F: 48 });
}

// CAPEX
{
  const s = wb.worksheets.getItem("CAPEX");
  baseSheet(s, 4);
  title(s, "A1:H1", "Investimento inicial — CAPEX", { range: "A2:H2", text: "Inclua custos pagos por terceiros e itens de proteção/encerramento; doação não transforma custo em zero." });
  s.getRange("A4:H4").values = [["ID", "Grupo", "Item", "Restritivo (R$)", "Base (R$)", "Expansão (R$)", "Fonte ID", "Nota / condição"]];
  header(s.getRange("A4:H4"));
  const items = [
    ["C01", "Infraestrutura", "Adequação física, elétrica, água e ventilação"],
    ["C02", "Equipamentos", "Processo principal"],
    ["C03", "Equipamentos", "Medição, controle e calibração"],
    ["C04", "Segurança", "EPC, emergência e prevenção de incêndio"],
    ["C05", "Instalação", "Frete, montagem e partida"],
    ["C06", "Qualidade", "Ensaios, avaliação e documentação inicial"],
    ["C07", "Ambiental", "Contenção, emissões, efluentes e resíduos"],
    ["C08", "Formação", "Treinamento inicial e materiais"],
    ["C09", "Capital de partida", "Lote inicial e consumíveis"],
    ["C10", "Encerramento", "Desmobilização e destinação segura"],
    ["C11", "Contingência", "Incertezas explicitamente justificadas"],
    ["C12", "Outro", "Item adicional identificado"],
  ];
  const data = items.map(r => [...r, null, null, null, null, null]);
  s.getRange(`A5:H${4 + data.length}`).values = data;
  styleInputs(s.getRange(`D5:F${4 + data.length}`), currencyFmt);
  styleInputs(s.getRange(`G5:H${4 + data.length}`));
  const totalRow = 5 + data.length;
  s.getRange(`A${totalRow}:C${totalRow}`).merge();
  s.getRange(`A${totalRow}:C${totalRow}`).values = [["TOTAL CAPEX"]];
  s.getRange(`D${totalRow}:F${totalRow}`).formulas = [[`=SUM(D5:D${totalRow - 1})`, `=SUM(E5:E${totalRow - 1})`, `=SUM(F5:F${totalRow - 1})`]];
  s.getRange(`A${totalRow}:F${totalRow}`).format = { fill: paleBlue, font: { bold: true }, borders: { preset: "doubleBottom", style: "thin", color: navy } };
  s.getRange(`D${totalRow}:F${totalRow}`).format.numberFormat = currencyFmt;
  s.getRange(`A5:H${totalRow}`).format.wrapText = true;
  s.getRange(`A5:H${totalRow}`).format.borders = { preset: "inside", style: "thin", color: line };
  setWidths(s, { A: 9, B: 18, C: 42, D: 18, E: 18, F: 18, G: 14, H: 42 });
}

// OPEX
{
  const s = wb.worksheets.getItem("OPEX");
  baseSheet(s, 4);
  title(s, "A1:I1", "Custos operacionais mensais — OPEX", { range: "A2:I2", text: "Custos diretos unitários do produto ficam na aba Demanda para evitar dupla contagem." });
  s.getRange("A4:I4").values = [["ID", "Grupo", "Item mensal", "Restritivo (R$)", "Base (R$)", "Expansão (R$)", "Fonte ID", "Data-base", "Nota"]];
  header(s.getRange("A4:I4"));
  const items = [
    ["O01", "Trabalho", "Coordenação e administração"],
    ["O02", "Trabalho", "Remuneração fixa e encargos"],
    ["O03", "Utilidades", "Energia, água e comunicação de base"],
    ["O04", "Manutenção", "Preventiva, corretiva e peças"],
    ["O05", "Qualidade", "Laboratório, calibração e rastreabilidade"],
    ["O06", "Segurança", "EPI/EPC, inspeção e emergência"],
    ["O07", "Ambiental", "Efluentes, emissões e rejeitos"],
    ["O08", "Infraestrutura", "Aluguel, seguros, licenças e taxas"],
    ["O09", "Logística", "Custos fixos de coleta e entrega"],
    ["O10", "Formação", "Treinamento continuado"],
    ["O11", "Pós-entrega", "Assistência, garantia e avaliação"],
    ["O12", "Administração", "Contabilidade e prestação de contas"],
    ["O13", "Parada", "Custo de ociosidade e indisponibilidade"],
    ["O14", "Outro", "Item adicional identificado"],
  ];
  const data = items.map(r => [...r, null, null, null, null, null, null]);
  s.getRange(`A5:I${4 + data.length}`).values = data;
  styleInputs(s.getRange(`D5:F${4 + data.length}`), currencyFmt);
  styleInputs(s.getRange(`G5:I${4 + data.length}`));
  s.getRange(`H5:H${4 + data.length}`).format.numberFormat = "yyyy-mm-dd";
  const totalRow = 5 + data.length;
  s.getRange(`A${totalRow}:C${totalRow}`).merge();
  s.getRange(`A${totalRow}:C${totalRow}`).values = [["TOTAL OPEX MENSAL"]];
  s.getRange(`D${totalRow}:F${totalRow}`).formulas = [[`=SUM(D5:D${totalRow - 1})`, `=SUM(E5:E${totalRow - 1})`, `=SUM(F5:F${totalRow - 1})`]];
  s.getRange(`A${totalRow}:F${totalRow}`).format = { fill: paleBlue, font: { bold: true }, borders: { preset: "doubleBottom", style: "thin", color: navy } };
  s.getRange(`D${totalRow}:F${totalRow}`).format.numberFormat = currencyFmt;
  s.getRange(`A5:I${totalRow}`).format.wrapText = true;
  s.getRange(`A5:I${totalRow}`).format.borders = { preset: "inside", style: "thin", color: line };
  setWidths(s, { A: 9, B: 17, C: 40, D: 17, E: 17, F: 17, G: 13, H: 14, I: 40 });
}

// Demanda
{
  const s = wb.worksheets.getItem("Demanda");
  baseSheet(s, 5);
  title(s, "A1:S1", "Demanda, receita e custo variável direto", { range: "A2:S2", text: "Não atribua receita a coproduto sem especificação, uso seguro, demanda e condição de comercialização." });
  s.getRange("A4:D4").values = [["Produto/serviço", "Conformidade atual", "Evidência de demanda", "Fonte ID"]];
  header(s.getRange("A4:D4"));
  s.getRange("E4:G4").values = [["Restritivo: qtd./mês", "Preço unit. (R$)", "Custo var. unit. (R$)"]];
  s.getRange("H4:J4").values = [["Base: qtd./mês", "Preço unit. (R$)", "Custo var. unit. (R$)"]];
  s.getRange("K4:M4").values = [["Expansão: qtd./mês", "Preço unit. (R$)", "Custo var. unit. (R$)"]];
  header(s.getRange("E4:M4"));
  s.getRange("N4:S4").values = [["Receita restr.", "Receita base", "Receita exp.", "Custo var. restr.", "Custo var. base", "Custo var. exp."]];
  header(s.getRange("N4:S4"));
  const rows = 15;
  const blank = Array.from({ length: rows }, () => Array(19).fill(null));
  s.getRange(`A5:S${4 + rows}`).values = blank;
  styleInputs(s.getRange(`A5:M${4 + rows}`));
  s.getRange(`E5:M${4 + rows}`).format.numberFormat = currencyFmt;
  s.getRange(`N5:S${4 + rows}`).format.numberFormat = currencyFmt;
  s.getRange("N5").formulas = [["=E5*F5"]];
  s.getRange(`N5:N${4 + rows}`).fillDown();
  s.getRange("O5").formulas = [["=H5*I5"]];
  s.getRange(`O5:O${4 + rows}`).fillDown();
  s.getRange("P5").formulas = [["=K5*L5"]];
  s.getRange(`P5:P${4 + rows}`).fillDown();
  s.getRange("Q5").formulas = [["=E5*G5"]];
  s.getRange(`Q5:Q${4 + rows}`).fillDown();
  s.getRange("R5").formulas = [["=H5*J5"]];
  s.getRange(`R5:R${4 + rows}`).fillDown();
  s.getRange("S5").formulas = [["=K5*M5"]];
  s.getRange(`S5:S${4 + rows}`).fillDown();
  styleFormula(s.getRange(`N5:S${4 + rows}`), currencyFmt);
  const tr = 5 + rows;
  s.getRange(`A${tr}:M${tr}`).merge();
  s.getRange(`A${tr}:M${tr}`).values = [["TOTAIS MENSAIS"]];
  s.getRange(`N${tr}:S${tr}`).formulas = [[`=SUM(N5:N${tr - 1})`, `=SUM(O5:O${tr - 1})`, `=SUM(P5:P${tr - 1})`, `=SUM(Q5:Q${tr - 1})`, `=SUM(R5:R${tr - 1})`, `=SUM(S5:S${tr - 1})`]];
  s.getRange(`A${tr}:S${tr}`).format = { fill: paleBlue, font: { bold: true }, borders: { preset: "doubleBottom", style: "thin", color: navy } };
  s.getRange(`N${tr}:S${tr}`).format.numberFormat = currencyFmt;
  s.getRange(`A5:S${tr}`).format.wrapText = true;
  s.getRange(`A5:S${tr}`).format.borders = { preset: "inside", style: "thin", color: line };
  s.getRange(`B5:B${tr - 1}`).dataValidation = { rule: { type: "list", values: ["Não definido", "Experimental", "Protótipo", "Piloto", "Conforme para escopo", "Não aplicável"] } };
  setWidths(s, { A: 30, B: 20, C: 32, D: 12, E: 14, F: 15, G: 16, H: 14, I: 15, J: 16, K: 14, L: 15, M: 16, N: 16, O: 16, P: 16, Q: 16, R: 16, S: 16 });
}

// Resumo
{
  const s = wb.worksheets.getItem("Resumo");
  baseSheet(s, 5);
  title(s, "A1:E1", "Resumo comparativo dos cenários", { range: "A2:E2", text: "Resultados permanecem vazios ou nulos até que as entradas sejam preenchidas e documentadas." });
  s.getRange("A4:E4").values = [["Indicador", "Restritivo", "Base", "Expansão condicionada", "Leitura"]];
  header(s.getRange("A4:E4"));
  const labels = [
    ["CAPEX total", null, null, null, "Investimento completo, incluindo segurança e encerramento"],
    ["Receita mensal", null, null, null, "Somente demanda fundamentada"],
    ["Custo variável direto", null, null, null, "Custos unitários multiplicados pela quantidade"],
    ["Margem de contribuição", null, null, null, "Receita menos custo variável direto"],
    ["OPEX mensal", null, null, null, "Custos indiretos/fixos"],
    ["Resultado operacional mensal", null, null, null, "Antes de dívida e subvenção"],
    ["Margem de contribuição (%)", null, null, null, "Base para ponto de equilíbrio em valor"],
    ["Ponto de equilíbrio (R$ receita)", null, null, null, "Não calculado sem margem positiva"],
    ["Capital de giro estimado", null, null, null, "Estimativa simplificada por prazos e caixa mínimo"],
    ["Necessidade inicial (CAPEX + giro)", null, null, null, "Não inclui retorno garantido"],
    ["Maior déficit acumulado em 12m", null, null, null, "Depende dos fatores mensais do fluxo"],
    ["Valor retido no território/mês", null, null, null, "Parcela informada dos custos operacionais"],
  ];
  s.getRange(`A5:E${4 + labels.length}`).values = labels;
  const capexTotalRow = 17;
  const opexTotalRow = 19;
  const demandTotalRow = 20;
  s.getRange("B5:D5").formulas = [[`='CAPEX'!D${capexTotalRow}`, `='CAPEX'!E${capexTotalRow}`, `='CAPEX'!F${capexTotalRow}`]];
  s.getRange("B6:D6").formulas = [[`='Demanda'!N${demandTotalRow}`, `='Demanda'!O${demandTotalRow}`, `='Demanda'!P${demandTotalRow}`]];
  s.getRange("B7:D7").formulas = [[`='Demanda'!Q${demandTotalRow}`, `='Demanda'!R${demandTotalRow}`, `='Demanda'!S${demandTotalRow}`]];
  s.getRange("B8:D8").formulas = [["=B6-B7", "=C6-C7", "=D6-D7"]];
  s.getRange("B9:D9").formulas = [[`='OPEX'!D${opexTotalRow}`, `='OPEX'!E${opexTotalRow}`, `='OPEX'!F${opexTotalRow}`]];
  s.getRange("B10:D10").formulas = [["=B8-B9", "=C8-C9", "=D8-D9"]];
  s.getRange("B11:D11").formulas = [["=IF(B6>0,B8/B6,0)", "=IF(C6>0,C8/C6,0)", "=IF(D6>0,D8/D6,0)"]];
  s.getRange("B12:D12").formulas = [["=IF(B11>0,B9/B11,0)", "=IF(C11>0,C9/C11,0)", "=IF(D11>0,D9/D11,0)"]];
  s.getRange("B13:D13").formulas = [[
    "=B6/30*'Premissas'!B17+B7/30*('Premissas'!B13+'Premissas'!B14+'Premissas'!B15)-B7/30*'Premissas'!B16+'Premissas'!B18",
    "=C6/30*'Premissas'!C17+C7/30*('Premissas'!C13+'Premissas'!C14+'Premissas'!C15)-C7/30*'Premissas'!C16+'Premissas'!C18",
    "=D6/30*'Premissas'!D17+D7/30*('Premissas'!D13+'Premissas'!D14+'Premissas'!D15)-D7/30*'Premissas'!D16+'Premissas'!D18",
  ]];
  s.getRange("B14:D14").formulas = [["=B5+B13", "=C5+C13", "=D5+D13"]];
  s.getRange("B15:D15").formulas = [["=-MIN('Fluxo 12m'!B14:M14,0)", "=-MIN('Fluxo 12m'!B26:M26,0)", "=-MIN('Fluxo 12m'!B38:M38,0)"]];
  s.getRange("B16:D16").formulas = [["=B9*'Premissas'!B22", "=C9*'Premissas'!C22", "=D9*'Premissas'!D22"]];
  styleFormula(s.getRange("B5:D16"), currencyFmt);
  s.getRange("B11:D11").format.numberFormat = pctFmt;
  s.getRange("A5:A16").format.font = { bold: true };
  s.getRange("E5:E16").format.wrapText = true;
  s.getRange("B5:D16").format.font = { color: "#008000" };
  s.getRange("A5:E16").format.borders = { preset: "inside", style: "thin", color: line };
  s.mergeCells("A19:E19");
  s.getRange("A19:E19").values = [["O modelo compara continuidade e risco; não calcula valor da empresa, retorno garantido ou recomendação de investimento."]];
  s.getRange("A19:E19").format = { fill: paleRed, font: { bold: true, color: "#8A1C1C" }, wrapText: true };
  setWidths(s, { A: 34, B: 20, C: 20, D: 24, E: 48 });
}

// Fluxo 12m
{
  const s = wb.worksheets.getItem("Fluxo 12m");
  baseSheet(s, 4);
  title(s, "A1:M1", "Fluxo de caixa simplificado — 12 meses", { range: "A2:M2", text: "Preencha o fator mensal de operação (0% a 100%). O modelo não presume rampa nem mercado." });
  const months = Array.from({ length: 12 }, (_, i) => `M${i + 1}`);
  const blocks = [
    { name: "RESTRITIVO", start: 4, col: "B", summaryCol: "B" },
    { name: "BASE", start: 16, col: "C", summaryCol: "C" },
    { name: "EXPANSÃO CONDICIONADA", start: 28, col: "D", summaryCol: "D" },
  ];
  for (const b of blocks) {
    const r = b.start;
    s.mergeCells(`A${r}:M${r}`);
    s.getRange(`A${r}:M${r}`).values = [[b.name]];
    section(s.getRange(`A${r}:M${r}`));
    s.getRange(`A${r + 1}:M${r + 1}`).values = [["Linha", ...months]];
    header(s.getRange(`A${r + 1}:M${r + 1}`));
    const labels = ["Fator de operação", "Receita", "Custo variável direto", "OPEX", "Dívida", "Subvenção", "CAPEX + giro", "Fluxo líquido", "Caixa acumulado"];
    s.getRange(`A${r + 2}:A${r + 10}`).values = labels.map(x => [x]);
    s.getRange(`A${r + 2}:A${r + 10}`).format.font = { bold: true };
    styleInputs(s.getRange(`B${r + 2}:M${r + 2}`), pctFmt);
    const sc = b.summaryCol;
    for (let c = 0; c < 12; c++) {
      const col = String.fromCharCode("B".charCodeAt(0) + c);
      s.getRange(`${col}${r + 3}`).formulas = [[`='Resumo'!${sc}6*${col}${r + 2}`]];
      s.getRange(`${col}${r + 4}`).formulas = [[`=-'Resumo'!${sc}7*${col}${r + 2}`]];
      s.getRange(`${col}${r + 5}`).formulas = [[`=-'Resumo'!${sc}9`]];
      const premCol = sc;
      s.getRange(`${col}${r + 6}`).formulas = [[`=-'Premissas'!${premCol}20`]];
      s.getRange(`${col}${r + 7}`).formulas = [[`='Premissas'!${premCol}21`]];
      s.getRange(`${col}${r + 8}`).formulas = [[c === 0 ? `=-'Resumo'!${sc}14` : "=0"]];
      s.getRange(`${col}${r + 9}`).formulas = [[`=SUM(${col}${r + 3}:${col}${r + 8})`]];
      const prior = c === 0 ? "0" : `${String.fromCharCode(col.charCodeAt(0) - 1)}${r + 10}`;
      s.getRange(`${col}${r + 10}`).formulas = [[`=${prior}+${col}${r + 9}`]];
    }
    styleFormula(s.getRange(`B${r + 3}:M${r + 10}`), currencyFmt);
    s.getRange(`B${r + 3}:M${r + 10}`).format.font = { color: "#008000" };
    s.getRange(`A${r + 1}:M${r + 10}`).format.borders = { preset: "inside", style: "thin", color: line };
  }
  setWidths(s, { A: 27, B: 13, C: 13, D: 13, E: 13, F: 13, G: 13, H: 13, I: 13, J: 13, K: 13, L: 13, M: 13 });
}

// Decisão
{
  const s = wb.worksheets.getItem("Decisão");
  baseSheet(s, 5);
  title(s, "A1:H1", "Portões de decisão e registro", { range: "A2:H2", text: "Status deve refletir evidência documentada. 'Não atendido' pode encerrar ou redimensionar a proposta." });
  s.getRange("A4:H4").values = [["Portão", "Pergunta", "Status", "Evidência / Fonte ID", "Responsável", "Data", "Decisão / ação", "Próxima revisão"]];
  header(s.getRange("A4:H4"));
  const gates = [
    ["Demanda", "Existe usuário/comprador, quantidade e condição de pagamento verificáveis?"],
    ["Configuração", "Capacidade e produtividade estão ligadas a protótipo ou ensaio identificado?"],
    ["Custos completos", "CAPEX, OPEX, qualidade, segurança, resíduos e encerramento estão incluídos?"],
    ["Capital de giro", "O maior déficit pode ser coberto sem dívida informal imposta?"],
    ["Manutenção", "Peças, competência, tempo parado e reposição estão previstos?"],
    ["Conformidade", "Produto/processo pode avançar no escopo e estágio declarados?"],
    ["Território", "Diagnóstico, consentimento, alternativas e direito de recusa estão registrados?"],
    ["Distribuição", "Remuneração, benefícios, dívida e passivos estão atribuídos com transparência?"],
    ["Cenário restritivo", "Há resposta para queda de demanda, custo maior, atraso e falha?"],
    ["Saída segura", "Existe plano de interrupção, desmobilização e destino de passivos?"],
  ];
  const data = gates.map(x => [x[0], x[1], "Pendente", null, null, null, null, null]);
  s.getRange(`A5:H${4 + data.length}`).values = data;
  styleInputs(s.getRange(`C5:H${4 + data.length}`));
  s.getRange(`C5:C${4 + data.length}`).dataValidation = { rule: { type: "list", values: ["Pendente", "Atendido", "Não atendido", "Não aplicável"] } };
  s.getRange(`F5:F${4 + data.length}`).format.numberFormat = "yyyy-mm-dd";
  s.getRange(`H5:H${4 + data.length}`).format.numberFormat = "yyyy-mm-dd";
  s.getRange(`A5:H${4 + data.length}`).format.wrapText = true;
  s.getRange(`A5:H${4 + data.length}`).format.borders = { preset: "inside", style: "thin", color: line };
  s.getRange(`A5:H${4 + data.length}`).format.rowHeight = 34;
  const statusRow = 17;
  s.mergeCells(`A${statusRow}:B${statusRow}`);
  s.getRange(`A${statusRow}:B${statusRow}`).values = [["STATUS DO MODELO"]];
  s.getRange(`C${statusRow}`).formulas = [[`=IF(COUNTIF(C5:C14,"Não atendido")>0,"BLOQUEADO",IF(COUNTIF(C5:C14,"Pendente")>0,"PENDENTE","PRONTO PARA REVISÃO"))`]];
  s.mergeCells(`C${statusRow}:H${statusRow}`);
  s.getRange(`A${statusRow}:H${statusRow}`).format = { fill: paleBlue, font: { bold: true }, borders: { preset: "outside", style: "medium", color: navy } };
  setWidths(s, { A: 20, B: 52, C: 18, D: 32, E: 20, F: 14, G: 34, H: 15 });
}

// Fontes
{
  const s = wb.worksheets.getItem("Fontes");
  baseSheet(s, 4);
  title(s, "A1:H1", "Fontes e trilha de auditoria", { range: "A2:H2", text: "Uma linha por cotação, medição, contrato, chamada, norma ou hipótese documentada." });
  s.getRange("A4:H4").values = [["Fonte ID", "Item/variável", "Valor/descrição", "Unidade", "Data-base", "Fonte/emitente", "URL ou caminho", "Notas e validade"]];
  header(s.getRange("A4:H4"));
  const rows = 50;
  s.getRange(`A5:H${4 + rows}`).values = Array.from({ length: rows }, () => Array(8).fill(null));
  styleInputs(s.getRange(`A5:H${4 + rows}`));
  s.getRange(`E5:E${4 + rows}`).format.numberFormat = "yyyy-mm-dd";
  s.getRange(`A5:H${4 + rows}`).format.wrapText = true;
  s.getRange(`A5:H${4 + rows}`).format.borders = { preset: "inside", style: "thin", color: line };
  setWidths(s, { A: 13, B: 28, C: 28, D: 14, E: 14, F: 26, G: 48, H: 42 });
}

// Workbook comments author and compact metadata.
wb.comments.setSelf({ displayName: "Fabio Takwara" });

// Inspect key regions and formula errors before export.
const checks = [];
checks.push((await wb.inspect({ kind: "table", range: "Resumo!A1:E19", include: "values,formulas", tableMaxRows: 20, tableMaxCols: 8 })).ndjson);
checks.push((await wb.inspect({ kind: "table", range: "Decisão!A1:H17", include: "values,formulas", tableMaxRows: 20, tableMaxCols: 10 })).ndjson);
checks.push((await wb.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 300 }, summary: "final formula error scan" })).ndjson);
await fs.writeFile(path.join(previewDir, "qa-inspect.ndjson"), checks.join("\n"), "utf8");

for (const sheetName of names) {
  const preview = await wb.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(path.join(previewDir, `${sheetName.replace(/[^a-zA-Z0-9]+/g, "-")}.png`), new Uint8Array(await preview.arrayBuffer()));
}

const out = await SpreadsheetFile.exportXlsx(wb);
await out.save(path.join(outputDir, "modelo-viabilidade-economica-territorial-v0.1.xlsx"));
console.log(path.join(outputDir, "modelo-viabilidade-economica-territorial-v0.1.xlsx"));
