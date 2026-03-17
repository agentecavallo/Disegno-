import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

# Impostazioni della pagina
st.set_page_config(page_title="ColoriAMO", layout="centered")
st.title("🎨 Area Creativa per i Bimbi")

# Dimensioni fisse del nostro foglio di disegno
LARGHEZZA_FOGLIO = 600
ALTEZZA_FOGLIO = 400

# --- MENÙ LATERALE (Tutto in Italiano) ---
st.sidebar.header("1. Il tuo Disegno")
file_caricato = st.sidebar.file_uploader("Carica un'immagine da colorare:", type=["png", "jpg", "jpeg"])

st.sidebar.header("2. Scegli lo Strumento")
tipo_pennello = st.sidebar.radio(
    "Con cosa vuoi disegnare?", 
    ["Matita ✏️", "Pennarello 🖊️", "Pennello Olio 🖌️"]
)

# Impostiamo la grandezza dei tratti in base allo strumento
spessori = {"Matita ✏️": 4, "Pennarello 🖊️": 12, "Pennello Olio 🖌️": 35}

# Colore rosso di default (#FF0000 è il codice del colore rosso)
colore_scelto = st.sidebar.color_picker("3. Scegli il colore:", value="#FF0000")

# --- GESTIONE DEL FOGLIO (Immagine o Bianco) ---
if file_caricato is not None:
    # Se hai caricato un'immagine, la apriamo
    immagine_sfondo = Image.open(file_caricato).convert("RGBA")
    # TRUCCO: La ridimensioniamo esattamente come il nostro foglio, così si vede tutta!
    immagine_sfondo = immagine_sfondo.resize((LARGHEZZA_FOGLIO, ALTEZZA_FOGLIO))
else:
    # Se non c'è nessuna immagine, creiamo un FOGLIO BIANCO di default
    immagine_sfondo = Image.new("RGBA", (LARGHEZZA_FOGLIO, ALTEZZA_FOGLIO), (255, 255, 255, 255))

st.write("✨ Disegna sul foglio bianco qui sotto, oppure carica un disegno dal menù a sinistra!")

# --- LA TELA DA DISEGNO (CANVAS) ---
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.0)",  # Colore trasparente per il riempimento
    stroke_width=spessori[tipo_pennello],
    stroke_color=colore_scelto,
    background_image=immagine_sfondo,
    height=ALTEZZA_FOGLIO,
    width=LARGHEZZA_FOGLIO,
    drawing_mode="freedraw",
    key="tela_disegno_bimbi", 
)
