"""
Aufgabe 10:

Um eine Aussagen über den Verlauf einer quadratischen Funktion f(x)=ax²+bx+c machen zu können, müssen verschiedene
Aspekte betrachtet werden:

- Die Öffnungsrichtung
- Die Stauchung bzw. Streckung
- Die Anzahl der Nullstellen

Schreiben Sie ein Programm, dem der Nutzer zunächst die Werte a, b und c übergibt. Aus den eingegebenen Werten soll
das Programm dann Aussagen über die aufgeführten Eigenschaften machen. Dabei gilt:

Öffnungsrichtung:

- Wenn a positiv ist, ist die Funktion nach oben geöffnet
- Wenn a negativ ist, ist die Funktion nach unten geöffnet

Stauchung bzw. Streckung:

- Wenn der Betrag von a größer als 1 ist, ist die Funktion gestreckt.
- Wenn der Betrag von a kleiner als 1 ist, ist die Funktion gestaucht.

Nullstellen:
Berechnen Sie Q=(b/2a)² - c/a

- Wenn Q größer als 0 ist, hat die Funktion zwei Nullstellen
- Wenn Q 0 ist, hat die Funktion eine Nullstelle
- Wenn Q kleiner als 0 ist, hat die Funktion keine Nullstelle
"""
import cmath


def find_zeros(function):
    a = function[0]
    b = function[1]
    c = function[2]
    zero_1 = (-b + cmath.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    zero_2 = (-b - cmath.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    return [zero_1, zero_2]


def find_amount_of_zeros(function):
    res = find_zeros(function)
    amount = 2
    zero_1 = res[0]
    zero_2 = res[1]
    if zero_1.imag != 0.0:
        amount -= 1
    if zero_2.imag != 0.0:
        amount -= 1
    if zero_1.real == zero_2.real and zero_1.imag == 0.0 and zero_2.imag == 0.0:
        amount = 1
    return amount


inpA = int(input("Insert a..."))
inpB = int(input("Insert b..."))
inpC = int(input("Insert c..."))

func = [inpA, inpB, inpC]

print("Function f(x) = {}x\u00b2 + {}x + {} entered".format(inpA, inpB, inpC))

if inpA == 0:
    print("Function is a parabola on y = {}".format(inpC))

direction = "opens up" if inpA > 0 else "opens down"

# "r" regular / "t" thin / "f" fat
how_open = "regular"

if inpA > 1:
    how_open = "fat"
elif inpA < 1:
    how_open = "thin"

zeros = find_amount_of_zeros(func)

print("The function {}, is {} with {} zeros".format(direction, how_open, zeros))
