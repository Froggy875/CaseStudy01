# Eine Auswahlbox mit Datenbankabfrage, das Ergebnis wird in current_device gespeichert
devices_in_db = find_devices()
if devices_in_db:
    current_device_name = st.selectbox(
        'Gerät auswählen',
        options=devices_in_db, key="sbDevice")
    if current_device_name in devices_in_db:
        loaded_device = Device.find_by_attribute("device_name", current_device_name)
        if loaded_device:
            st.write(f"Loaded Device: {loaded_device}") # nutzt __str__ Methode
        else:
            st.error("Device not found in the database.")
        with st.form("Device"):
            st.write(loaded_device.device_name) # Direkter Zugriff auf die Attribute
            text_input_val = st.text_input("Geräte-Verantwortlicher", value=loaded_device.managed_by_user_id)
            loaded_device.set_managed_by_user_id(text_input_val) # Nutzt die Setter-Methode
            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                loaded_device.store_data()
                st.write("Data stored.")
                st.rerun()