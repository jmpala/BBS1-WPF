""""
Aufgabe 1:

Erstellen Sie eine Liste kontostand und füllen Sie diese Liste
mit 10.000.000 zufälligen Ganzzahlen zwischen –10.000 und +100.000.
Verwenden Sie zum Erzeugen der Zufallszahlen
die randint-Funktion der random-Bibliothek.
Messen Sie außerdem die Zeit, die das Erzeugen dieser langen Liste in Anspruch nimmt. Verwenden
Sie hierzu die time-Funktion der time-Bibliothek. Messen Sie den Zeitpunkt vor dem Erstellen der
Liste, den Zeitpunkt nach dem Erstellen der Liste und bilden Sie die Differenz aus beiden, um die
verstrichene Zeit zu ermitteln.
Geben Sie schlussendlich die gemessene Zeit auf der Konsole aus (geben Sie die Liste selbst besser
nicht aus, denn die ist seee…eeehr lang).
"""
import random
import time

kontostand = []

time_start = time.time()

for x in range(10_000_000):
    kontostand.append(random.randint(-10_000, 100_000))

time_end = time.time()

print("The operation took: ", time_end - time_start, " Seconds")
