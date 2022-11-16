"""
Aufgabe 9 – Zahlen multiplizieren

Das Programm soll den Benutzer auffordern eine Ganzzahl „n“ einzugeben. Anschließend soll das Programm alle
natürlichen Zahlen von 1 bis n miteinander multiplizieren (das nennt man auch „die Fakultät bilden“) und das Produkt
dann auf der Konsole ausgeben. Beispiel: Wenn der Benutzer 6 eingibt, soll das Programm als Ergebnis 720 ausgeben
(weil 1*2*3*4*5*6=720).
"""

num = int(input("Give a number to multiply all numbers in between..."))

multi = 1
nums = []
for x in range(1, num + 1):
    multi *= x
    nums.append(str(x))

print('*'.join(nums) + '=' + str(multi))
