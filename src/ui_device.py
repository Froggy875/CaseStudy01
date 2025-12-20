import streamlit as st
from queries import find_devices, find_users
from devices import Device
from users import User

# grundkonfiguration
st.set_page_config(page_title="Admin-Panel", layout="wide")


# --- DIALOG FENSTER DEFINITION ---
@st.dialog("Gerät bearbeiten")
def edit_device_dialog(devices_in_db):
    st.write("## Geräteauswahl")
    if devices_in_db:
        current_device_name = st.selectbox(
            'Gerät auswählen',
            options=devices_in_db, key="sbDevice")

        if current_device_name in devices_in_db:
            loaded_device = Device.find_by_attribute("device_name", current_device_name)
            
            if loaded_device:                
                # Das Formular kombiniert dein Layout mit deiner Logik
                with st.form("Device"):
                    st.write(f"Bearbeite: **{loaded_device.device_name}**")

                    # Eingabefeld für den Verantwortlichen (Logik aus deinem Beispiel)
                    text_input_val = st.text_input("Geräte-Verantwortlicher", value=loaded_device.managed_by_user_id)
                    loaded_device.set_managed_by_user_id(text_input_val)

                    # Every form must have a submit button.
                    submitted = st.form_submit_button("Submit")
                    if submitted:
                        loaded_device.store_data()
                        st.write("Data stored.")
                        st.rerun()
            else:
                st.error("Device not found in the database.")
        else:
            st.error("Selected device is not in the database.")
    else:
        st.write("No devices found.")


@st.dialog("Gerät hinzufügen")
def add_device_dialog(devices_in_db):
    with st.form("add_device_form", clear_on_submit=True):
        # 1. Eingabefeld für den neuen Namen
        new_name = st.text_input("Gerätename (einzigartig)")
        
        # 2. Eingabefeld für die E-Mail des Zuständigen
        new_manager_email = st.text_input("Zuständiger (E-Mail)")

        submitted = st.form_submit_button("Gerät anlegen")

        if submitted:
            if not new_name or not new_manager_email:
                st.error("Bitte beide Felder ausfüllen.")
            
            # Prüfung auf Einzigartigkeit
            elif new_name in devices_in_db:
                st.error(f"Fehler: Ein Gerät mit dem Namen '{new_name}' existiert bereits!")
            
            else:
                # 3. Neues Gerät-Objekt erstellen
                # Ich nehme an, die Device-Klasse kann so initialisiert werden:
                try:
                    new_device = Device(device_name=new_name, managed_by_user_id=new_manager_email)
                    
                    # Daten speichern
                    new_device.store_data()
                    
                    st.success(f"Gerät '{new_name}' wurde erfolgreich angelegt.")
                    st.rerun()  # Schließt den Dialog und aktualisiert die Liste im Hintergrund
                except Exception as e:
                    st.error(f"Fehler beim Speichern: {e}")

# --- DIALOG FENSTER DEFINITION ---
@st.dialog("Nutzer bearbeiten")
def edit_user_dialog(users_in_db): # 1. Parameter passend benannt
    st.write("## Nutzerauswahl")
    
    if users_in_db:
        current_id = st.selectbox(
            'Nutzer auswählen',
            options=users_in_db, key="sbUser")

        if current_id in users_in_db:
            # 2. WICHTIG: User statt Device verwenden!
            loaded_user = User.find_by_attribute("id", current_id)
            
            if loaded_user:                
                with st.form("User_Form"): # Eindeutiger Formular-Name
                    st.write(f"Bearbeite: **{loaded_user.id}**")

                    # Name bearbeiten
                    new_name = st.text_input("Name", value=loaded_user.name)
                    
                    submitted = st.form_submit_button("Speichern")
                    if submitted:
                        loaded_user.name = new_name 
                        loaded_user.store_data()
                        st.success("Nutzerdaten gespeichert.")
                        st.rerun()
            else:
                st.error("Nutzer wurde in der Datenbank nicht gefunden.")
        else:
            st.error("Ausgewählte ID ist nicht in der Liste.")
    else:
        st.write("Keine Nutzer zum Bearbeiten vorhanden.")


