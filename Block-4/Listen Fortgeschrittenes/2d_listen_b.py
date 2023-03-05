""""
2D-Listen

Erstellen Sie eine 2D-Liste mit den Dimensionen 4x4, bei der jedes Element die Summe aus seinem
Spaltenindex und seinem Reihenindex ist. Die Liste soll also so aussehen:

[[0,1,2,3],[1,2,3,4],[2,3,4,5][3,4,5,6]]

b - (eine oder zwei) gewöhnliche for-Schleifen verwenden.
"""

liste = []

for x in range(4):
    aux_liste = []
    for y in range(x, x + 4):
        aux_liste.append(y)
    liste.append(aux_liste)

print(liste)
