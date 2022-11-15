"""
Aufgabe 2 – Wiederholte Begrüßung
Das Programm soll den Benutzer auffordern einzugeben, wie oft er begrüßt werden möchte.
Das Programm soll ihn anschließend entsprechend oft mit „Hallo“ begrüßen.
"""

num = 0
limit = int(input("Loop how many times?"))

while num < limit:
    print(str(num+1) + ". Hallo")
    num += 1
