# Importiert die LED-Klasse zur Steuerung der GPIO-Ausgänge.
from gpiozero import LED
# Importiert getpass für eine verdeckte Passworteingabe im Terminal.
from getpass import getpass
# Importiert sleep für die zeitlich begrenzten LED-Signale.
from time import sleep
# Legt das gültige Passwort fest.
PASSWORT = "bratwurst"
 
# Verbindet die rote LED mit GPIO 22 (BCM-Nummerierung).
rot = LED(22)
# Verbindet die gelbe LED mit GPIO 27(BCM-Nummerierung).
gelb = LED(27)
# Verbindet die grüne LED mit GPIO 17 (BCM-Nummerierung).
gruen = LED(17)
 
try:
    # Speichert, ob bereits ein falsches Passwort eingegeben wurde.
    falsche_versuche = 0
    # Fragt so lange nach dem Passwort, bis es richtig oder zweimal falsch eingegeben wurde.
    while True:
        # Fragt das Passwort ab, ohne die Eingabe im Terminal anzuzeigen.
        eingabe = getpass("Bitte Passwort eingeben: ")
        # Prüft, ob die Eingabe dem festgelegten Passwort entspricht.
        if eingabe == PASSWORT:
            # Zeigt eine richtige Eingabe zwei Sekunden lang mit Grün an.
            gruen.on()
            sleep(2)
            gruen.off()
            break
        # Prüft, ob dies der erste falsche Versuch ist.
        if falsche_versuche == 0:
            # Merkt sich den ersten falschen Versuch.
            falsche_versuche += 1
            # Lässt Rot kurz für eine Sekunde aufleuchten.
            rot.on()
            sleep(1)
            rot.off()
            # Lässt Gelb leuchten, während auf die nächste Eingabe gewartet wird.
            gelb.on()
        else:
            # Schaltet nach dem zweiten falschen Versuch die rote LED dauerhaft ein.
            rot.on()
            # Wartet endlos, ohne erneut eine Passworteingabe anzufordern.
            while True:
                sleep(1)
finally:
    # Schaltet alle LEDs aus, wenn das Programm beendet oder unterbrochen wird.
    rot.off()
    gelb.off()
    gruen.off()
