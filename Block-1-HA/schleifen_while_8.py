"""
Aufgabe 8 – Verschachtelte Schleifen

Das Programm soll vom Benutzer zwei Zahlen „breite“ und „hoehe“ einlesen. Anschließend soll das Programm mit dem
Buchstaben „X“ ein hohles / nicht ausgefülltes Rechteck ausgeben, welches die vom Benutzer eingegebene Breite und
Höhe hat.
"""

print("Square printer not filled...")

width = int(input("Enter width: "))
height = int(input("Enter height: "))

temp_height = height
while temp_height > 0:
    temp_width = width

    while temp_width > 0:
        if temp_width == 1 or temp_width == width or temp_height == 1 or temp_height == height:
            print("x", end="")
        else:
            print(" ", end="")
        temp_width -= 1

    print("\n", end="")
    temp_height -= 1
