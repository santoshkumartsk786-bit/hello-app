import streamlit as st

st.set_page_config(page_title="Name App")

st.title("Hello! 👋")

st.write("Please enter your name below:")

name = st.text_input("Your Name")

if st.button("Submit"):
    if name.strip() == "":
        st.error("Please type a name.")
    else:
        st.success(f"Hello, {name}! Nice to meet you 😊")
