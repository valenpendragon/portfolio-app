import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=400)

with col2:
    st.title("Jeffrey Scott")
    content = """
    I started out my career expecting to be an applied mathematician with a very strong background in statistics,
    five other major areas of mathematics. The termination of the Supercollider Project changed all of that. My
    skills with Unix and network engineering transformed me into a system and network engineer. I worked in that
    capacity for over two decades, until health and vision problems forced me to take time off from work.
    During that period, I discovered Python 2.7 and 3.x. It was a language I really enjoyed working with, unlike
    C/C++/C#. I began building a portfolio of programming projects to demonstrate my skills in this area.
    """
    st.info(content)

contact_msg = """
Below, you can find my slowly growing list of applications I built in Python. 
Feel free to contact me using the links in the left panel.
"""
st.write(contact_msg)