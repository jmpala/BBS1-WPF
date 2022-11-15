"""
Aufgabe 5 – Zahlenraten

Das Programm bestimmt zu Beginn eine zufällige Ganzzahl zwischen 0 und 100 – schreiben Sie hierzu zu
Beginn des Programmes „import random“ und weisen Sie dann der Variable „meineZufallszahl“ mit
dem Befehl „meineZufallszahl = random.randint(0,100)“ eine zufällige Zahl zu.

Das Programm soll den Benutzer nun dazu auffordern, die Zahl zu erraten.
- Wenn der Benutzer eine zu kleine Zahl eingibt, soll ihn das Programm darauf hinweisen und eine neue Eingabe verlangen.
- Wenn der Benutzer eine zu große Zahl eingibt, soll ihn das Programm darauf hinweisen und eine neue Eingabe verlangen.
- Wenn der Benutzer eine negative Zahl eingibt, soll sich das Programm beenden.
- Wenn der Benutzer die gesucht Zufallszahl eingibt, soll das Programm gratulieren („GG WP!“) und sich beenden.
"""

import random


def user_input():
    return int(input("Enter a number between 0 and 100: "))


ran = random.randint(0, 100)

print("Guest the random number...")

# Game Loop
while True:
    guess = user_input()
    if (guess < 0):
        break;
    elif guess == ran:
        print("GG WP!")
        print("secret number was: " + str(ran))
        break;
    elif guess > ran:
        print("Your guess is higher than the secret number")
    elif guess < ran:
        print("Your guess is lower than the secret number")

print("exiting game...")
