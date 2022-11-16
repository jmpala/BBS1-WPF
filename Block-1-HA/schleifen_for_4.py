"""
Aufgabe 4 – Zahlenfolgen rückwärts ausgeben

Das Programm soll den Benutzer auffordern eine Ganzzahl „n“ einzugeben. Anschließend soll das
Programm alle natürlichen Zahlen von n bis 1 nacheinander ausgeben.
"""

num = int(input("Enter a number to count down to 1..."))

for x in range(num, 1 - 1, -1):
    print(x)
