import streamlit as st
from desicode_interpreter import run_desicode

# Streamlit page settings
st.set_page_config(page_title="DesiCode 🧠", page_icon="🌶️", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>💻🎉 DesiCode – Apni Desi Programming Language 🎉💻</h1>", unsafe_allow_html=True)
st.markdown("### 🧠 Learn coding in a desi style with `bol`, `rakh`, `jod`, `guna`, `kaam karle`, `rakh a = 10`, and more!", unsafe_allow_html=True)
st.warning("⚠️ Works best on laptop/desktop browsers.")

# Example programs
examples = {
    "👋 Namaste Duniya": 'bol "Namaste Duniya!"',
    "📦 Naam Print": 'rakh naam = "Shishir"\nbol "Mera naam hai:"\nbol naam',
    "🔁 Repeat 3 Times": 'repeat 3 bol "Coding is fun!"',
    "🧠 Condition Example": 'rakh naam = "Shishir"\nagar naam barabar "Shishir" toh bol "Sahi pakde hain!"',
    "➕➖ Math Example": 'rakh a = 10\nrakh b = 5\nrakh total jod a b\nbol total',
    "🧑‍💻 Function Example": 'kaam karle intro\nbol "Namaste Duniya!"\nrakh naam = "Shishir"\nbol naam\nkhatam\n\nintro',
    "🧾 Multiline Print": 'bol "Namaste Duniya!"\nbol "Mera naam hai:\\nShishir\\nAur main DesiCoder hoon!"'
}

# Tabs: Editor + Python Comparison
tab1, tab2 = st.tabs(["📝 DesiCode Editor", "🐍 Python Equivalent"])

# Editor tab
with tab1:
    selected_example = st.selectbox("📂 Choose Example Code:", list(examples.keys()))
    raw_code = st.text_area("✍️ Likho apna DesiCode yahan:", examples[selected_example], height=250)
    user_code = raw_code.encode('utf-8').decode('unicode_escape')  # 🔥 Key fix for decoding \\n properly

    if st.button("🔥 Run Code"):
        result = run_desicode(user_code)
        st.subheader("🖨️ Output:")
        st.markdown(f"```\n{result}\n```")  # This renders true multiline output!

# Python Comparison tab
with tab2:
    st.markdown("### DesiCode vs Python – Learn Instantly 👇")
    st.markdown("""
| DesiCode                                   | Python Equivalent                    |
|--------------------------------------------|---------------------------------------|
| bol "Hello"                                | print("Hello")                        |
| rakh naam = "Shishir"                      | naam = "Shishir"                      |
| agar naam barabar "Shishir" toh bol "Hi"   | if naam == "Shishir": print("Hi")    |
| repeat 3 bol "Hi"                          | for i in range(3): print("Hi")        |
| jod a b                                    | a + b                                 |
| rakh total jod a b                         | total = a + b                         |
| kaam karle intro ... khatam                | def intro(): ...                      |
| intro                                      | intro()                               |
| bol "Line1\\nLine2"                        | print("Line1\\nLine2")                |
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
st.markdown("⭐ Try more examples using `bol`, `rakh`, `agar`, `repeat`, `kaam karle`, and math-style assignments!")







