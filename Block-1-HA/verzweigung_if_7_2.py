"""
Aufgabe 7:

Um von Mainz nach Wiesbaden und zurück zu gelangen,fährt manmit der Bahnlinie S8.

- Eine Fahrt kostet(ohneBahncard) 5€.
- Eine Bahncard 50 (50% Preisreduzierungauf alle Karten für ein Jahr) kostet 200€.
- Eine Bahncard 25 (25% Preisreduzierungauf alle Karten für ein Jahr) kostet 50€.

Das Programm erfragt zu Beginn,
wie viele Fahrten von Mainz nach Wiesbaden und zurück der Benutzer im nächsten Jahr plant.Das Programm berechnet nun,
wie viel Euro entsprechend viele Fahrten mit allen drei Optionen (keine Bahncard, Bahncard 25, Bahncard 50) kosten und
gibt die drei Ergebnisse in Textform aus (z.B. „2 Fahrten kosten ohne Bahncard 10€, mit Bahncard 25 57,50€ und mit
Bahncard 50 205,00€.“).In einer abschließenden Ausgabe hält das Programm fest, welche der drei Alternativen für die
gewählte Anzahl Fahrten die beste ist (z.B. „Für die gewählten 2 Fahrten ist weder der Kauf einer Bahncard 50 noch
einer Bahncard 25 sinnvoll.“).
"""

inp = int(input("Give the numbers of travels: "))

ticket = 5

total = total_25 = total_50 = 0

total = ticket * inp
total_25 = total * 0.75 + 50
total_50 = total * 0.50 + 200

options = [
    [total, "Normal Rate"],
    [total_25, "Card 25"],
    [total_50, "Card 50"]
]

bestOpt = options[0]
for opt in options:
    if opt[0] < bestOpt[0]:
        bestOpt = opt

print("{} is the best option and cost {}".format(bestOpt[1], bestOpt[0]))
