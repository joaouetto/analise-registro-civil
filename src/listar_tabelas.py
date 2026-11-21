from pathlib import Path
import pandas as pd

raiz = Path("data/raw")

for arq in sorted(raiz.glob("*/*.xls")):
    try:
        bruto = pd.read_excel(arq, header=None, nrows=10)
        textos = [str(x) for x in bruto.stack().dropna() if isinstance(x, str)]
        titulo = textos[0][:160] if textos else "(sem texto)"
    except Exception as erro:
        titulo = f"ERRO: {erro}"
    print(f"{arq.parent.name}/{arq.name}: {titulo}")