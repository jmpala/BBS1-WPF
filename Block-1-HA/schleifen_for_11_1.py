"""
Aufgabe 11 – Verschachtelte Schleifen

Lösen Sie die beiden Aufgaben mit dem Namen „Verschachtelte Schleifen“ auf dem Übungsblatt zu while-Schleifen
mit for-Schleifen.

Aufgabe 7 – Verschachtelte Schleifen
"""

print("Square printer...")

width = int(input("Enter width: "))
height = int(input("Enter height: "))

for vheight in range(height, 0, -1):
    for vwidth in range(width, 0, -1):
        print("x", end="")
    print("\n", end="")

