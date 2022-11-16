"""
Aufgabe 12 – Verschachtelte Schleifen

Gegeben sind zwei Listen:
adjektive=["rote","gelbe","grüne","blaue","große","kleine"]
fruechte=["Äpfel","Bananen","Birnen","Grapefruits","Kaktusfeige"]

Geben Sie mithilfe verschachtelter Schleifen jede Kombinationsmöglichkeit von Elementen der ersten mit Elementen
der zweiten Liste aus. Es sollen jedoch nur solche Kombinationen ausgegeben werden, bei denen das Adjektiv weniger
Buchstaben hat als die Frucht, und bei denen das Adjektiv einen anderen Anfangsbuchstaben hat als die Frucht.

Beispiel: Ausgegeben werden sollen Kombinationen wie „Rote Äpfel", „grüne Kaktusfeigen", usw. Nicht ausgegeben werden
sollen Kombinationen wie „Gelbe Äpfel", „Blaue Bananen", usw.
"""

adjektive = ["rote", "gelbe", "grüne", "blaue", "große", "kleine"]
fruechte = ["Äpfel", "Bananen", "Birnen", "Grapefruits", "Kaktusfeige"]

for adj in adjektive:
    for fru in fruechte:
        if len(adj) < len(fru):
            print(adj + ' ' + fru)
