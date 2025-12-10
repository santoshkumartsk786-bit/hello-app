# ============================
# GOOGLE COLAB VERSION
# ============================

print("Welcome to the Name App!")
name = input("What is your name? ")

print(f"Hello, {name}! Nice to meet you 😊")
import streamlit as st

st.title("Simple Name App")

name = st.text_input("What is your name?")

if name:
    st.success(f"Hello, {name}! Nice to meet you 😊")
