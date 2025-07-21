import streamlit as st
with open("background_image_skull.b64.txt") as f:
    b64_string = f.read()

st.markdown(
    f"""
    <style>
    body, .stApp {{
        background-color: #000000 !important;
        background-image: url('data:image/png;base64,{b64_string}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .escape-header, .escape-instructions {{
        background: rgba(0,0,0,0.7);
        border-radius: 16px;
        padding: 32px 40px;
        margin-bottom: 1em;
        color: #fff;
        font-size: 2em;
        font-family: 'Fira Mono', 'Consolas', 'Menlo', 'Monaco', 'Courier New', monospace;
        text-align: left;
        box-shadow: 0 4px 24px rgba(0,0,0,0.6);
    }}
    .escape-instructions {{
        font-size: 1.5em;
        color: #E2D931;
        margin-bottom: 2em;
    }}
    .stTextInput > div > input {{
        font-size: 4em !important;
        height: 120px !important;
        padding: 28px 36px !important;
        letter-spacing: 0.1em;
        font-family: 'Fira Mono', 'Consolas', 'Menlo', 'Monaco', 'Courier New', monospace;
        background: rgba(0,0,0,0.7);
        color: #fff;
        border: 2px solid #E2D931;
        border-radius: 12px;
    }}
    </style>
    <div class="escape-header">Tangen VGS</div>
    <div class="escape-instructions">Skriv inn passordet for å komme videre!</div>
    """,
    unsafe_allow_html=True
)

# Sett passordet her
KORREKT_PASSORD = "vann"

password = st.text_input("Skriv inn passordet her:", type="password")

if password:
    if password == KORREKT_PASSORD:
        st.success("🎉 Gratulerer! Du har løst oppgaven og funnet riktig passord!")
        st.balloons()
    else:
        st.error("Feil passord. Prøv igjen!")
