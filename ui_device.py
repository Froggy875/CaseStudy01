import streamlit as st

st.title("Login")
st.text_input("Nutzername")
st.text_input("Passwort")

if st.button("Login"):
    st.switch_page("pages/user_page.py")

if st.button("Ich bin Admin"):
    st.switch_page("pages/admin_page.py")
