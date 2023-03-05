""""
2D-Listen

Erstellen Sie eine 2D-Liste mit den Dimensionen 4x4, bei der jedes Element die Summe aus seinem
Spaltenindex und seinem Reihenindex ist. Die Liste soll also so aussehen:

[[0,1,2,3],[1,2,3,4],[2,3,4,5][3,4,5,6]]

d - List Comprehension mit einer Schleife verwenden.
"""

liste = [[0 + x, 1 + x, 2 + x, 3 + x] for x in range(4)]

print(liste)
