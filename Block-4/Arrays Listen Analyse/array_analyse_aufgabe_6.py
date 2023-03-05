""""
Aufgabe 6:

Erklären Sie, wieso es einen Unterschied macht, ob Sie…

- 1.000mal je ein Element vorne in eine Liste mit 10 Millionen Elementen einfügen
- einmal 1.000 Elemente gleichzeitig vorne in eine Liste mit 10 Millionen Elementen einfügen

Demonstrieren Sie den Unterschied in einem Code-Beispiel.
"""

import random
import time

kontostand = []

time_start = time.time()

for x in range(10_000_000):
    kontostand.append(random.randint(-10_000, 100_000))

add_start = time.time()
for x in range(1_000):
    kontostand.insert(0, 0)
add_end = time.time()
print("Time adding 1000 values individually at the beginning: ", add_end - add_start, " seconds")


grouped_values = []
for x in range(1_000):
    grouped_values.append(0)

add_start = time.time()
new_array = [*grouped_values, *kontostand]
add_end = time.time()
print("Time adding 1000 all together at the beginning: ", add_end - add_start, " seconds - length: ", len(new_array))

time_end = time.time()

print("The operation took: ", time_end - time_start, " Seconds")
