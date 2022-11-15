"""
Aufgabe 7 – Verschachtelte Schleifen

Das Programm soll vom Benutzer zwei Zahlen „breite“ und „hoehe“ einlesen. Anschließend soll das Programm mit dem
Buchstaben „X“ ein Rechteck ausgeben, welches die vom Benutzer eingegebene Breite und Höhe hat.
"""

print("Square printer...")

width = int(input("Enter width: "))
height = int(input("Enter height: "))

while height > 0:
    temp_width = width

    while temp_width > 0:
        print("x", end="")
        temp_width -= 1

    print("\n", end="")
    height -= 1
