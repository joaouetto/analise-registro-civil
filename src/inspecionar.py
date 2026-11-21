import pandas as pd

arquivos = [
    "data/raw/01nascidosvivos_xls/Tabela 1.1.xls",
    "data/raw/02obitos_xls/Tabela 2.1.xls",
]

for arq in arquivos:
    planilha = pd.ExcelFile(arq)
    print("=" * 80)
    print(arq, "| abas:", planilha.sheet_names)
    for aba in planilha.sheet_names:
        d = planilha.parse(aba, header=None)
        print(f"\n--- aba '{aba}' | tamanho: {d.shape} ---")
        print(d.head(14).to_string(max_cols=14, max_colwidth=22))
