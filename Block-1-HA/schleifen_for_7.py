"""
Aufgabe 7 – Zahlenfolgen filtern und aufsummieren

Das Programm soll den Benutzer auffordern eine Ganzzahl „n“ einzugeben. Anschließend soll das Programm alle
geraden natürlichen Zahlen von 1 bis n aufsummieren und die Summe dann auf der Konsole ausgeben. Beispiel:
Wenn der Benutzer 6 eingibt, soll das Programm als Ergebnis 12 ausgeben (weil 2+4+6=12).
"""

num = int(input("Give a number to sum only the evens in between..."))

summe = 0
nums = []
for x in range(1, num + 1):
    if x % 2 == 0:
        summe += x
        nums.append(str(x))

if summe <= 0:
    print("No numbers to sum...")
    print("Exiting program...")
    exit()

print('+'.join(nums) + '=' + str(summe))
