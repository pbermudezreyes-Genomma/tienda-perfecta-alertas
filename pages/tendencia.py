import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tendencia Trimestral - Tienda Perfecta", page_icon="📈", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.hero {
    background: linear-gradient(135deg, #1F3864 0%, #2E6DA4 100%);
    border-radius: 14px; padding: 32px 40px 24px; margin-bottom: 24px;
}
.hero h1 { color:#fff; font-size:1.8rem; font-weight:800; margin:0 0 6px; }
.hero p  { color:#c8d8f0; font-size:0.95rem; margin:0; }

.section-title {
    background:#1F3864; color:#fff; border-radius:8px;
    padding:9px 16px; font-weight:700; font-size:0.9rem;
    margin:24px 0 12px; letter-spacing:0.4px;
}

.kpi-card {
    background:#fff; border-radius:10px; padding:18px 10px;
    text-align:center; box-shadow:0 2px 10px rgba(0,0,0,0.07);
    border-top:4px solid #1F3864;
}
.kpi-val { font-size:1.8rem; font-weight:800; color:#1F3864; }
.kpi-lab { font-size:0.75rem; color:#666; margin-top:4px; line-height:1.4; }

.badge-red    { background:#FFE0E0; color:#C00000; border-radius:20px; padding:3px 10px; font-size:0.78rem; font-weight:700; }
.badge-yellow { background:#FFF3C4; color:#8A6000; border-radius:20px; padding:3px 10px; font-size:0.78rem; font-weight:700; }
.badge-green  { background:#E3F5D8; color:#3A7D0A; border-radius:20px; padding:3px 10px; font-size:0.78rem; font-weight:700; }

.sku-row {
    display:grid; grid-template-columns: 2fr 1fr 90px 90px 90px 110px;
    gap:0; align-items:center;
    padding:9px 14px; border-bottom:1px solid #EEF0F5; font-size:0.84rem;
}
.sku-row.header {
    background:#1F3864; color:#fff; font-weight:700;
    border-radius:8px 8px 0 0; font-size:0.8rem;
}

.bar-wrap { background:#E8EDF5; border-radius:4px; height:10px; width:100%; }
.bar-fill  { height:10px; border-radius:4px; }

.insight-box {
    border-radius:10px; padding:14px 16px; margin-bottom:8px;
    border-left:5px solid; font-size:0.87rem; line-height:1.6;
}
</style>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>📈 Reporte de Tendencia Trimestral</h1>
  <p>Recurrencia de alertas por SKU &nbsp;|&nbsp; Enero – Marzo 2026 &nbsp;|&nbsp; Tienda Perfecta · Genomma Lab</p>
</div>
""", unsafe_allow_html=True)

# ── MOCK DATA ─────────────────────────────────────────────────────────────────
skus = pd.DataFrame([
    # Producto, Pais, Canal, Ene, Feb, Mar, KAM
    ("SILKA MEDIC CREMA 60G",      "Mexico",   "Cadenas Nac.",  58, 54, 51, "Maria Lopez",    "sin_mejora"),
    ("SILKA MEDIC GEL 100G",       "Mexico",   "Cadenas Nac.",  62, 65, 61, "Maria Lopez",    "sin_mejora"),
    ("SILKA MEDIC SPRAY 150ML",    "Colombia", "Farmacias",     45, 52, 70, "Juan Perez",     "mejora"),
    ("GOICOECHEA CREMA 200G",      "Colombia", "Farmacias",     70, 68, 65, "Juan Perez",     "sin_mejora"),
    ("GOICOECHEA BODY MILK 400ML", "Peru",     "Supermercados", 55, 58, 72, "Ana Torres",     "mejora"),
    ("SILKA MEDIC CREMA 30G",      "Peru",     "Supermercados", 40, 43, 44, "Ana Torres",     "sin_mejora"),
    ("FERMODYL SHAMPOO 400ML",     "Chile",    "Cadenas Nac.",  68, 74, 78, "Carlos Reyes",   "resuelto"),
    ("SILKA MEDIC GEL 50G",        "Chile",    "Cadenas Nac.",  60, 63, 71, "Carlos Reyes",   "mejora"),
    ("GOICOECHEA CREMA 400G",      "Argentina","Farmacias",     52, 55, 57, "Laura Gutierrez","sin_mejora"),
    ("SILKA MEDIC CREMA 60G",      "Argentina","Farmacias",     48, 46, 44, "Laura Gutierrez","sin_mejora"),
    ("FERMODYL ACOND. 400ML",      "Ecuador",  "Supermercados", 65, 72, 76, "Pedro Salas",    "resuelto"),
    ("GOICOECHEA BODY OIL 200ML",  "Ecuador",  "Supermercados", 58, 60, 73, "Pedro Salas",    "mejora"),
], columns=["Producto","Pais","Canal","Enero","Febrero","Marzo","KAM","Estado"])

sin_mejora = len(skus[skus["Estado"] == "sin_mejora"])
mejora     = len(skus[skus["Estado"] == "mejora"])
resuelto   = len(skus[skus["Estado"] == "resuelto"])
total      = len(skus)
recurrentes = len(skus[skus[["Enero","Febrero","Marzo"]].apply(lambda r: all(v < 75 for v in r), axis=1)])

# ── KPIs ─────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
c1,c2,c3,c4,c5 = st.columns(5)
for col, val, lab, border in [
    (c1, total,       "SKUs monitoreados<br>en el trimestre",    "#1F3864"),
    (c2, recurrentes, "SKUs en alerta<br>los 3 meses",           "#C00000"),
    (c3, sin_mejora,  "Sin mejora<br>sostenida",                 "#E6A800"),
    (c4, mejora,      "Con mejora<br>parcial",                   "#2E6DA4"),
    (c5, resuelto,    "Resueltos<br>(superaron 75%)",            "#3A7D0A"),
]:
    col.markdown(f"""
    <div class="kpi-card" style="border-top-color:{border};">
      <div class="kpi-val" style="color:{border};">{val}</div>
      <div class="kpi-lab">{lab}</div>
    </div>""", unsafe_allow_html=True)

# ── FILTROS ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">  DETALLE POR SKU — EVOLUCION MENSUAL</div>', unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns([1,1,1])
with col_f1:
    pais_sel = st.selectbox("Pais", ["Todos"] + sorted(skus["Pais"].unique().tolist()))
with col_f2:
    estado_sel = st.selectbox("Estado", ["Todos", "Sin mejora 🔴", "Mejora parcial 🟡", "Resuelto 🟢"])
with col_f3:
    kam_sel = st.selectbox("KAM", ["Todos"] + sorted(skus["KAM"].unique().tolist()))

df = skus.copy()
if pais_sel   != "Todos": df = df[df["Pais"] == pais_sel]
if kam_sel    != "Todos": df = df[df["KAM"]  == kam_sel]
if estado_sel == "Sin mejora 🔴":    df = df[df["Estado"] == "sin_mejora"]
elif estado_sel == "Mejora parcial 🟡": df = df[df["Estado"] == "mejora"]
elif estado_sel == "Resuelto 🟢":    df = df[df["Estado"] == "resuelto"]

# ── TABLA SKUs ────────────────────────────────────────────────────────────────
badge_map = {
    "sin_mejora": '<span class="badge-red">🔴 Sin mejora</span>',
    "mejora":     '<span class="badge-yellow">🟡 Mejora parcial</span>',
    "resuelto":   '<span class="badge-green">🟢 Resuelto</span>',
}

def barra(val, meta=75):
    pct = min(val, 100)
    color = "#C00000" if val <= 60 else "#E6A800" if val < 75 else "#3A7D0A"
    return f"""
    <div class="bar-wrap">
      <div class="bar-fill" style="width:{pct}%;background:{color};"></div>
    </div>
    <span style="font-size:10px;color:#666;">{val}%</span>"""

st.markdown("""
<div style="border:1px solid #E0E8F5;border-radius:10px;overflow:hidden;">
  <div class="sku-row header">
    <div>Producto</div><div>Pais / Canal</div>
    <div style="text-align:center;">Enero</div>
    <div style="text-align:center;">Febrero</div>
    <div style="text-align:center;">Marzo</div>
    <div style="text-align:center;">Estado</div>
  </div>""", unsafe_allow_html=True)

for _, row in df.iterrows():
    bg = "#FFF8F8" if row["Estado"] == "sin_mejora" else "#FFFDF0" if row["Estado"] == "mejora" else "#F5FFF0"
    st.markdown(f"""
  <div class="sku-row" style="background:{bg};">
    <div style="font-weight:600;color:#1F3864;font-size:0.82rem;">{row['Producto']}<br>
      <span style="font-weight:400;color:#888;font-size:0.75rem;">KAM: {row['KAM']}</span>
    </div>
    <div style="font-size:0.8rem;color:#555;">{row['Pais']}<br><span style="color:#888;">{row['Canal']}</span></div>
    <div>{barra(row['Enero'])}</div>
    <div>{barra(row['Febrero'])}</div>
    <div>{barra(row['Marzo'])}</div>
    <div style="text-align:center;">{badge_map[row['Estado']]}</div>
  </div>""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── INSIGHTS ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">  INSIGHTS DEL TRIMESTRE</div>', unsafe_allow_html=True)

sin_df = skus[skus["Estado"] == "sin_mejora"]
pais_critico = sin_df.groupby("Pais").size().idxmax() if not sin_df.empty else "—"
kam_critico  = sin_df.groupby("KAM").size().idxmax()  if not sin_df.empty else "—"
n_sin        = len(sin_df)

insights = [
    ("#FFE8E8", "#C00000",
     f"&#128308; <strong>{n_sin} SKUs sin mejora sostenida</strong> durante los 3 meses del trimestre. "
     f"El pais con mayor recurrencia es <strong>{pais_critico}</strong>. "
     f"Se recomienda escalar con el Country Manager y exigir plan estructural."),
    ("#FFFBE6", "#E6A800",
     f"&#129473; <strong>{mejora} SKUs muestran mejora parcial</strong> pero aun no alcanzan el 75%. "
     f"Requieren seguimiento activo en el proximo mes para consolidar la recuperacion."),
    ("#E8F5E3", "#3A7D0A",
     f"&#9989; <strong>{resuelto} SKUs fueron resueltos</strong> y superaron el umbral del 75%. "
     f"Buenas practicas identificadas para replicar en otros paises y canales."),
    ("#EEF4FF", "#1F3864",
     f"&#128204; <strong>KAM con mayor recurrencia de alertas: {kam_critico}.</strong> "
     f"Se recomienda revisar capacidad operativa y alineacion con el equipo de operaciones."),
]

for bg, border, text in insights:
    st.markdown(f"""
    <div class="insight-box" style="background:{bg};border-color:{border};">
      <span style="color:{border};">{text}</span>
    </div>""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;color:#aaa;font-size:0.75rem;margin-top:32px;
            padding-top:14px;border-top:1px solid #E8EDF5;">
  Confidencial · Uso Interno · Trade Marketing Global - Tienda Perfecta · Genomma Lab Internacional
</div>""", unsafe_allow_html=True)
