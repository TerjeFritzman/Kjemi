import streamlit as st

st.title("Tangen VGS Kjemi")

# Legg til mer funksjonalitet her etter behov
st.markdown(
    """
    <style>
    .escape-header {
        color: #E23131;
        font-size: 2.2em;
        font-weight: bold;
        margin-bottom: 0.5em;
        text-align: left;
    }
    .escape-instructions {
        color: #E2D931;
        font-size: 1.2em;
        margin-bottom: 1.5em;
        text-align: left;
    }
    .stTextInput > div > input {
        font-size: 1.1em;
        letter-spacing: 0.1em;
    }
    </style>
    <div class="escape-header">Først løs oppgaven!</div>
    <div class="escape-instructions">Deretter skriv inn passordet for å komme videre!</div>
    """,
    unsafe_allow_html=True
)

# Sett passordet her
KORREKT_PASSORD = "h20"

password = st.text_input("Skriv inn passordet her:", type="password")

if password:
    if password == KORREKT_PASSORD:
        st.success("🎉 Gratulerer! Du har løst oppgaven og funnet riktig passord!")
        st.balloons()
    else:
        st.error("Feil passord. Prøv igjen!")
