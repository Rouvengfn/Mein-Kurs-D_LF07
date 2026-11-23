import sqlite3

verbindung = sqlite3.connect("messwerte.db")

cursor = verbindung.cursor()

cursor.execute("""
SELECT id, zeit, wert
FROM messwerte
ORDER BY id
""")

daten = cursor.fetchall()

print("Gespeicherte Messwerte")
print("------------------------------")

for datensatz in daten:
    print(
        "ID:", datensatz[0],
        "| Zeit:", datensatz[1],
        "| Temperatur:", datensatz[2], "°C"
    )

print("------------------------------")
print("Anzahl Datensätze:", len(daten))

verbindung.close()