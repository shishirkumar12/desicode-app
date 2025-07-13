import streamlit as st
from desicode_interpreter import run_desicode

# 🎨 Page settings
st.set_page_config(page_title="DesiCode 🧠", page_icon="🌶️", layout="centered")

# 🖼️ Header
st.markdown("<h1 style='text-align: center;'>💻🎉 DesiCode – Apni Desi Programming Language 🎉💻</h1>", unsafe_allow_html=True)
st.markdown("### 🧠 Learn coding in a desi style with `bol`, `rakh`, `agar`, and `repeat`!\n", unsafe_allow_html=True)

# ⚠️ Mobile warning
st.warning("⚠️ Best experienced on **laptops or desktops**. Mobile support coming soon!")

# 📂 Examples to choose
examples = {
    "👋 Namaste Duniya": 'bol "Namaste Duniya!"',
    "📦 Naam Print": 'rakh naam "Shishir"\nbol "Mera naam hai:"\nbol naam',
    "🔁 Repeat 3 Times": 'repeat 3 bol "Coding is fun!"',
    "🧠 Condition Example": 'rakh naam "Shishir"\nagar naam barabar "Shishir" toh bol "Sahi pakde hain!"'
}

# Tabs
tab1, tab2 = st.tabs(["📝 DesiCode Editor", "🐍 Python Equivalent"])

# 📝 DesiCode Editor tab
with tab1:
    selected_example = st.selectbox("📂 Choose Example Code:", list(examples.keys()))
    default_code = examples[selected_example]
    user_code = st.text_area("✍️ Likho apna DesiCode yahan:", default_code, height=200)

    if st.button("🔥 Run Code"):
        result = run_desicode(user_code)
        st.subheader("🖨️ Output:")
        st.code(result)

# 🐍 Python Equivalent tab
with tab2:
    st.markdown("### DesiCode vs Python – Learn Instantly 👇")
    st.markdown("""
| DesiCode                                   | Python                            |
|-------------------------------------------|-----------------------------------|
| `bol "Hello"`                             | `print("Hello")`                  |
| `rakh naam "Shishir"`                     | `naam = "Shishir"`                |
| `agar naam barabar "Shishir" toh bol "Ok"`| `if naam == "Shishir": print("Ok")` |
| `repeat 3 bol "Hi"`                       | `for i in range(3): print("Hi")`  |
""")

# 💬 Feedback box
st.markdown("---")
st.markdown("### 💬 Kaisa laga aapko DesiCode?")
feedback = st.text_input("Aapka feedback (chhota ya bada, dono chalega!)")

if st.button("📤 Submit Feedback"):
    st.success("Shukriya! Aapka feedback record ho gaya hai 😄")

# ❤️ Footer
st.markdown("---")
st.markdown("Made with ❤️ by [Shishir Kumar](https://github.com/shishirkumar12)")
st.markdown("⭐ Try more examples using `bol`, `rakh`, `agar`, `repeat` — aur coding ho jaaye desi style mein!")


