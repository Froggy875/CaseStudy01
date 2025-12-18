import streamlit as st

if st.button("Admin Page"):
    st.session_state.user_data = "Beispiel-Daten"
    st.switch_page("pages/admin_page.py")

if st.button("User Page"):
    st.session_state.user_data = "Beispiel-Daten"
    st.switch_page("pages/user_page.py")


