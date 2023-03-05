"""
Algorithmik

Bei einem Badmintonturnier sollen fünf Spieler im FFA-Modus (jeder gegen jeden) gegeneinander
antreten. Bei 5 Teilnehmern (Spieler 1, Spieler 2, Spieler 3, Spieler 4, Spieler 5) gibt es also folgende
Spielkonstellationen…

- Spieler 1 vs. Spieler 2
- Spieler 1 vs. Spieler 3
- Spieler 1 vs. Spieler 4
- Spieler 1 vs. Spieler 5
- Spieler 2 vs. Spieler 3
- Spieler 2 vs. Spieler 4
- Spieler 2 vs. Spieler 5
- Spieler 3 vs. Spieler 4
- Spieler 3 vs. Spieler 5
- Spieler 4 vs. Spieler 5

…oder in Form einer 2D-Liste ausgedrückt…
[[1,2], [1,3], [1,4], [1,5], [2,3], [2,4], [2,5], [3,4], [3,5], [4,5]]

Schreiben Sie eine Funktion erstelleSpielkonstellationen(spielerzahl), welche abhängig von der als
Parameter übergebenen Spielerzahl alle möglichen Spielkonstellationen in eine 2D-Liste schreibt
(analog zum Beispiel oben). Nutzen Sie zum Lösen der Aufgabe…

a - zwei Schleifen.
"""


def erstelleSpielkonstellationen(spielerzahl):
    aux = []
    for x in range(1, spielerzahl + 1):
        for y in range(x + 1, spielerzahl + 1):
            aux.append([x, y])
    return aux


print(erstelleSpielkonstellationen(5))
