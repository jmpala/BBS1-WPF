""""
2D-Listen

Erstellen Sie eine 2D-Liste mit den Dimensionen 4x4, bei der jedes Element die Summe aus seinem
Spaltenindex und seinem Reihenindex ist. Die Liste soll also so aussehen:

[[0,1,2,3],[1,2,3,4],[2,3,4,5][3,4,5,6]]

c - List Comprehension mit zwei Schleifen verwenden
"""

liste = [[y for y in range(x, x + 4)] for x in range(4)]

print(liste)
