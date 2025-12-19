import streamlit as st

# Grundkonfiguration (falls nicht bereits in der Datei vorhanden)
st.set_page_config(page_title="Admin-Panel", layout="wide")

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

# --- TAB 1: GERÄTE-VERWALTUNG (KORRIGIERT) ---
with tab1:
    st.header("Geräte-Verwaltung")
    
    # 1. BESTANDSLISTE
    st.subheader("Aktueller Gerätebestand")

    # Erweiterte Mockup-Daten mit Zuständigkeiten
    geraete_daten = [
        {"ID": "INV-001", "Name": "MacBook Pro", "Status": "Verfügbar", "Zustaendig": "Max Mustermann"},
        {"ID": "INV-002", "Name": "Dell Monitor", "Status": "Verliehen", "Zustaendig": "Erika Musterfrau"},
        {"ID": "INV-003", "Name": "iPad Air", "Status": "Wartung", "Zustaendig": "Technik-Team"}
    ]

    # Tabellen-Header (optional für bessere Lesbarkeit)
    h1, h2, h3, h4, h5 = st.columns([1, 2, 2, 2, 1])
    h1.markdown("**ID**")
    h2.markdown("**Name**")
    h3.markdown("**Status**")
    h4.markdown("**Zuständig**")
    h5.write("") # Platzhalter für Button-Spalte

    # Anzeige der Liste
    for geraet in geraete_daten:
        # Neue Spaltenaufteilung: ID, Name, Status, Zuständig, Aktion
        col_id, col_name, col_status, col_zustaendig, col_action = st.columns([1, 2, 2, 2, 1])
        
        col_id.write(geraet["ID"])
        col_name.write(geraet["Name"])
        col_status.write(geraet["Status"])
        col_zustaendig.write(geraet["Zustaendig"]) # Neue Spalte
        
        if col_action.button("Löschen", key=f"del_{geraet['ID']}"):
            st.error(f"Gerät {geraet['ID']} würde gelöscht werden.")

    st.divider() # Optische Trennung

    # 2. GERÄT HINZUFÜGEN (Darunter platziert)
    st.subheader("Neues Gerät hinzufügen")
    with st.expander("Formular zum Hinzufügen öffnen", expanded=True):
        with st.form("add_device_form"):
            c1, c2 = st.columns(2)
            with c1:
                st.text_input("Gerätename")
                st.selectbox("Zuständiger", ["Nils", "Mathias"])
            with c2:
                st.text_input("Seriennummer")
                st.selectbox("Kategorie", ["IT-Hardware", "Büro", "Werkzeug"])

            
            # Schritt 4 & 5 aus deinem Ablauf: Bestätigung und Speichern
            if st.form_submit_button("Gerät speichern"):
                st.success("System speichert Gerätedaten...")

# --- TAB 2: NUTZER-VERWALTUNG ---
with tab2:
    st.header("Nutzer-Verwaltung")
    
    # 1. NUTZERLISTE
    st.subheader("Registrierte Nutzer")
    
    # Mockup-Daten für Nutzer
    nutzer_daten = [
        {"ID": "USR-01", "Name": "Max Mustermann", "Rolle": "Admin"},
        {"ID": "USR-02", "Name": "Erika Musterfrau", "Rolle": "Standard-Nutzer"},
        {"ID": "USR-03", "Name": "John Doe", "Rolle": "Techniker"}
    ]
    
    # Anzeige der Nutzerliste
    for nutzer in nutzer_daten:
        c_id, c_name, c_rolle, c_action = st.columns([1, 2, 2, 1])
        c_id.write(nutzer["ID"])
        c_name.write(nutzer["Name"])
        c_rolle.write(nutzer["Rolle"])
        if c_action.button("Entfernen", key=f"del_usr_{nutzer['ID']}"):
            st.error(f"Nutzer {nutzer['Name']} wurde entfernt (Mockup)")

    st.divider()

    # 2. NUTZER ANLEGEN (Darunter)
    st.subheader("Neuen Nutzer registrieren")
    with st.expander("Nutzerdaten-Eingabe öffnen", expanded=True):
        with st.form("add_user_form"):
            col_left, col_right = st.columns(2)
            with col_left:
                st.text_input("Vorname")
                st.text_input("Nachname")
            with col_right:
                st.text_input("E-Mail Adresse")
                st.selectbox("Rolle zuweisen", ["Standard-Nutzer", "Admin", "Techniker", "Gast"])
            
            # Schritt: Eingabe bestätigen
            if st.form_submit_button("Nutzer im System anlegen"):
                st.success("System speichert Nutzerdaten...")

# --- TAB 3: RESERVIERUNGSSYSTEM ---
with tab3:
    st.header("Reservierung vornehmen")
    # Schritt 2: Gerät auswählen
    selected_device = st.selectbox("Gerät auswählen", ["Laptop A", "Beamer B", "Messgerät C"])
    
    # Schritt 3: Reservierungsdaten eingeben
    col_a, col_b = st.columns(2)
    with col_a:
        st.date_input("Startdatum")
    with col_b:
        st.date_input("Enddatum")
    
    st.info("Validierung bestehender Reservierungen läuft im Hintergrund...")
    
    # Schritt 4 & 5
    if st.button("Reservierung bestätigen"):
        st.success(f"System speichert Reservierungsdaten für {selected_device}")

# --- TAB 4: WARTUNGSMANAGEMENT ---
with tab4:
    st.header("Wartungs-Management Übersicht")
    
    # Schritt 2: Nächste Wartungstermine anzeigen
    st.subheader("Anstehende Wartungstermine")
    st.dataframe({
        "Gerät": ["Server Rack", "Klimaanlage", "Gabelstapler"],
        "Datum": ["2024-01-15", "2024-02-01", "2024-03-10"],
        "Status": ["Dringend", "Geplant", "Geplant"]
    }, use_container_width=True)
    
    st.divider()
    
    # Schritt 3: Wartungskosten anzeigen
    st.subheader("Wartungskosten pro Quartal (Prognose)")
    st.bar_chart({"Q1": 1200, "Q2": 800, "Q3": 2500, "Q4": 450})
    st.metric(label="Gesamtkosten nächstes Quartal", value="2.500 €", delta="15% zum Vorjahr")
