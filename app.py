
import streamlit as st
import pyperclip
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.markdown("""
<style>

/* Import Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

/* Animated Background */
@keyframes gradient{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* Main Container */
.block-container{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(18px);
    border-radius:20px;
    padding:2rem;
    box-shadow:0 8px 32px rgba(0,0,0,.35);
}

/* Title */
h1{
    color:white;
    text-align:center;
    font-weight:700;
    margin-bottom:10px;
}

/* Subtitle */
p{
    color:#f1f5f9;
}

/* Text Area */
textarea{
    background:rgba(255,255,255,.12)!important;
    color:white!important;
    border-radius:12px!important;
    border:1px solid rgba(255,255,255,.2)!important;
}

/* Input Box */
input{
    color:white!important;
}

/* Select Box */
.stSelectbox div[data-baseweb="select"]{
    background:rgba(255,255,255,.12);
    border-radius:12px;
}

/* Buttons */
.stButton>button{
    width:100%;
    background:linear-gradient(45deg,#06b6d4,#3b82f6);
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:18px;
    font-weight:600;
    transition:.3s;
}

.stButton>button:hover{
    transform:translateY(-3px);
    box-shadow:0 10px 20px rgba(0,0,0,.35);
}

/* Success Box */
.stSuccess{
    border-radius:12px;
}

/* Warning Box */
.stWarning{
    border-radius:12px;
}

/* Error Box */
.stError{
    border-radius:12px;
}

/* Footer */
.footer{
    text-align:center;
    color:white;
    margin-top:30px;
    opacity:.8;
    font-size:14px;
}

/* Scrollbar */
::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-thumb{
    background:#38bdf8;
    border-radius:20px;
}

::-webkit-scrollbar-track{
    background:#1e293b;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1>🌍 AI Language Translation Tool</h1>
<p style='text-align:center;font-size:18px;color:white'>
Translate text between 100+ languages instantly using AI.
</p>
""", unsafe_allow_html=True)

# st.title("🌍 AI Language Translation Tool")
st.write("Translate text into multiple languages using Google Translate AI.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar"
}

source = st.selectbox(
    "Source Language",
    list(languages.keys()),
    index=0
)

target = st.selectbox(
    "Target Language",
    list(languages.keys()),
    index=2
)

text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type something here..."
)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success("Translation Successful")

            st.text_area(
                "Translated Text",
                translated,
                height=180
            )

            if st.button("Copy Translation"):
                pyperclip.copy(translated)
                st.success("Copied to Clipboard!")

        except Exception as e:
            st.error(str(e))

st.markdown("""
<div class="footer">
Made with ❤️ using Python, Streamlit & Google Translate AI
</div>
""", unsafe_allow_html=True)