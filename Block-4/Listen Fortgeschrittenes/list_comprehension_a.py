""""
List Comprehension

Erstellen Sie eine Liste, welche... alle zweistelligen, geraden, natürlichen Zahlen enthält
"""


# variation 1
liste_v1 = []
for n in range(10, 100):
    if n % 2 == 0:
        liste_v1.append(n)

print("Liste V1: ", liste_v1)


## variation 2
liste_v2 = []
for n in range(10, 100, 2):
    liste_v2.append(n)

print("Liste V2: ", liste_v2)


## variation 3
liste_v3 = [n for n in range(10, 100) if n % 2 == 0]
print("Liste V3: ", liste_v3)


## variation 4
liste_v4 = [n for n in range(10, 100, 2)]
print("Liste V4: ", liste_v4)
