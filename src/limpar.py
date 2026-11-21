import re
from pathlib import Path
import pandas as pd

UFS = ["Rondônia", "Acre", "Amazonas", "Roraima", "Pará", "Amapá", "Tocantins",
       "Maranhão", "Piauí", "Ceará", "Rio Grande do Norte", "Paraíba",
       "Pernambuco", "Alagoas", "Sergipe", "Bahia", "Minas Gerais",
       "Espírito Santo", "Rio de Janeiro", "São Paulo", "Paraná",
       "Santa Catarina", "Rio Grande do Sul", "Mato Grosso do Sul",
       "Mato Grosso", "Goiás", "Distrito Federal"]
REGIOES = ["Brasil", "Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]
ALVO = UFS + REGIOES


def limpar_nome(x):
    return re.sub(r"\s*\(\d+\)\s*$", "", str(x)).strip()


def ler(caminho, primeira_linha):
    d = pd.read_excel(caminho, header=None).iloc[primeira_linha:].copy()
    d["lugar"] = d[0].map(limpar_nome)
    d = d[d["lugar"].isin(ALVO)]
    # o estado aparece antes das cidades de mesmo nome: mantém a 1a ocorrência
    d = d.drop_duplicates("lugar", keep="first")
    return d.set_index("lugar")


def num(s):
    return pd.to_numeric(s.replace("-", 0), errors="coerce")


nasc = ler("data/raw/01nascidosvivos_xls/Tabela 1.1.xls", 5)
obit = ler("data/raw/02obitos_xls/Tabela 2.1.xls", 7)

res = pd.DataFrame(index=nasc.index)
res["registros_nasc"] = num(nasc[1])
res["nasc_2024"] = num(nasc[12])
res["nasc_anos_anteriores"] = nasc[list(range(3, 12))].apply(num).sum(axis=1)
res["pct_registro_tardio"] = (res["nasc_anos_anteriores"] / res["registros_nasc"] * 100).round(2)
res["obitos_2024"] = num(obit[8])
res["saldo_vegetativo"] = res["nasc_2024"] - res["obitos_2024"]
res["nasc_por_obito"] = (res["nasc_2024"] / res["obitos_2024"]).round(2)

Path("data/processed").mkdir(parents=True, exist_ok=True)
res.to_csv("data/processed/uf_2024.csv", encoding="utf-8-sig")

print("Linhas:", res.shape[0], "(esperado: 33 = 27 estados + 5 regiões + Brasil)")
print()
print(res.loc[["Brasil", "Nordeste", "Paraíba"]].to_string())
print()
print("Maior % de registro tardio:")
print(res["pct_registro_tardio"].sort_values(ascending=False).head(8).to_string())
