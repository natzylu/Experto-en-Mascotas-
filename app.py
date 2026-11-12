import csv
from datetime import datetime
from pathlib import Path
import streamlit as st
from engine import recomendar

st.set_page_config(page_title="Experto en Mascotas", page_icon="🐾", layout="centered")
st.markdown("""<style>
.stApp {background: linear-gradient(180deg,#f4fbf8 0%,#ffffff 45%)}
.hero {padding:1.5rem;border-radius:18px;background:#0f766e;color:white;margin-bottom:1rem}
.resultado {padding:1.2rem;border-radius:16px;background:#ecfdf5;border:1px solid #6ee7b7}
.small {color:#475569;font-size:.92rem}
</style>""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>🐾 Experto en Mascotas</h1><p>Complete el formulario para recibir una recomendación compatible con su estilo de vida.</p></div>', unsafe_allow_html=True)

with st.form("consulta"):
    c1, c2 = st.columns(2)
    with c1:
        espacio = st.selectbox("Tamaño de la vivienda", ["Pequeño", "Mediano", "Grande"])
        tiempo = st.selectbox("Tiempo libre diario", ["Poco", "Medio", "Mucho"])
        presupuesto = st.selectbox("Presupuesto mensual", ["Bajo", "Medio", "Alto"])
        experiencia = st.selectbox("Experiencia con mascotas", ["Ninguna", "Algo", "Mucha"])
    with c2:
        actividad = st.selectbox("Nivel de actividad física", ["Baja", "Media", "Alta"])
        niños = st.selectbox("¿Hay niños pequeños en casa?", ["No", "Sí"])
        preferencia = st.radio("Tipo de mascota preferida", ["Mamíferos", "Peces", "Aves"])
    enviar = st.form_submit_button("Obtener recomendación", use_container_width=True, type="primary")

if enviar:
    hechos = {"espacio":espacio,"tiempo":tiempo,"presupuesto":presupuesto,"experiencia":experiencia,"actividad":actividad,"niños":niños,"preferencia":preferencia}
    recomendacion, reglas = recomendar(hechos)
    st.markdown(f'<div class="resultado"><h2>Recomendación: {recomendacion}</h2><p>Resultado basado en sus respuestas y las reglas del sistema experto.</p></div>', unsafe_allow_html=True)
    with st.expander("Ver explicación"):
        if reglas:
            for r in reglas:
                condiciones = ", ".join(f"{k}: {v}" for k, v in r["si"].items())
                st.write(f"**{r['id']}** · {condiciones}")
        else:
            st.write("Se aplicó una recomendación general según su preferencia y el espacio disponible.")
    ruta = Path("historial_mascotas.csv")
    nuevo = not ruta.exists()
    try:
        with ruta.open("a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if nuevo: w.writerow(["fecha", *hechos.keys(), "recomendacion", "reglas"])
            w.writerow([datetime.now().isoformat(timespec="seconds"), *hechos.values(), recomendacion, ",".join(r["id"] for r in reglas) or "RESPALDO"])
        st.success("Consulta guardada correctamente.")
    except OSError as e:
        st.warning(f"La recomendación se generó, pero no se pudo guardar el historial: {e}")

st.markdown('<p class="small">Esta herramienta ofrece una recomendación orientativa. Investigue las necesidades específicas del animal antes de adoptarlo.</p>', unsafe_allow_html=True)
