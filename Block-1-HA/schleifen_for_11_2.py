"""
Aufgabe 11 – Verschachtelte Schleifen

Lösen Sie die beiden Aufgaben mit dem Namen „Verschachtelte Schleifen“ auf dem Übungsblatt zu while-Schleifen
mit for-Schleifen.

Aufgabe 8 – Verschachtelte Schleifen
"""

print("Square printer...")

width = int(input("Enter width: "))
height = int(input("Enter height: "))

for vheight in range(height, 0, -1):
    for vwidth in range(width, 0, -1):
        if vwidth == 1 or vwidth == width or vheight == 1 or vheight == height:
            print("x", end="")
        else:
            print(" ", end="")
    print("\n", end="")

