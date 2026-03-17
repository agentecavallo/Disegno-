import streamlit as st
import random

# ── Configurazione pagina ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="🌈 Quiz dei Bambini",
    page_icon="🦁",
    layout="centered",
)

# ── CSS personalizzato ─────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');

  html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
  }

  .stApp {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 25%, #a1c4fd 75%, #c2e9fb 100%);
    min-height: 100vh;
  }

  .title-box {
    text-align: center;
    background: white;
    border-radius: 30px;
    padding: 20px 30px;
    margin-bottom: 24px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
  }
  .title-box h1 { font-size: 2.8rem; margin: 0; }
  .title-box p  { font-size: 1.2rem; color: #666; margin: 4px 0 0; }

  .domanda-box {
    background: white;
    border-radius: 24px;
    padding: 28px 32px;
    text-align: center;
    box-shadow: 0 6px 24px rgba(0,0,0,0.10);
    margin-bottom: 20px;
  }
  .domanda-box .emoji { font-size: 5rem; line-height: 1.2; }
  .domanda-box h2 { font-size: 1.7rem; color: #333; margin: 12px 0 0; }

  div.stButton > button {
    width: 100%;
    font-family: 'Nunito', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    border-radius: 18px;
    padding: 14px 10px;
    border: 3px solid transparent;
    transition: transform 0.15s, box-shadow 0.15s;
    cursor: pointer;
  }
  div.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
  }

  .score-box {
    background: white;
    border-radius: 20px;
    padding: 16px 24px;
    text-align: center;
    font-size: 1.3rem;
    font-weight: 700;
    color: #444;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    margin-bottom: 20px;
  }

  .feedback-ok  { font-size: 2rem; color: #2ecc71; font-weight: 900; text-align: center; }
  .feedback-no  { font-size: 2rem; color: #e74c3c; font-weight: 900; text-align: center; }
  .fine-box {
    background: white;
    border-radius: 28px;
    padding: 36px;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
  }
  .fine-box h2 { font-size: 2.2rem; }
  .fine-box p  { font-size: 1.3rem; color: #555; }
</style>
""", unsafe_allow_html=True)

# ── Domande ────────────────────────────────────────────────────────────────────
DOMANDE = [
    {"emoji": "🐶", "domanda": "Che animale è questo?",
     "risposta": "Cane", "opzioni": ["Gatto", "Cane", "Coniglio", "Cavallo"]},
    {"emoji": "🐱", "domanda": "Che animale è questo?",
     "risposta": "Gatto", "opzioni": ["Cane", "Volpe", "Gatto", "Orso"]},
    {"emoji": "🍎", "domanda": "Che frutto è questo?",
     "risposta": "Mela", "opzioni": ["Pera", "Banana", "Mela", "Arancia"]},
    {"emoji": "🍌", "domanda": "Che frutto è questo?",
     "risposta": "Banana", "opzioni": ["Mela", "Banana", "Uva", "Fragola"]},
    {"emoji": "🚗", "domanda": "Che veicolo è questo?",
     "risposta": "Macchina", "opzioni": ["Bici", "Treno", "Macchina", "Aereo"]},
    {"emoji": "✈️", "domanda": "Che veicolo è questo?",
     "risposta": "Aereo", "opzioni": ["Macchina", "Barca", "Aereo", "Moto"]},
    {"emoji": "🌞", "domanda": "Cosa vedi nel cielo di giorno?",
     "risposta": "Sole", "opzioni": ["Luna", "Stelle", "Sole", "Nuvola"]},
    {"emoji": "🌙", "domanda": "Cosa vedi nel cielo di notte?",
     "risposta": "Luna", "opzioni": ["Sole", "Luna", "Arcobaleno", "Fiore"]},
    {"emoji": "🌸", "domanda": "Cos'è questo?",
     "risposta": "Fiore", "opzioni": ["Albero", "Foglia", "Fiore", "Erba"]},
    {"emoji": "🐠", "domanda": "Che animale è questo?",
     "risposta": "Pesce", "opzioni": ["Balena", "Pesce", "Granchio", "Delfino"]},
    {"emoji": "🍕", "domanda": "Che cibo è questo?",
     "risposta": "Pizza", "opzioni": ["Pasta", "Pizza", "Panino", "Torta"]},
    {"emoji": "🎈", "domanda": "Cos'è questo?",
     "risposta": "Palloncino", "opzioni": ["Palla", "Palloncino", "Uovo", "Bolla"]},
    {"emoji": "🐘", "domanda": "Che animale è questo?",
     "risposta": "Elefante", "opzioni": ["Ippopotamo", "Rinoceronte", "Elefante", "Giraffa"]},
    {"emoji": "🌈", "domanda": "Cos'è questo?",
     "risposta": "Arcobaleno", "opzioni": ["Tramonto", "Arcobaleno", "Nuvola", "Stella"]},
    {"emoji": "🍓", "domanda": "Che frutto è questo?",
     "risposta": "Fragola", "opzioni": ["Ciliegia", "Fragola", "Lampone", "Pesca"]},
]

COLORI_BOTTONI = ["#FF6B6B", "#4ECDC4", "#FFE66D", "#A8E6CF"]

# ── Stato sessione ─────────────────────────────────────────────────────────────
def inizializza():
    domande_mischiate = random.sample(DOMANDE, len(DOMANDE))
    st.session_state.domande      = domande_mischiate
    st.session_state.indice       = 0
    st.session_state.punteggio    = 0
    st.session_state.feedback     = None   # None | "ok" | "no"
    st.session_state.risposta_data = None
    st.session_state.fine         = False

if "domande" not in st.session_state:
    inizializza()

TOTALE = len(st.session_state.domande)

# ── Intestazione ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="title-box">
  <h1>🌈 Quiz dei Bambini</h1>
  <p>Quante ne sai? Dimostralo! 🎉</p>
</div>
""", unsafe_allow_html=True)

# ── Fine gioco ─────────────────────────────────────────────────────────────────
if st.session_state.fine:
    p = st.session_state.punteggio
    if p == TOTALE:
        stella, msg = "🏆", "Sei un campione!"
    elif p >= TOTALE * 0.7:
        stella, msg = "⭐⭐⭐", "Bravissimo!"
    elif p >= TOTALE * 0.4:
        stella, msg = "⭐⭐", "Bravo, continua così!"
    else:
        stella, msg = "⭐", "Riprova, ce la fai!"

    st.markdown(f"""
    <div class="fine-box">
      <div style="font-size:4rem">{stella}</div>
      <h2>{msg}</h2>
      <p>Hai risposto bene a <strong>{p}</strong> domande su <strong>{TOTALE}</strong>!</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("🔄 Gioca ancora!", use_container_width=True):
        inizializza()
        st.rerun()
    st.stop()

# ── Domanda corrente ───────────────────────────────────────────────────────────
i  = st.session_state.indice
dq = st.session_state.domande[i]

# punteggio
st.markdown(f"""
<div class="score-box">
  ❓ Domanda {i+1} di {TOTALE} &nbsp;|&nbsp; ⭐ Punti: {st.session_state.punteggio}
</div>
""", unsafe_allow_html=True)

# card domanda
st.markdown(f"""
<div class="domanda-box">
  <div class="emoji">{dq['emoji']}</div>
  <h2>{dq['domanda']}</h2>
</div>
""", unsafe_allow_html=True)

# feedback
if st.session_state.feedback == "ok":
    st.markdown(f'<div class="feedback-ok">✅ Esatto! Bravissimo/a! 🎉</div>', unsafe_allow_html=True)
elif st.session_state.feedback == "no":
    st.markdown(f'<div class="feedback-no">❌ Ops! Era: {dq["risposta"]} {dq["emoji"]}</div>', unsafe_allow_html=True)

st.write("")

# opzioni
if st.session_state.feedback is None:
    opzioni = dq["opzioni"].copy()
    random.shuffle(opzioni)
    cols = st.columns(2)
    for idx, opz in enumerate(opzioni):
        col = cols[idx % 2]
        colore = COLORI_BOTTONI[idx]
        with col:
            # colora sfondo bottone via markdown trick
            st.markdown(f"""
            <style>
            div[data-testid="column"]:nth-child({(idx%2)+1}) div.stButton:nth-of-type(1) > button {{
              background-color: {colore}22;
              border-color: {colore};
              color: #222;
            }}
            </style>
            """, unsafe_allow_html=True)
            if st.button(opz, key=f"opz_{i}_{idx}"):
                st.session_state.risposta_data = opz
                if opz == dq["risposta"]:
                    st.session_state.feedback  = "ok"
                    st.session_state.punteggio += 1
                else:
                    st.session_state.feedback = "no"
                st.rerun()
else:
    # bottone avanti
    label = "➡️ Prossima domanda" if i < TOTALE - 1 else "🏁 Vedi il risultato!"
    if st.button(label, use_container_width=True):
        if i < TOTALE - 1:
            st.session_state.indice   += 1
            st.session_state.feedback  = None
            st.session_state.risposta_data = None
        else:
            st.session_state.fine = True
        st.rerun()
