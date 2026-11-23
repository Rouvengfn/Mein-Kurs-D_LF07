from gpiozero import PWMLED
 
# PWMLED statt LED: damit kann man die Helligkeit stufenlos regeln (0.0 bis 1.0)
# GPIO-Nummern (BCM), nicht die Pin-Nummern auf der Leiste!
rot = PWMLED(15)  # Pin 15
gelb = PWMLED(13)  # Pin 13
gruen = PWMLED(11)  # Pin 130
 
LAMPEN = [("Rot", rot), ("Gelb", gelb), ("Grün", gruen)]
 
LEUCHT_DAUER = 5  # Sekunden voll an
EINBLENDEN = 0.8  # Sekunden für das sanfte Hochfahren
AUSBLENDEN = 0.8  # Sekunden für das sanfte Runterfahren
 
try:
    while True:
        for name, lampe in LAMPEN:
            print(f"{name} leuchtet ...")
            # Einmal: einblenden -> 5 s an -> ausblenden. Wartet, bis es fertig ist.
            lampe.blink(
                on_time=LEUCHT_DAUER,
                off_time=0,
                fade_in_time=EINBLENDEN,
                fade_out_time=AUSBLENDEN,
                n=1,
                background=False,
            )
except KeyboardInterrupt:
    print("\nBeendet.")

