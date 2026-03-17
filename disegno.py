import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.set_page_config(page_title="ColoriAMO", layout="centered")
st.title("🎨 Area Creativa")

# 1. Caricamento immagine
st.sidebar.header("1. Carica Disegno")
file = st.sidebar.file_uploader("Scegli un'immagine:", type=["png", "jpg", "jpeg"])

# 2. Configurazione Pennelli
st.sidebar.header("2. Strumenti")
tipo = st.sidebar.radio("Pennello:", ["Matita ✏️", "Pennarello 🖊️", "Pennello Olio 🖌️"])
pennelli = {"Matita ✏️": 4, "Pennarello 🖊️": 12, "Pennello Olio 🖌️": 35}
colore = st.sidebar.color_picker("Scegli Colore:", "#000000")

# --- IL TRUCCO PER RISOLVERE L'ERRORE ---
# Creiamo sempre un'immagine, così il Canvas non riceve mai "nulla"
if file is not None:
    img_da_mostrare = Image.open(file).convert("RGB")
else:
    # Se non c'è file, creiamo un foglio bianco 600x400
    img_da_mostrare = Image.new("RGB", (600, 400), (255, 255, 255))

# Visualizziamo il Canvas
# NOTA: ho cambiato la 'key' in 'canvas_v5' per resettare tutto
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=pennelli[tipo],
    stroke_color=colore,
    background_image=img_da_mostrare,
    height=400,
    width=600,
    drawing_mode="freedraw",
    key="canvas_v5", 
)

st.info("💡 Se non vedi l'immagine, caricala dal menu a sinistra!")
