"""
Aufgabe 10 – Primzahlermittler

Das Programm soll den Benutzer auffordern eine Ganzzahl „n“ einzugeben. Das Programm soll ermitteln, ob es sich bei
der eingegebenen Zahl um eine Primzahl handelt. Das Programm soll in einem vollständigen Satz antworten, was der
Primzahltest ergeben hat. Beispiel: Wenn n=17 ist, soll das Programm ausgeben „die eingegebene Zahl ist eine Primzahl“.
"""

num = int(input("Give a number to multiply all numbers in between..."))

if num == 2:
    print("this is prime number")

for x in range(3, num + 1, 2):
    if (num % x) == 0 and x < num:
        break
    elif (num % x) != 0 and x < num:
        continue
    else:
        print("this is prime number")

