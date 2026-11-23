import paho.mqtt.client as mqtt
import random
import time

# MQTT-Client erstellen
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

# Verbindung mit Mosquitto
client.connect("localhost", 1883)

print("Sender gestartet!")
print("------------------")

# 20 Temperaturwerte erzeugen
for nummer in range(1, 21):

    temperatur = round(random.uniform(18, 25), 1)

    client.publish(
        "sensor/temperature",
        temperatur
    )

    print(
        "Event", nummer,
        "gesendet:",
        temperatur,
        "°C"
    )

    time.sleep(2)

# Verbindung beenden
client.disconnect()

print("------------------")
print("20 Events wurden gesendet.")