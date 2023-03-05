""""
List Comprehension

Erstellen Sie eine Liste, welche... die Quadratzahlen aller ganzen Zahlen von –9 bis +9 enthält
"""


# variation 1
liste_v1 = []
for n in range(-9, 10):
    liste_v1.append(n ** 2)

print("Liste V1: ", liste_v1)


## variation 2
liste_v2 = [n ** 2 for n in range(-9, 10)]

print("Liste V2: ", liste_v2)
