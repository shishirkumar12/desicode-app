import streamlit as st
from desicode_interpreter import run_desicode

st.set_page_config(page_title="DesiCode 🧠", page_icon="🌶️", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>💻🎉 DesiCode – Apni Desi Programming Language 🎉💻</h1>", unsafe_allow_html=True)
st.markdown("### 🧠 Learn coding in a desi style with `bol`, `rakh`, `jod`, `guna`, `kaam karle` and more!", unsafe_allow_html=True)
st.warning("⚠️ Works best on laptop/desktop browsers.")

# DesiCode examples
examples = {
    "👋 Namaste Duniya": 'bol "Namaste Duniya!"',
    "📦 Naam Print": 'rakh naam "Shishir"\nbol "Mera naam hai:"\nbol naam',
    "🔁 Repeat 3 Times": 'repeat 3 bol "Coding is fun!"',
    "🧠 Condition Example": 'rakh naam "Shishir"\nagar naam barabar "Shishir" toh bol "Sahi pakde hain!"',
    "➕➖ Math Example": 'jod 5 3\nghata 10 2\nguna 4 3\nbhaag 8 2',
    "🧑‍💻 Function Example": 'kaam karle intro\nbol "Namaste Duniya!"\nrakh naam "Shishir"\nbol naam\nkhatam\n\nintro'
}

# Tabs
tab1, tab2 = st.tabs(["📝 DesiCode Editor", "🐍 Python Equivalent"])

with tab1:
    selected_example = st.selectbox("📂 Choose Example Code:", list(examples.keys()))
    user_code = st.text_area("✍️ Likho apna DesiCode yahan:", examples[selected_example], height=250)

    if st.button("🔥 Run Code"):
        result = run_desicode(user_code)
        st.subheader("🖨️ Output:")
        st.code(result)

with tab2:
    st.markdown("### DesiCode vs Python – Learn Instantly 👇")
    st.markdown("""
| DesiCode                                 | Python Equivalent                     |
|------------------------------------------|----------------------------------------|
| bol "Hello"                              | print("Hello")                         |
| rakh naam "Shishir"                      | naam = "Shishir"                       |
| agar naam barabar "Shishir" toh bol "Hi"| if naam == "Shishir": print("Hi")     |
| repeat 3 bol "Hi"                        | for i in range(3): print("Hi")         |
| jod 5 3                                  | 5 + 3                                  |
| ghata 10 2                               | 10 - 2                                 |
| guna 4 6                                 | 4 * 6                                  |
| bhaag 8 2                                | 8 / 2                                  |
| pucho naam                               | input("naam")                          |
| kaam karle intro ... khatam             | def intro(): ...                      |
    """)

# Feedback
st.markdown("---")
st.markdown("### 💬 Kaisa laga aapko DesiCode?")
feedback = st.text_input("Aapka feedback (chhota ya bada, dono chalega!)")
if st.button("📤 Submit Feedback"):
    st.success("Shukriya! Aapka feedback record ho gaya hai 😄")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by [Shishir Kumar](https://github.com/shishirkumar12)")
st.markdown("⭐ Try more examples using `bol`, `rakh`, `agar`, `repeat`, `kaam karle` — aur coding ho jaaye desi style mein!")




