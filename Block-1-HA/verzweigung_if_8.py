"""
Aufgabe 8:

Das Programm soll zu Beginn die Parametern a, b und c einer
quadratischen Funktion der Form f(x)=ax²+bx+c erfragen.
Anschließend berechnet es mithilfe der PQ-Formel (mögliche)
Nullstellen von f.
Zu beachten ist, dass für a nicht 0 eingegeben werden darf,
da f dann keine quadratische Funktion wäre.
Ebenso kann eine quadratische Funktion entweder keine oder eine oder zwei Nullstellen haben. Die
verschiedenen Fälle sind zu berücksichtigen.
"""
import cmath


def pq_formel(a, b, c):#
    zero_1 = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    zero_2 = (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return [zero_1, zero_2]


inpA = float(input("a:"))

if inpA == 0:
    print("A can't be 0")
    exit(-1)

inpB = float(input("b:"))
inpC = float(input("c:"))

print(pq_formel(inpA, inpB, inpC))
