import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.set_page_config(page_title="ColoriAMO", layout="centered")
st.title("🎨 Area Creativa per i Bimbi")

# --- BARRA LATERALE ---
st.sidebar.header("Impostazioni")
bg_image = st.sidebar.file_uploader("1. Carica il disegno:", type=["png", "jpg", "jpeg"])

# Scelta del tipo di "pennello"
pennello = st.sidebar.radio("2. Tipo di tratto:", ["Matita", "Pennarello", "Pennello Olio"])
spessori = {"Matita": 4, "Pennarello": 12, "Pennello Olio": 35}
stroke_width = spessori[pennello]

# Scelta del colore
stroke_color = st.sidebar.color_picker("3. Scegli un colore:", "#FF0000")

# --- GESTIONE IMMAGINE ---
bg_img_obj = None
if bg_image is not None:
    # Apriamo l'immagine e forziamo il formato RGB per evitare errori
    bg_img_obj = Image.open(bg_image).convert("RGB")
    # Ridimensioniamo per farla stare bene nello schermo del telefono
    bg_img_obj = bg_img_obj.resize((400, 400))

# --- IL CANVAS (L'AREA DISEGNO) ---
# Se non c'è immagine, mostriamo un canvas bianco standard
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_image=bg_img_obj, 
    background_color="#FFFFFF",
    height=400,
    width=400,
    drawing_mode="freedraw",
    key="canvas_principale",
)

if bg_image is None:
    st.info("👈 Carica un'immagine dalla barra laterale per iniziare a colorare!")
else:
    st.success("Buon divertimento! Usa le dita o il mouse per colorare.")
