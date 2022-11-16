"""
Aufgabe 3 – Zahlenfolgen ausgeben

Das Programm soll den Benutzer auffordern eine Ganzzahl „n“ einzugeben.
Anschließend soll das Programm alle natürlichen Zahlen von 1 bis n nacheinander ausgeben.
"""

num = int(input("Enter a number to count from +1 to it.."))

for x in range(1, num + 1):
    print(x)
