import streamlit as st
import random

# ── Configurazione pagina ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="🎨 Impara i Colori!",
    page_icon="🎨",
    layout="centered",
)

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;800&display=swap');

  html, body, [class*="css"] {
    font-family: 'Baloo 2', cursive;
  }

  .stApp {
    background: #1a1a2e;
    min-height: 100vh;
  }

  .title-box {
    text-align: center;
    padding: 18px 20px 10px;
    margin-bottom: 10px;
  }
  .title-box h1 {
    font-size: 3rem;
    margin: 0;
    color: white;
    text-shadow: 0 0 20px rgba(255,255,255,0.4);
  }
  .title-box p {
    font-size: 1.2rem;
    color: #ccc;
    margin: 4px 0 0;
  }

  .color-stage {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 10px auto 18px;
  }

  .color-circle {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    margin: 0 auto;
    box-shadow: 0 0 60px rgba(255,255,255,0.25), 0 0 120px rgba(255,255,255,0.1);
    border: 6px solid rgba(255,255,255,0.2);
    transition: transform 0.3s;
  }

  .domanda-text {
    text-align: center;
    font-size: 1.6rem;
    font-weight: 600;
    color: white;
    margin: 16px 0 10px;
  }

  .score-bar {
    background: rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 10px 24px;
    text-align: center;
    font-size: 1.2rem;
    font-weight: 600;
    color: white;
    margin-bottom: 14px;
    backdrop-filter: blur(6px);
  }

  div.stButton > button {
    width: 100%;
    font-family: 'Baloo 2', cursive;
    font-size: 1.3rem;
    font-weight: 800;
    border-radius: 20px;
    padding: 16px 10px;
    border: none;
    color: white;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    transition: transform 0.15s, box-shadow 0.15s;
    cursor: pointer;
    letter-spacing: 0.5px;
  }
  div.stButton > button:hover {
    transform: translateY(-4px) scale(1.03);
    box-shadow: 0 12px 28px rgba(0,0,0,0.4);
  }

  .feedback-ok {
    text-align: center;
    font-size: 2.2rem;
    font-weight: 800;
    color: #2ecc71;
    margin: 8px 0;
    text-shadow: 0 0 20px rgba(46,204,113,0.5);
  }
  .feedback-no {
    text-align: center;
    font-size: 2.2rem;
    font-weight: 800;
    color: #e74c3c;
    margin: 8px 0;
    text-shadow: 0 0 20px rgba(231,76,60,0.5);
  }

  .fine-box {
    background: rgba(255,255,255,0.08);
    border-radius: 28px;
    padding: 36px;
    text-align: center;
    border: 2px solid rgba(255,255,255,0.15);
    backdrop-filter: blur(10px);
  }
  .fine-box h2 { font-size: 2.4rem; color: white; }
  .fine-box p  { font-size: 1.3rem; color: #ccc; }
</style>
""", unsafe_allow_html=True)

# ── Dati colori ────────────────────────────────────────────────────────────────
COLORI = [
    {"nome": "Rosso",    "hex": "#FF3B3B", "emoji": "🍎", "btn": "#FF3B3B"},
    {"nome": "Blu",      "hex": "#3B8BFF", "emoji": "🌊", "btn": "#3B8BFF"},
    {"nome": "Giallo",   "hex": "#FFD93D", "emoji": "🌟", "btn": "#E8C400"},
    {"nome": "Verde",    "hex": "#3BCC6E", "emoji": "🌿", "btn": "#3BCC6E"},
    {"nome": "Arancione","hex": "#FF8C3B", "emoji": "🍊", "btn": "#FF8C3B"},
    {"nome": "Viola",    "hex": "#9B59FF", "emoji": "🍇", "btn": "#9B59FF"},
    {"nome": "Rosa",     "hex": "#FF6EC7", "emoji": "🌸", "btn": "#FF6EC7"},
    {"nome": "Azzurro",  "hex": "#3BE8FF", "emoji": "🦋", "btn": "#00BFCF"},
    {"nome": "Marrone",  "hex": "#A0522D", "emoji": "🐻", "btn": "#A0522D"},
    {"nome": "Bianco",   "hex": "#F0F0F0", "emoji": "☁️",  "btn": "#999999"},
]

TOTALE_ROUND = 10

def genera_domanda():
    colore_giusto = random.choice(COLORI)
    distrattori   = random.sample([c for c in COLORI if c["nome"] != colore_giusto["nome"]], 3)
    opzioni       = [colore_giusto] + distrattori
    random.shuffle(opzioni)
    return colore_giusto, opzioni

def inizializza():
    st.session_state.round       = 0
    st.session_state.punteggio   = 0
    st.session_state.feedback    = None
    st.session_state.fine        = False
    giusto, opzioni = genera_domanda()
    st.session_state.colore_giusto = giusto
    st.session_state.opzioni       = opzioni

if "round" not in st.session_state:
    inizializza()

# ── Intestazione ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="title-box">
  <h1>🎨 Impara i Colori!</h1>
  <p>Tocca il nome del colore giusto! 🌈</p>
</div>
""", unsafe_allow_html=True)

