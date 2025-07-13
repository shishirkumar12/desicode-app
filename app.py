import streamlit as st
from desicode_interpreter import run_desicode

st.set_page_config(page_title="DesiCode Interpreter", page_icon="🧠")

st.title("🧠 DesiCode - Apni Desi Programming Language")
st.write("Likho apna DesiCode niche aur run karo!")

default_code = '''bol "Namaste Duniya!"
rakh naam "Shishir"
bol "Mera naam hai:"
bol naam
'''

user_code = st.text_area("✍️ DesiCode likho:", default_code, height=200)

if st.button("🔥 Run Code"):
    result = run_desicode(user_code)
    st.subheader("🖨️ Output:")
    st.code(result)