@st.dialog("Nutzer hinzufügen")
def add_user_dialog(users_in_db):
    with st.form("add_device_form", clear_on_submit=True):
        
        # Eingabefeld für die E-Mail des Zuständigen
        new_email = st.text_input("E-Mail (einzigartig)")

        # Eingabefeld für den neuen Namen
        new_name = st.text_input("Name")


        submitted = st.form_submit_button("Nutzer anlegen")

        if submitted:
            if not new_name or not new_email:
                st.error("Bitte beide Felder ausfüllen.")
            
            # Prüfung auf Einzigartigkeit
            elif new_name in devices_in_db:
                st.error(f"Fehler: Ein Nutzer mit dem Namen '{new_name}' existiert bereits!")
            
            else:
                # 3. Neues Gerät-Objekt erstellen
                # Ich nehme an, die Device-Klasse kann so initialisiert werden:
                try:
                    new_user = User(name=new_name, id=new_email)
                    
                    # Daten speichern
                    new_user.store_data()
                    
                    st.success(f"Gerät '{new_name}' wurde erfolgreich angelegt.")
                    st.rerun()  # Schließt den Dialog und aktualisiert die Liste im Hintergrund
                except Exception as e:
                    st.error(f"Fehler beim Speichern: {e}")









st.title("Admin-Dashboard")

# Navigation zurück
if st.button("⬅ Zurück zum Hauptmenü"):
    st.switch_page("ui_device.py")

# Definition der Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Geräte-Verwaltung", 
    "Nutzer-Verwaltung", 
    "Reservierungssystem", 
    "Wartungsmanagement"
])

# --- TAB 1: GERÄTE-VERWALTUNG ---
with tab1:

    st.subheader("Registrierte Geräte")

    col1, col2, col3 = st.columns([2, 2, 1])
    col1.write("Gerätename")
    col2.write("Zuständig")


    # Eine Auswahlbox mit Datenbankabfrage, das Ergebnis wird in current_device gespeichert
    devices_in_db = find_devices()

    # container damit seite nicht überlaufen kann..
    with st.container(height=300): 
            for device in devices_in_db:
                current_device = Device.find_by_attribute("device_name", device)
                
                # Diese Zeilen sind jetzt eingerückt
                if current_device is not None:
                    c1, c2, c3 = st.columns([2, 2, 1])
                    c1.write(current_device.device_name)
                    c2.write(current_device.managed_by_user_id)
                    if c3.button("Entfernen", key=f"del_{current_device.device_name}"):
                        current_device.delete()
                        st.rerun()


    col1, col2 = st.columns([1,3.5])
    if col1.button("Gerät hinzufügen"):
        add_device_dialog(devices_in_db)

    if col2.button("Gerät bearbeiten"):
        edit_device_dialog(devices_in_db)



# --- TAB 2, 3 & 4 ---
with tab2:
    st.subheader("Registrierte Nutzer")

    col1, col2, col3 = st.columns([2, 2, 1])
    col1.write("Email")
    col2.write("Name")


    # Eine Auswahlbox mit Datenbankabfrage, das Ergebnis wird in current_device gespeichert
    users_in_db = find_users()

    # container damit seite nicht überlaufen kann..
    with st.container(height=300): 
            for user in users_in_db:
                current_user = User.find_by_attribute("id", user)
                    
                if user is not None:
                    c1, c2, c3 = st.columns([2, 2, 1])
                    c1.write(current_user.name)
                    c2.write(current_user.id)
                    
                    if c3.button("Entfernen", key=f"del_{current_user.id}"):
                        current_user.delete()
                        st.rerun()


    col1, col2 = st.columns([1,3.5])
    if col1.button("Nutzer hinzufügen"):
        add_user_dialog(users_in_db)

    if col2.button("Nutzer bearbeiten"):
        edit_user_dialog(users_in_db)

with tab3:
    st.header("Reservierung vornehmen")
    # ... (Dein restlicher Code für Tab 3)

with tab4:
    st.header("Wartungs-Management Übersicht")
    st.subheader("Anstehende Wartungstermine")
    st.dataframe({
        "Gerät": ["Server Rack", "Klimaanlage"],
        "Datum": ["2024-01-15", "2024-02-01"],
        "Status": ["Dringend", "Geplant"]
    }, width='stretch')