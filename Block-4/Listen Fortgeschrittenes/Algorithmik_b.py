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

b - …eine Schleife (ja, das geht, wenn man mit den Operatoren % und // umgehen kann)
"""


def getAllGroupVariations(participants: int) -> int:
    return (participants * (participants - 1)) // 2


def zeigeAlleMatchups(spielerzahl: list) -> list:
    new_list = []
    total_elements = len(spielerzahl)
    step = 0

    for i in range(getAllGroupVariations(total_elements)):
        a = (i + getAllGroupVariations(-step)) // total_elements
        b = ((i + 1 + step) + getAllGroupVariations(-a)) % total_elements

        if total_elements - b == 1:
            step += 1

        new_list.append([spielerzahl[a], spielerzahl[b]])

    return new_list


players = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(zeigeAlleMatchups(players))
