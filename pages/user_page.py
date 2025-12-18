from datetime import time, date
import streamlit as st


st.title("Gerät reservieren")
selected_device = st.selectbox(
        "Gerät auswählen",
        ("Gerät1", "Gerät2", "Gerät3")
    )

selected_date = st.date_input(
        "Datum auswählen",
        value=date.today()
    )

col1, col2 = st.columns(2)

with col1:
    from_time = st.time_input("Von", value=time(8, 0))

with col2:
    to_time = st.time_input("Bis", value=time(17, 0))

if st.button("Auswahl speichern"):
    st.write(f"{selected_device} wurde für {selected_date.strftime('%d.%m.%Y')} von {from_time} bis {to_time} reserviert")
