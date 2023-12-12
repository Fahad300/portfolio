import streamlit as st
from send_email import send_email

st.title("Contact Us")

with st.form(key="contact_us_form"):
    user_email = st.text_input("Please Enter your Email")
    user_msg = st.text_area("Please Enter a message")
    send_button = st.form_submit_button("Submit")
    message = f"""
    New User from PORTFOLIO\n
    From: {user_email}\n
    {user_msg}     
    """
    if send_button:
        send_email(message)
        st.success("Email Sent Successfully.")