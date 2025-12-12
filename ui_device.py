import streamlit as st
from datetime import datetime, time

tab1, tab2 = st.tabs(["User-Login", "Gerätemanagement"])

with tab2:
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

with tab1:
   st.write("# User-Login")
   if st.button("New User"):
      email = st.text_input(
      label='Geben Sie hier Ihre Email-Adresse ein:',
      value='' # Optionaler Startwert
      )

      pw = st.text_input(
      label='Geben Sie hier Ihr Passwort ein:',
      value='' # Optionaler Startwert
      )
      

   login_button = st.button("login")






