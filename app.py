import streamlit as st
import os

html_code = """YOUR FULL HTML CODE HERE"""

# Write to a file
with open("portfolio.html", "w", encoding="utf-8") as f:
    f.write(html_code)

# Read and display
with open("portfolio.html", "r", encoding="utf-8") as f:
    html_content = f.read()
    
st.set_page_config(page_title="Jhanvi Jyant — Design Portfolio", page_icon="🎨", layout="wide")
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp {margin: 0; padding: 0;}
    </style>
""", unsafe_allow_html=True)

st.components.v1.html(html_content, height=800, scrolling=True)
