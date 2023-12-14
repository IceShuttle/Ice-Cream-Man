import streamlit as st
import db

st.set_page_config(page_title="Login Page", page_icon="🔒")
st.title("Login Here")

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        db.connect_db(username,password)
        if db.is_connected():
            st.success("Logged in!")
        else:
            st.error("Invalid username or password")

    if st.button("LogOut"):
        db.disconnect()

login()
