""""
Aufgabe 2:

Sie arbeiten in der Steuerverwaltung von Griechenland und haben nun
eine Liste der Kontostände aller 10 Millionen Griechen (aus Aufgabe 1).
Sie erhalten von Ihrem Vorgesetzten den Auftrag…

- die 1.000 ersten Kontostände der Liste zu löschen,
da die 1.000 dazugehörigen Griechen mittlerweile verstorben sind
- die 1.000 letzten Kontostände der Liste zu löschen,
da die 1.000 dazugehörigen Griechen mittlerweile die griechische Staatsbürgerschaft
abgegeben haben
- die 1.000 Kontostände genau aus der Mitte der Liste zu löschen, da die 1.000 dazugehörigen
Griechen kein Konto mehr verwenden wollen („Bargeld ftw!“)

Führen Sie die Anweisungen Ihres Vorgesetzten aus und messen Sie für jeden der drei Aufgaben die
Zeit, die diese in Anspruch genommen hat. Geben Sie diese schlussendlich auf der Konsole aus.
"""

import random
import time

kontostand = []

time_start = time.time()

for x in range(10_000_000):
    kontostand.append(random.randint(-10_000, 100_000))


remove_start = time.time()
for x in range(10_000):
    kontostand.pop(0)
remove_end = time.time()
print("The remove 1000 from beginning operation took: ", remove_end - remove_start, " Seconds")


remove_start = time.time()
for x in range(10_000):
    kontostand.pop()
remove_end = time.time()
print("The remove 1000 from the end operation took: ", remove_end - remove_start, " Seconds")


remove_start = time.time()
for x in range(10_000):
    kontostand.pop(len(kontostand)//2)
remove_end = time.time()
print("The remove 1000 from the middle operation took: ", remove_end - remove_start, " Seconds")


time_end = time.time()
print("The operation took: ", time_end - time_start, " Seconds")
