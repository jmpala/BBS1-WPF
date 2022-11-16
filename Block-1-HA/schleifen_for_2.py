"""
Aufgabe 2 – Wiederholte Begrüßung

Das Programm soll den Benutzer auffordern einzugeben, wie oft er begrüßt werden möchte. Das Programm soll
ihn anschließend entsprechend oft mit „Hallo“ begrüßen.
"""

num = int(input("Enter a number to repeat a salute that many times..."))

for x in range(1, num + 1):
    print("Hello!")
