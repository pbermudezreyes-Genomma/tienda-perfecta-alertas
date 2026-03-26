import streamlit as st

st.set_page_config(
    page_title="Agente de Alertas - Tienda Perfecta",
    page_icon="⚠️",
    layout="wide"
)

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

  .hero {
    background: linear-gradient(135deg, #1F3864 0%, #2E6DA4 100%);
    border-radius: 14px; padding: 40px 48px 32px; margin-bottom: 28px;
    box-shadow: 0 4px 24px rgba(31,56,100,0.18);
  }
  .hero h1 { color: #fff; font-size: 2rem; font-weight: 800; margin: 0 0 6px; letter-spacing: -0.5px; }
  .hero p  { color: #c8d8f0; font-size: 1rem; margin: 0; }
  .hero .badge {
    display: inline-block; background: rgba(255,255,255,0.15);
    color: #fff; border-radius: 20px; padding: 4px 14px;
    font-size: 0.78rem; font-weight: 600; margin-top: 14px; margin-right: 6px;
  }

  .section-title {
    background: #1F3864; color: #fff; border-radius: 8px;
    padding: 10px 18px; font-weight: 700; font-size: 0.95rem;
    margin: 28px 0 14px; letter-spacing: 0.4px;
  }
  .section-title.red { background: #7B2C2C; }

  .context-box {
    background: #FFF5F5; border-left: 5px solid #C00000;
    border-radius: 8px; padding: 16px 20px; color: #333;
    font-size: 0.93rem; line-height: 1.7;
  }
  .summary-box {
    background: #EEF4FF; border-left: 5px solid #1F3864;
    border-radius: 8px; padding: 16px 20px; color: #333;
    font-size: 0.93rem; line-height: 1.7;
  }

  .kpi-card {
    background: #fff; border-radius: 12px; padding: 22px 10px;
    text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    border-top: 4px solid #1F3864;
  }
  .kpi-val  { font-size: 2rem; font-weight: 800; color: #1F3864; }
  .kpi-lab  { font-size: 0.78rem; color: #666; margin-top: 4px; line-height: 1.4; }

  .feature-row {
    display: flex; align-items: flex-start; gap: 14px;
    background: #F7F9FF; border-radius: 10px;
    padding: 14px 16px; margin-bottom: 8px;
    border: 1px solid #E0E8F5;
  }
  .feature-num {
    background: #1F3864; color: #fff; border-radius: 50%;
    width: 30px; height: 30px; min-width: 30px;
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; font-size: 0.82rem;
  }
  .feature-title { font-weight: 700; color: #1F3864; font-size: 0.92rem; }
  .feature-desc  { font-size: 0.85rem; color: #555; margin-top: 2px; }

  .step-row {
    display: grid; grid-template-columns: 40px 1fr 130px 80px;
    gap: 0; align-items: center;
    padding: 10px 14px; border-bottom: 1px solid #E8EDF5;
    font-size: 0.87rem;
  }
  .step-row:last-child { border-bottom: none; }
  .step-row.header {
    background: #1F3864; color: #fff; font-weight: 700;
    border-radius: 8px 8px 0 0; font-size: 0.82rem;
  }
  .step-num {
    background: #2E4057; color: #fff; border-radius: 50%;
    width: 26px; height: 26px; display: flex;
    align-items: center; justify-content: center;
    font-weight: 700; font-size: 0.8rem;
  }
  .step-auto { color: #888; font-style: italic; }
  .step-time { color: #1F3864; font-weight: 600; text-align: right; }

  .timeline-row {
    display: grid; grid-template-columns: 80px 1fr 90px 110px;
    gap: 0; align-items: center;
    padding: 9px 14px; border-bottom: 1px solid #E8EDF5; font-size: 0.86rem;
  }
  .timeline-row:last-child { border-bottom: none; }
  .timeline-row.header {
    background: #1F3864; color: #fff; font-weight: 700;
    border-radius: 8px 8px 0 0; font-size: 0.82rem;
  }
  .badge-done   { background:#E3F5D8; color:#3A7D0A; border-radius:20px; padding:3px 10px; font-size:0.78rem; font-weight:600; }
  .badge-active { background:#FFF3C4; color:#8A6000; border-radius:20px; padding:3px 10px; font-size:0.78rem; font-weight:600; }
  .badge-plan   { background:#D9E8F5; color:#1F3864; border-radius:20px; padding:3px 10px; font-size:0.78rem; font-weight:600; }

  .deliverable {
    display: flex; align-items: flex-start; gap: 16px;
    background: #F7F9FF; border-radius: 10px;
    padding: 16px; margin-bottom: 8px; border: 1px solid #E0E8F5;
  }
  .del-num {
    background: #1F3864; color: #fff; border-radius: 8px;
    width: 36px; height: 36px; min-width: 36px;
    display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 1rem;
  }
  .del-title { font-weight: 700; color: #1F3864; font-size: 0.93rem; }
  .del-desc  { font-size: 0.84rem; color: #555; margin-top: 3px; line-height: 1.5; }

  .email-box {
    border: 1px solid #C8D4E8; border-radius: 10px; overflow: hidden;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  }
  .email-header {
    background: #1F3864; padding: 12px 20px;
    font-weight: 700; color: #fff; font-size: 0.88rem;
  }
  .email-meta {
    background: #EEF4FF; padding: 12px 20px;
    font-size: 0.85rem; border-bottom: 2px solid #1F3864;
  }
  .email-meta div { margin-bottom: 4px; }
  .email-meta span { font-weight: 700; color: #1F3864; margin-right: 8px; }
  .email-meta .asunto { color: #C00000; font-weight: 700; }
  .email-meta .adjunto { color: #0070C0; }
  .email-body {
    background: #FAFAFA; padding: 20px 24px;
    font-family: 'Courier New', monospace; font-size: 0.82rem;
    color: #333; line-height: 1.7; white-space: pre-wrap;
  }

  .benefit-row {
    display: flex; align-items: center; gap: 14px;
    padding: 12px 16px; border-bottom: 1px solid #EEF0F5;
    font-size: 0.88rem;
  }
  .benefit-row:last-child { border-bottom: none; }
  .benefit-tag {
    background: #D9E1F2; color: #1F3864; border-radius: 8px;
    padding: 4px 12px; font-weight: 700; font-size: 0.82rem;
    min-width: 130px; text-align: center;
  }

  .footer {
    text-align: center; color: #aaa; font-size: 0.78rem;
    margin-top: 40px; padding-top: 16px; border-top: 1px solid #E8EDF5;
  }
</style>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>⚠️ Agente de Alertas de Disponibilidad</h1>
  <p>Automatizacion Inteligente de Distribucion &nbsp;|&nbsp; Tienda Perfecta &nbsp;|&nbsp; Genomma Lab Internacional</p>
  <span class="badge">Trade Marketing Global</span>
  <span class="badge">Marzo 2026</span>
  <span class="badge">Lanzamiento: Cierre Mar 2026</span>
</div>
""", unsafe_allow_html=True)

# ── CONTEXTO ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title red">  CONTEXTO</div>', unsafe_allow_html=True)
st.markdown("""
<div class="context-box">
A pesar de los esfuerzos del equipo comercial, no se ha logrado una <strong>disciplina constante
de revision y accion</strong> sobre la data de Disponibilidad de <strong>Tienda Perfecta</strong>.
Dado que la disponibilidad es el <strong>fundamental #1 de la compania</strong> para el resultado de las marcas,
desarrollamos esta herramienta para <strong>operacionalizar el seguimiento</strong> de esta data estrategica
y mejorar el desempeno de marcas y canales en todos los mercados.
</div>
""", unsafe_allow_html=True)

# ── RESUMEN EJECUTIVO ─────────────────────────────────────────────────────────
st.markdown('<div class="section-title">  RESUMEN EJECUTIVO</div>', unsafe_allow_html=True)
st.markdown("""
<div class="summary-box">
El <strong>Agente de Alertas de Disponibilidad</strong> automatiza el monitoreo mensual de distribucion
en <strong>Tienda Perfecta</strong>. Detecta SKUs por debajo del <strong>75%</strong>, identifica al KAM responsable
y envia automaticamente un correo personalizado con Excel adjunto solicitando correccion en
<strong>48 horas</strong> y plan de mitigacion. Un proceso que antes tomaba horas ahora se completa
en <strong>menos de 2 minutos</strong>.
</div>
""", unsafe_allow_html=True)

# ── KPIs ─────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
k1, k2, k3, k4 = st.columns(4)
for col, val, lab in [
    (k1, "< 2 min", "Tiempo de ejecucion<br>total del proceso"),
    (k2, "75%",     "Umbral de alerta<br>de disponibilidad"),
    (k3, "48 h",    "Ventana de respuesta<br>exigida al KAM"),
    (k4, "100%",    "Correos personalizados<br>con adjunto"),
]:
    col.markdown(f"""
    <div class="kpi-card">
      <div class="kpi-val">{val}</div>
      <div class="kpi-lab">{lab}</div>
    </div>""", unsafe_allow_html=True)

# ── QUE HACE EL AGENTE ───────────────────────────────────────────────────────
st.markdown('<div class="section-title">  QUE HACE EL AGENTE</div>', unsafe_allow_html=True)
features = [
    ("1", "Procesamiento automatico",         "Lee el reporte mensual y filtra todos los SKUs con disponibilidad < 75%."),
    ("2", "Semaforo de criticidad",            "Clasifica cada SKU: CRITICO (0%-60%) o ALERTA (60%-78%)."),
    ("3", "Asignacion de responsable",         "Cruza cada alerta con el maestro Pais-Canal-Cadena e identifica al KAM y Team Leader."),
    ("4", "Correo personalizado por KAM",      "Redacta y envia un correo urgente con nombre, pais, SKUs afectados y solicitud de plan de accion en 48h."),
    ("5", "Excel adjunto con semaforo",        "Genera y adjunta un Excel con los SKUs criticos del KAM, coloreados por nivel de alerta."),
    ("6", "Envio masivo via Outlook",          "Usa la sesion activa de Outlook. Sin contrasenas adicionales. CC automatico al Team Leader."),
    ("7", "Reporte maestro de seguimiento",    "Consolida el estado de todos los envios: KAM, pais, SKUs afectados y prioridad."),
]
col_a, col_b = st.columns(2)
for i, (num, tit, desc) in enumerate(features):
    col = col_a if i % 2 == 0 else col_b
    col.markdown(f"""
    <div class="feature-row">
      <div class="feature-num">{num}</div>
      <div>
        <div class="feature-title">{tit}</div>
        <div class="feature-desc">{desc}</div>
      </div>
    </div>""", unsafe_allow_html=True)

# ── FLUJO DEL PROCESO ────────────────────────────────────────────────────────
st.markdown('<div class="section-title">  FLUJO DEL PROCESO (FIN DE MES)</div>', unsafe_allow_html=True)
steps = [
    ("1", "Actualizar reporte mensual con datos del cierre",            "Analista Trade", "5 min"),
    ("2", "Ejecutar el agente (un clic)",                               "Analista Trade", "< 1 min"),
    ("3", "Deteccion de alertas + generacion de correos y excels",      "Automatico",     "< 1 min"),
    ("4", "Envio masivo a KAMs via Outlook con adjunto",                "Automatico",     "< 1 min"),
    ("5", "Revision del reporte maestro de estado",                     "Trade Leader",   "5 min"),
    ("6", "Recepcion de planes de accion",                              "KAMs Pais",      "48 h"),
]
st.markdown("""
<div style="border:1px solid #E0E8F5; border-radius:10px; overflow:hidden;">
  <div class="step-row header">
    <div></div><div>ACCION</div><div>RESPONSABLE</div><div>TIEMPO</div>
  </div>""", unsafe_allow_html=True)
for num, accion, resp, tiempo in steps:
    is_auto = resp == "Automatico"
    resp_html = f'<span class="step-auto">{resp}</span>' if is_auto else resp
    bg = "#F0F4FF" if int(num) % 2 == 0 else "#FAFBFF"
    st.markdown(f"""
  <div class="step-row" style="background:{bg};">
    <div><div class="step-num">{num}</div></div>
    <div>{accion}</div>
    <div>{resp_html}</div>
    <div class="step-time">{tiempo}</div>
  </div>""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ── HOJA DE RUTA ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">  HOJA DE RUTA DE IMPLEMENTACION</div>', unsafe_allow_html=True)
timeline = [
    ("Fase 1", "Procesamiento de datos y deteccion de alertas",        "Mar 2026", "done"),
    ("Fase 2", "Redaccion automatica de correos personalizados",        "Mar 2026", "done"),
    ("Fase 3", "Generacion de Excel semaforo adjunto por KAM",         "Mar 2026", "done"),
    ("Fase 4", "Envio masivo via Outlook",                             "Mar 2026", "done"),
    ("Fase 5", "Lanzamiento oficial al cierre de marzo 2026",          "Mar 2026", "active"),
    ("Fase 6", "Automatizacion mensual programada (scheduler)",        "Abr 2026", "plan"),
]
badge = {"done": "✅ Completado", "active": "🔄 En curso", "plan": "📅 Planeado"}
badge_class = {"done": "badge-done", "active": "badge-active", "plan": "badge-plan"}
st.markdown("""
<div style="border:1px solid #E0E8F5; border-radius:10px; overflow:hidden;">
  <div class="timeline-row header">
    <div>FASE</div><div>ACTIVIDAD</div><div>FECHA</div><div>ESTADO</div>
  </div>""", unsafe_allow_html=True)
for fase, act, fecha, status in timeline:
    bg = "#F0F4FF" if timeline.index((fase,act,fecha,status)) % 2 == 0 else "#FAFBFF"
    st.markdown(f"""
  <div class="timeline-row" style="background:{bg};">
    <div style="font-weight:700;color:#1F3864;">{fase}</div>
    <div>{act}</div>
    <div style="color:#555;">{fecha}</div>
    <div><span class="{badge_class[status]}">{badge[status]}</span></div>
  </div>""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ── ENTREGABLES MENSUALES ────────────────────────────────────────────────────
st.markdown('<div class="section-title">  ENTREGABLES MENSUALES</div>', unsafe_allow_html=True)
deliverables = [
    ("01", "Excel Semaforo por KAM",
     "Archivo personalizado con los SKUs criticos del KAM, clasificados por nivel de alerta "
     "(CRITICO 0-60% / ALERTA 60-78%), distribucion actual y cadena afectada. Se adjunta automaticamente a cada correo."),
    ("02", "Correo de Alerta Personalizado",
     "Email urgente y profesional dirigido al KAM con copia al Team Leader. Incluye resumen ejecutivo "
     "(pais, canal, SKUs, distribucion promedio) y solicita correccion en 48h + plan de mitigacion."),
    ("03", "Reporte Maestro de Seguimiento",
     "Excel consolidado con el estado de todos los envios del mes: KAM, pais, SKUs afectados, "
     "nivel de prioridad y confirmacion de envio. Disponible para revision del VP y Trade Leaders."),
]
for num, tit, desc in deliverables:
    st.markdown(f"""
    <div class="deliverable">
      <div class="del-num">{num}</div>
      <div>
        <div class="del-title">{tit}</div>
        <div class="del-desc">{desc}</div>
      </div>
    </div>""", unsafe_allow_html=True)

# ── PREVIEW DEL CORREO ───────────────────────────────────────────────────────
st.markdown('<div class="section-title">  EJEMPLO DE CORREO DE ALERTA</div>', unsafe_allow_html=True)
cuerpo = """Estimada Maria,

La disponibilidad de los SKUs relacionados a continuacion quedo por debajo del 75% al cierre de mes. Requerimos tu intervencion para:

  1. Correccion Inmediata: Restablecer niveles de stock en punto de venta en las proximas 48 horas.

  2. Plan de Mitigacion: Si la baja es recurrente, enviar un breve plan de accion para evitar futuros quiebres en este canal.

RESUMEN EJECUTIVO
------------------------------------------------
  Pais:                  Mexico
  Canal:                 Cadenas Nacionales
  SKUs afectados:        8
  Cadenas involucradas:  3
  Distribucion promedio: 58.4%  (Meta: >= 75%)
------------------------------------------------

Encontraras el detalle completo con semaforo de criticidad en el archivo adjunto.

Quedamos atentos a tu respuesta.

Saludos cordiales,
Equipo Trade Marketing Global - Tienda Perfecta
Genomma Lab Internacional"""

st.markdown(f"""
<div class="email-box">
  <div class="email-header">📧 Vista previa del correo automatico</div>
  <div class="email-meta">
    <div><span>Para:</span> kam.responsable@genommalab.com</div>
    <div><span>CC:</span> teamleader@genommalab.com</div>
    <div><span>Asunto:</span> <span class="asunto">⚠️ ALERTA: Baja Distribucion Critica - Mexico | Cadenas Nacionales</span></div>
    <div><span>Adjunto:</span> <span class="adjunto">📎 SKUs_Criticos_Mexico_KAM.xlsx</span></div>
  </div>
  <div class="email-body">{cuerpo}</div>
</div>
""", unsafe_allow_html=True)

# ── BENEFICIOS ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">  BENEFICIOS CLAVE</div>', unsafe_allow_html=True)
benefits = [
    ("Eficiencia",       "De horas de trabajo manual a menos de 2 minutos por ciclo mensual."),
    ("Estandarizacion",  "Cada KAM recibe el mismo formato profesional con sus datos exactos."),
    ("Trazabilidad",     "El reporte maestro muestra de un vistazo quien tiene alertas activas."),
    ("Escalabilidad",    "Opera sobre cualquier pais, canal o SKU sin ajustes adicionales."),
    ("Accion rapida",    "Exige respuesta en 48h con plan concreto, reduciendo el tiempo de reaccion."),
]
st.markdown('<div style="border:1px solid #E0E8F5; border-radius:10px; overflow:hidden; background:#fff;">', unsafe_allow_html=True)
for tag, desc in benefits:
    st.markdown(f"""
    <div class="benefit-row">
      <div class="benefit-tag">{tag}</div>
      <div>{desc}</div>
    </div>""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  Confidencial · Uso Interno Genomma Lab Internacional · Trade Marketing Global - Tienda Perfecta · Marzo 2026
</div>
""", unsafe_allow_html=True)
