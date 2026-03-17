import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

# Impostazioni della pagina
st.set_page_config(page_title="ColoriAMO", layout="centered")
st.title("🎨 Area Creativa")

# Dimensioni perfette per i telefoni (più stretto e un po' più alto)
LARGHEZZA_FOGLIO = 350
ALTEZZA_FOGLIO = 450

# --- MENÙ LATERALE ---
st.sidebar.header("1. Il tuo Disegno")
file_caricato = st.sidebar.file_uploader("Carica un'immagine:", type=["png", "jpg", "jpeg"])

st.sidebar.header("2. Scegli lo Strumento")
tipo_pennello = st.sidebar.radio(
    "Strumento:", 
    ["Matita ✏️", "Pennarello 🖊️", "Pennello Olio 🖌️"]
)

spessori = {"Matita ✏️": 4, "Pennarello 🖊️": 12, "Pennello Olio 🖌️": 30}
colore_scelto = st.sidebar.color_picker("3. Scegli il colore:", value="#FF0000")

# --- GESTIONE IMMAGINE ---
immagine_sfondo = None
if file_caricato is not None:
    # Usiamo il formato RGBA che è quello che il Canvas "digerisce" meglio
    immagine_sfondo = Image.open(file_caricato).convert("RGBA")
    immagine_sfondo = immagine_sfondo.resize((LARGHEZZA_FOGLIO, ALTEZZA_FOGLIO))

st.write("✨ Chiudi il menù a sinistra (cliccando la freccetta < in alto) per colorare!")

# --- LA TELA DA DISEGNO ---
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.0)",
    stroke_width=spessori[tipo_pennello],
    stroke_color=colore_scelto,
    background_color="#FFFFFF",  # <-- TRUCCO: Questo forza sempre il foglio ad essere BIANCO
    background_image=immagine_sfondo,
    height=ALTEZZA_FOGLIO,
    width=LARGHEZZA_FOGLIO,
    drawing_mode="freedraw",
    key="tela_definitiva", 
)
