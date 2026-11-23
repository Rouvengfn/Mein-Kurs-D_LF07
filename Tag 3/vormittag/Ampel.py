# Importiert die LED-Klasse zur Steuerung der GPIO-Ausgänge.
from gpiozero import LED
# Importiert sleep, damit jede LED fünf Sekunden leuchten kann.
from time import sleep

# Verbindet die rote LED mit GPIO 25 (BCM-Nummerierung).
rot = LED(25)
# Verbindet die gelbe LED mit GPIO 24 (BCM-Nummerierung).
gelb = LED(24)
# Verbindet die grüne LED mit GPIO 23 (BCM-Nummerierung).
gruen = LED(23)

try:
	# Wiederholt die Ampel-Sequenz unbegrenzt.
	while True:
		# Schaltet jede LED der Reihe nach für fünf Sekunden ein.
		for lampe in (rot, gelb, gruen):
			lampe.on()
			sleep(5)
			lampe.off()
finally:
	# Schaltet alle LEDs auch beim Beenden des Programms aus.
	rot.off()
	gelb.off()
	gruen.off()
