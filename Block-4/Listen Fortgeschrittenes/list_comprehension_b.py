""""
List Comprehension

Erstellen Sie eine Liste, welche... alle Zahlen zwischen –50 und +50 enthält, welche durch 2 und 3 teilbar sind
"""


# variation 1
liste_v1 = []
for n in range(-50, 51):
    if n % 6 == 0:
        liste_v1.append(n)

print("Liste V1: ", liste_v1)


## variation 2
liste_v2 = []
for n in range(-48, 51, 6):
    liste_v2.append(n)

print("Liste V2: ", liste_v2)


## variation 3
liste_v3 = [n for n in range(-50, 51) if n % 6 == 0]
print("Liste V3: ", liste_v3)


## variation 4
liste_v4 = [n for n in range(-48, 50, 6)]
print("Liste V4: ", liste_v4)
