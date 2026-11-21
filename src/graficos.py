from pathlib import Path
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data/processed/uf_2024.csv", index_col="lugar", encoding="utf-8-sig")
regioes = ["Brasil", "Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]
ufs = df.drop(index=regioes)


def barras(coluna, titulo, eixo):
    d = ufs[coluna].sort_values()
    cores = ["#d1495b" if nome == "Paraíba" else "#2e6f95" for nome in d.index]
    fig = go.Figure(go.Bar(x=d.values, y=d.index, orientation="h", marker_color=cores))
    fig.add_vline(x=df.loc["Brasil", coluna], line_dash="dash",
                  annotation_text="Brasil", annotation_position="top")
    fig.update_layout(title=titulo, xaxis_title=eixo, height=800,
                      template="plotly_white", margin=dict(l=150))
    return fig


fig1 = barras("nasc_por_obito",
              "Nascimentos para cada óbito, por estado (2024)",
              "Nascimentos por óbito")
fig2 = barras("pct_registro_tardio",
              "Registros de nascimento feitos em 2024 de crianças nascidas em anos anteriores (%)",
              "% do total de registros")

html = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<title>Registro Civil 2024: Paraíba</title>
<style>body{{font-family:system-ui,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem}}</style>
</head><body>
<h1>Registro Civil 2024: onde a Paraíba se encaixa?</h1>
<p>Fonte: IBGE, Estatísticas do Registro Civil 2024. A Paraíba aparece em vermelho.</p>
{fig1.to_html(full_html=False, include_plotlyjs="cdn")}
{fig2.to_html(full_html=False, include_plotlyjs=False)}
<p><small>Limitação: dados de um único ano; o registro tardio não mede o sub-registro total.</small></p>
</body></html>"""

Path("docs").mkdir(exist_ok=True)
Path("docs/index.html").write_text(html, encoding="utf-8")
print("Página criada em docs/index.html")
