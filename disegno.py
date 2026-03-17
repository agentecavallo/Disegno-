import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.set_page_config(page_title="ColoriAMO", layout="centered")
st.title("🎨 Area Creativa per i Bimbi")

# 1. Scelta dello strumento
st.sidebar.header("Strumenti")
tool = st.sidebar.selectbox(
    "Cosa vuoi usare?", ("brush", "freedraw", "line", "rect")
)

# Simuliamo i pennelli cambiando lo spessore
pennello = st.sidebar.radio("Tipo di tratto:", ["Matita", "Pennarello", "Pennello Olio"])
spessori = {"Matita": 3, "Pennarello": 10, "Pennello Olio": 25}
stroke_width = spessori[pennello]

# 2. Scelta del colore
stroke_color = st.sidebar.color_picker("Scegli un colore:", "#FF0000")
bg_image = st.sidebar.file_uploader("Carica un disegno da colorare (PNG/JPG):", type=["png", "jpg"])

# 3. Il Canvas (La zona dove si disegna)
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Colore riempimento per forme
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=True,
    height=500,
    drawing_mode=tool,
    key="canvas",
)

st.write("✨ Carica un'immagine e usa la barra a sinistra per colorare!")
