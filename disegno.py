import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np

st.set_page_config(page_title="ColoriAMO", layout="centered")
st.title("🎨 Area Creativa per i Bimbi")

# 1. Caricamento file nella barra laterale
st.sidebar.header("1. Carica Disegno")
bg_image = st.sidebar.file_uploader("Scegli un'immagine da colorare:", type=["png", "jpg", "jpeg"])

# 2. Configurazione Pennelli
st.sidebar.header("2. Strumenti")
pennello = st.sidebar.radio("Tipo di tratto:", ["Matita", "Pennarello", "Pennello Olio"])
spessori = {"Matita": 3, "Pennarello": 12, "Pennello Olio": 30}
stroke_width = spessori[pennello]
stroke_color = st.sidebar.color_picker("Scegli un colore:", "#FF0000")

# --- LOGICA DI PROTEZIONE ---
# Se l'utente ha caricato un'immagine, la usiamo. 
# Se NON l'ha caricata, creiamo uno sfondo bianco vuoto per non far crashare l'app.
if bg_image:
    img = Image.open(bg_image)
else:
    # Crea un'immagine bianca 600x400 se non c'è upload
    img = Image.new('RGB', (600, 400), color = 'white')

# Mostriamo il Canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_image=img, # Ora 'img' esiste sempre!
    height=400,
    width=600,
    drawing_mode="freedraw",
    key="canvas",
)

st.write("🖌️ Disegna sopra l'immagine bianca o carica un tuo disegno!")
