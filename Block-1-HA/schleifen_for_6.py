"""
Aufgabe 6 – Zahlenfolgen filtern und ausgeben

Das Programm soll den Benutzer auffordern eine Ganzzahl „n“ einzugeben. Anschließend soll das Programm
alle natürlichen Zahlen von 1 bis n ausgeben, die durch 3 teilbar sind. Beispiel: Wenn der Benutzer 6 eingibt,
soll das Programm „3“ und „6“ ausgeben.
"""

num = int(input("Give a number to obtain all the multiples of 3 inbetween..."))

for x in range(1, num + 1):
    if x % 3 == 0:
        print(x)
