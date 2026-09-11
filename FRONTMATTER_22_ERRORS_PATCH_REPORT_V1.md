# Relatório de patch — 22 erros globais de front matter

Escopo exclusivo: correções técnicas nos 10 arquivos de `docs/analyses/pu-vegetal/`, fora de `BAM-CHN-001`. Nenhum corpo, claim, referência bibliográfica ou estado documental foi alterado.

Classificação: 10 `MISSING_REQUIRED_FIELD`, 11 `INVALID_ENUM` e 1 `MISSING_REQUIRED_FIELD` combinado com identificador ausente resolvido por declaração explícita `ausente-na-fonte` já sustentada pelo próprio documento. Não houve YAML inválido, data inválida, chave duplicada, tipo errado, campo desconhecido ou decisão científica/editorial necessária.

Patch mínimo: inclusão de `responsavel_curadoria: Fabio Takwara`; mapeamento de tipos legados para a taxonomia vigente; inclusão de `identificador: ausente-na-fonte` quando o próprio arquivo informa `NOT_LOCATED_IN_DOCUMENT`.

Arquivos BAM-CHN-001 modificados: 0. Zenodo: 0. Limpeza não relacionada: 0.
