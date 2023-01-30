import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address: ")
    raw_message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        message = f"""\
Subject: New email from {user_email} via Portfolio Site

From: {user_email}
{raw_message}
"""
        send_email(message)
        st.info("Your message sent successfully.")
