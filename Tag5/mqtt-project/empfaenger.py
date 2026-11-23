import paho.mqtt.client as mqtt
import sqlite3
from datetime import datetime


def on_message(client, userdata, message):
    wert = message.payload.decode()
    zeit = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Empfangen:", wert, "Zeit:", zeit)

    verbindung = sqlite3.connect("messwerte.db")
    cursor = verbindung.cursor()

    cursor.execute(
        "INSERT INTO messwerte (zeit, wert) VALUES (?, ?)",
        (zeit, wert)
    )

    verbindung.commit()
    verbindung.close()


# Datenbank erstellen
verbindung = sqlite3.connect("messwerte.db")
cursor = verbindung.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messwerte (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    zeit TEXT,
    wert REAL
)
""")

verbindung.commit()
verbindung.close()


# MQTT-Client
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.on_message = on_message

client.connect("localhost", 1883)

client.subscribe("sensor/temperature")

print("Empfänger läuft...")
print("Warte auf Nachrichten auf sensor/temperature")

client.loop_forever()
