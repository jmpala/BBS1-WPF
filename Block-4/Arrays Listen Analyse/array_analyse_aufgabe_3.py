""""
Aufgabe 3:

Sie arbeiten nach wie vor in der Steuerverwaltung von Griechenland und Ihr Vorgesetzter bittet Sie…

- vorne in die kontostand-Liste 1.000 neue Einträge zu erstellen – alle mit dem Kontostand 0,
weil 1.000 Griechen ein neues Konto angelegt haben
- hinten in die kontostand-Liste 1.000 neue Einträge zu erstellen – alle mit dem Kontostand 50,
weil 1.000 Griechen ein Konto bei der DKB eröffnet haben, wo es einen Neukundenbonus
von 50€ gibt :-O
- genau in der Mitte der kontostand-Liste 1.000 neue Einträge zu erstellen – alle mit dem
Kontostand 1.337, denn 1.000 Griechen haben bei der Staatslotterie ein Konto mit
ebendiesem Startbetrag gewonnen

Führen Sie die Anweisungen Ihres Vorgesetzten aus und messen Sie für jeden der drei Aufgaben die
Zeit, die diese in Anspruch genommen hat. Geben Sie diese schlussendlich auf der Konsole aus.
"""

import random
import time

kontostand = []

time_start = time.time()

for x in range(10_000_000):
    kontostand.append(random.randint(-10_000, 100_000))


add_start = time.time()
for x in range(10_000):
    kontostand.insert(0, 0)
add_end = time.time()
print("The Add 1000 at the beginning operation took: ", add_end - add_start, " Seconds")


add_start = time.time()
for x in range(10_000):
    kontostand.append(50)
add_end = time.time()
print("The Add 1000 at the end operation took: ", add_end - add_start, " Seconds")



add_start = time.time()
for x in range(10_000):
    kontostand.insert(len(kontostand) // 2, 1337)
add_end = time.time()
print("The Add 1000 at the middle operation took: ", add_end - add_start, " Seconds")


time_end = time.time()
print("The operation took: ", time_end - time_start, " Seconds")
