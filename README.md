# Registro Civil 2024: a Paraíba registra mais nascimentos do que óbitos?

## Pergunta
Em 2024, a Paraíba registrou mais nascimentos do que óbitos? E qual parte dos registros de nascimento foi tardia (crianças nascidas em anos anteriores), em comparação com o Nordeste e o Brasil?

## Resultado
| | Nascimentos 2024 | Óbitos 2024 | Saldo | Nascimentos por óbito | Registro tardio |
|---|---|---|---|---|---|
| Paraíba | 48.591 | 29.468 | +19.123 | 1,65 | 1,88% |
| Nordeste | 659.017 | 370.144 | +288.873 | 1,78 | 1,93% |
| Brasil | 2.370.945 | 1.490.857 | +880.088 | 1,59 | 2,07% |

- A Paraíba registrou 1,65 nascimento para cada óbito, acima da média do Brasil (1,59) e abaixo da do Nordeste (1,78).
- O registro tardio na Paraíba (1,88%) é parecido com o do Brasil. Os maiores percentuais estão no Norte, como Amazonas (17,95%) e Roraima (13,26%).

## Gráficos interativos
Página ao vivo: https://SEU-USUARIO.github.io/analise-registro-civil/

## Como foi feito
- Python (pandas) para ler e limpar as planilhas do IBGE
- Plotly para os gráficos, publicados em uma página HTML
- Seleção de 27 estados, 5 regiões e o Brasil a partir de tabelas que misturam estados, regiões metropolitanas e municípios

## Fonte dos dados
IBGE, Estatísticas do Registro Civil 2024: Tabela 1.1 (nascidos vivos por ano de nascimento, segundo o lugar de residência da mãe) e Tabela 2.1 (óbitos por ano de ocorrência, segundo o lugar de residência do falecido).

## Limitações
- Os dados cobrem um único ano (2024); o projeto não mostra evolução ao longo do tempo.
- O registro tardio mede só os nascimentos de anos anteriores registrados em 2024. Não é o sub-registro total.
- O IBGE indica que o sub-registro tende a ser maior no Norte e no Nordeste, o que pode afetar os números.
- Uso apenas de estatísticas agregadas; nenhum dado pessoal.

## Como rodar
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/limpar.py
python src/graficos.py