# ── Fine gioco ─────────────────────────────────────────────────────────────────
if st.session_state.fine:
    p = st.session_state.punteggio
    if p == TOTALE_ROUND:
        premio, msg = "🏆🌈", "Perfetto! Conosci tutti i colori!"
    elif p >= 7:
        premio, msg = "⭐⭐⭐", "Bravissimo/a! Quasi perfetto!"
    elif p >= 4:
        premio, msg = "⭐⭐", "Bravo/a! Continua a colorare!"
    else:
        premio, msg = "⭐", "Riprova, imparerai presto!"

    st.markdown(f"""
    <div class="fine-box">
      <div style="font-size:4.5rem; margin-bottom:10px">{premio}</div>
      <h2>{msg}</h2>
      <p>Hai indovinato <strong style="color:white">{p}</strong> colori su <strong style="color:white">{TOTALE_ROUND}</strong>! 🎉</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("🔄 Gioca ancora!", use_container_width=True):
        inizializza()
        st.rerun()
    st.stop()

# ── Score bar ──────────────────────────────────────────────────────────────────
r = st.session_state.round
p = st.session_state.punteggio
st.markdown(f"""
<div class="score-bar">
  🎨 Giro {r + 1} di {TOTALE_ROUND} &nbsp;|&nbsp; ⭐ Punti: {p}
</div>
""", unsafe_allow_html=True)

# ── Pallino colorato ───────────────────────────────────────────────────────────
colore = st.session_state.colore_giusto
st.markdown(f"""
<div class="color-stage">
  <div class="color-circle" style="background:{colore['hex']};"></div>
</div>
<div class="domanda-text">Che colore è questo? {colore['emoji']}</div>
""", unsafe_allow_html=True)

# ── Feedback ───────────────────────────────────────────────────────────────────
if st.session_state.feedback == "ok":
    st.markdown(f'<div class="feedback-ok">✅ Sì! È {colore["nome"]}! Bravissimo/a! 🎉</div>', unsafe_allow_html=True)
elif st.session_state.feedback == "no":
    st.markdown(f'<div class="feedback-no">❌ Era {colore["nome"]} {colore["emoji"]} — riprova!</div>', unsafe_allow_html=True)

st.write("")

# ── Bottoni risposta ───────────────────────────────────────────────────────────
if st.session_state.feedback is None:
    opzioni = st.session_state.opzioni
    col1, col2 = st.columns(2)
    for idx, opz in enumerate(opzioni):
        col = col1 if idx % 2 == 0 else col2
        with col:
            st.markdown(f"""
            <style>
            section[data-testid="column"]:nth-of-type({(idx%2)+1}) > div:nth-of-type({idx//2 + 1}) div.stButton > button {{
              background: {opz['btn']};
            }}
            </style>
            """, unsafe_allow_html=True)
            if st.button(opz["nome"], key=f"btn_{r}_{idx}"):
                if opz["nome"] == colore["nome"]:
                    st.session_state.feedback  = "ok"
                    st.session_state.punteggio += 1
                else:
                    st.session_state.feedback = "no"
                st.rerun()
else:
    label = "➡️ Prossimo colore!" if r < TOTALE_ROUND - 1 else "🏁 Vedi il risultato!"
    if st.button(label, use_container_width=True):
        if r < TOTALE_ROUND - 1:
            st.session_state.round   += 1
            st.session_state.feedback = None
            giusto, opzioni = genera_domanda()
            st.session_state.colore_giusto = giusto
            st.session_state.opzioni       = opzioni
        else:
            st.session_state.fine = True
        st.rerun()
