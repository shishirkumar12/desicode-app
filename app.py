import streamlit as st
from desicode_interpreter import run_desicode

# Set page config
st.set_page_config(page_title="DesiCode 🧠", page_icon="🌶️", layout="wide")

# Custom CSS for color theme
st.markdown("""
    <style>
        body {
            background-color: #fff8f0;
        }
        .stApp {
            background-color: #fff8f0;
            font-family: 'Segoe UI', sans-serif;
        }
        .block-container {
            padding: 2rem;
            background-color: #fff8f0;
        }
        h1 {
            color: #d62828;
        }
        .stTextArea textarea {
            background-color: #fff;
            color: #000;
            font-size: 16px;
            border-radius: 8px;
        }
        .stCodeBlock pre {
            background-color: #1e1e1e;
            color: #f8f8f2;
            font-family: 'Courier New', monospace;
            padding: 1rem;
            border-radius: 10px;
        }
        .stButton button {
            background-color: #f77f00;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
        }
        .stButton button:hover {
            background-color: #d62828;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("""
    <h1 style='text-align: center; font-size: 50px;'>🌶️ DesiCode – Desi Style Coding Language</h1>
    <p style='text-align: center;'>Apni bhaasha mein coding karo, mazaak-mazaak mein programming seekho! 🇮🇳</p>
""", unsafe_allow_html=True)

st.divider()

# Layout columns
left, right = st.columns([2, 1])

# Example programs
examples = {
    "👋 Namaste Duniya": 'bol "Namaste Duniya!"',
    "📦 Naam Print": 'rakh naam = "Shishir"\nbol "Mera naam hai:"\nbol naam',
    "🔁 Repeat": 'repeat 3 bol "Coding is fun!"',
    "➕ Math": 'rakh a = 10\nrakh b = 5\nrakh total jod a b\nbol total',
    "🤔 Condition": 'rakh naam = "Shishir"\nagar naam barabar "Shishir" toh bol "Sahi pakde hain!"',
    "🧾 Multiline": 'bol "Line 1\\nLine 2\\nLine 3"'
}

# Left side: Code input
with left:
    st.subheader("✍️ Likho apna DesiCode")
    example_choice = st.selectbox("📂 Choose Example Code:", list(examples.keys()))
    default_code = examples[example_choice]
    user_code = st.text_area("DesiCode Editor:", value=default_code, height=300)
    user_code = user_code.encode('utf-8').decode('unicode_escape')
    run = st.button("🔥 Run Code", use_container_width=True)

# Right side: Output display
with right:
    st.subheader("🖨️ Output Console")
    if run:
        result = run_desicode(user_code)
        st.code(result, language='text')
    else:
        st.info("Code ka output yahan dikhega!")

st.divider()

# Footer
st.markdown("""
<p style='text-align: center;'>
    Made with ❤️ by <a href='https://github.com/shishirkumar12' target='_blank'>Shishir Kumar</a>  
    | Try commands like <code>bol</code>, <code>rakh</code>, <code>jod</code>, <code>kaam karle</code> and more!
</p>
""", unsafe_allow_html=True)









