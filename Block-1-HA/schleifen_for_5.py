"""
Aufgabe 5 – Zahlenfolgen aufsummieren

Das Programm soll den Benutzer auffordern eine Ganzzahl „n“ einzugeben. Anschließend soll das Programm alle
natürlichen Zahlen von 1 bis n aufsummieren und die Summe dann auf der Konsole ausgeben. Beispiel: Wenn der Benutzer
6 eingibt, soll das Programm als Ergebnis 21 ausgeben (weil 1+2+3+4+5+6=21).
"""

num = int(input("Give a number to sum all natural numbers to the given number..."))

summe = 0

for x in range(1, num + 1):
    summe += x

print("Total Summe:" + str(summe))
