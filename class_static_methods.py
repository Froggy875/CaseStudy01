class Device:
    counter = 0  # Klassenattribut für die Anzahl der Instanzen
    def __init__(self, name, farbe):
        self.name = name
        self.farbe = farbe
        Device.counter += 1  # Erhöhe den Zähler bei jeder Instanzerstellung
    @classmethod
    def von_typ(cls, typ):  # Alternativer Konstruktor
        if typ == "Laptop":
            return cls("Standard-Laptop", "Silber")
        else:
            return cls("Unbekanntes Gerät", "Weiß")
gerät1 = Device.von_typ("Laptop")
gerät2 = Device.von_typ("Tablet")
gerät3 = Device("Smartphone", "Schwarz")
print("Erstellte Geräte:", Device.counter)  # Ausgabe: 3