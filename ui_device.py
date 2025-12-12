import streamlit as st
from datetime import datetime, time

# Eine Überschrift der ersten Ebene
st.write("# Gerätemanagement")

# Eine Überschrift der zweiten Ebene
st.write("## Geräteauswahl")

# Eine Auswahlbox mit hard-gecoded Optionen, das Ergebnis

current_device = st.selectbox(label='Gerät auswählen',
        options = ["Gerät_A", "Gerät_B"])

st.write(f"Das ausgewählte Gerät ist {current_device}")

#Zeitauswahl

# 1) Datum wählen
datum = st.date_input("Datum auswählen")

# 2) Start- und Endzeit wählen
col1, col2 = st.columns(2)
with col1:
    start_time = st.time_input("Startzeit", value=time(9, 0))
with col2:
    end_time = st.time_input("Endzeit", value=time(17, 0))

# 3) Kombinierten Zeitslot anzeigen
if start_time >= end_time:
    st.error("Endzeit muss nach der Startzeit liegen.")
else:
    start_dt = datetime.combine(datum, start_time)
    end_dt = datetime.combine(datum, end_time)
    st.write("Gewählter Zeitslot:")
    st.write(start_dt, "–", end_dt)





