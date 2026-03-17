import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.set_page_config(page_title="ColoriAMO", layout="centered")
st.title("🎨 Area Creativa per i Bimbi")

# --- BARRA LATERALE ---
st.sidebar.header("Configurazione")

# 1. Caricamento immagine (fondamentale farlo prima del canvas)
bg_image = st.sidebar.file_uploader("1. Carica il disegno da colorare:", type=["png", "jpg", "jpeg"])

# Gestione dell'immagine
bg_img_obj = None
if bg_image:
    bg_img_obj = Image.open(bg_image)
    # Opzionale: ridimensiona l'immagine per farla stare bene nel canvas
    bg_img_obj = bg_img_obj.resize((600, 400))

# 2. Scelta dello strumento
tool = st.sidebar.selectbox("2. Cosa vuoi usare?", ("freedraw", "line", "rect", "circle", "transform"))

# 3. Scelta del "Pennello"
pennello = st.sidebar.radio("3. Tipo di tratto:", ["Matita", "Pennarello", "Pennello Olio"])
spessori = {"Matita": 3, "Pennarello": 12, "Pennello Olio": 30}
stroke_width = spessori[pennello]

# 4. Scelta del colore
stroke_color = st.sidebar.color_picker("4. Scegli un colore:", "#FF0000")

# --- AREA DISEGNO (CANVAS) ---

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # trasparenza per le forme piene
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_image=bg_img_obj, # Qui ora è sicuro, se è None non crasha
    height=400,
    width=600,
    drawing_mode=tool,
    key="canvas",
)

st.info("💡 Consiglio: Carica un'immagine dalla barra a sinistra e inizia a dipingere!")
