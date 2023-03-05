""""
Aufgabe 4:

Die griechische Steuerverwaltung möchte den durchschnittlichen Kontostand aller
Griechen ermitteln. Hierzu sollen laut Ihrem Vorgesetzten allerdings nur 1.000
zufällige Konten unter den 10 Millionen Konten ausgewählt werden und von diesen der
durchschnittliche Kontostand ermittelt werden. Verwenden Sie hierzu die in Aufgabe 1
erwähnte randint-Funktion. Ermitteln Sie auch hier wieder die für diese Aufgabe benötigte Zeit und
geben Sie diese am Ende auf der Konsole aus.
"""

import random
import time

kontostand = []

time_start = time.time()

for x in range(10_000_000):
    kontostand.append(random.randint(-10_000, 100_000))


average_start = time.time()
average = 0
for x in range(10_000):
    average += kontostand[random.randint(0, len(kontostand) - 1)]
average_end = time.time()
print("Average is: ", average / 10_000)
print("Average Calculation of 1000 random people took: ", average_end - average_start, " Seconds")


time_end = time.time()
print("The operation took: ", time_end - time_start, " Seconds")
