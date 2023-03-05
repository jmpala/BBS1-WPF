""""
List Comprehension

Erstellen Sie eine Liste, welche... die Funktionswerte der Funktion f(x)=2x²-4x+6 für alle ganzzahligen x für –5 <= x <= 5
enthält.
"""


def cuadratic(x):
    return 2 * x ** 2 - 4 * x + 6


# variation 1
liste_v1 = []
for n in range(-5, 6):
    liste_v1.append(cuadratic(n))

print("Liste V1: ", liste_v1)


## variation 2
liste_v2 = [cuadratic(n) for n in range(-5, 6)]

print("Liste V2: ", liste_v2)
