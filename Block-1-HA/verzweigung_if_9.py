"""
Aufgabe 9:

a) Das Programm soll den Benutzer zu Beginn nach m und b, also der Steigung und dem y-Achsenabschnitt einer
linearen Funktion fragen. Anschließend gibt das Programm die Funktionsgleichung einer linearen Funktion mit den
angegebenen Parametern aus.

b) Das Programm soll nun den Nutzer fragen, ob… …er anschließend einen x-Wert angeben möchte, um vom Programm
den dazugehörigen Funktionswert zu erhalten (Eingabe „X“) oder …ob er anschließend einen Funktionswert angeben möchte,
um vom Programm den dazugehörigen x-Wert zu erhalten (Eingabe „Y“). Falls die Eingabe weder „X“ noch „Y“ ist, wird das
Programm direkt beendet. Nun gibt der Nutzer… …im Fall der Eingabe „X“ einen x-Wert ein und das Programm gibt daraufhin
den zugehörigen Funktionswert aus oder …im Falle der Eingabe „Y“ einen Funktionswert ein und das Programm gibt
daraufhin den zugehörigen x-Wert aus.

c) Das Programm aus Aufgabe 1b soll erweitert werden. Es soll eine dritte Eingabemöglichkeit „N“ geben, bei der das
Programm die Nullstelle der eingegebenen linearen Funktion berechnet und ausgibt.
"""


def solve_x_for_function(function, x):
    m = function[0]
    b = function[1]
    return m * x + b


def solve_y_for_function(function, y):
    m = function[0]
    b = function[1]
    return (y - b) / m


def solve_for_zero(function):
    m = function[0]
    b = function[1]
    return (0 - b) / m



print("f(x)=mx+b")
inpM = float(input("Give m..."))
inpB = float(input("Give b..."))

pair = [inpM, inpB]

print("Your linear equation is: f(x)={}x{}"
      .format(inpM,
              "+{}".format(inpB) if inpB >= 0 else "{}".format(inpB)))

is_solveX = False

solve_for = str(input("Enter X or Y to solve the equation or N to find the Zero of f(x)..."))


if solve_for.lower() == "x":
    inpX = float(input("Input x value..."))
    res = solve_x_for_function(pair, inpX)
    print("y = {}({}) + {} = {}".format(inpM, inpX, inpB, res))
elif solve_for.lower() == "y":
    inpY = float(input("Input y value..."))
    res = solve_y_for_function(pair, inpY)
    print("x = ({} - {}) / {} = {}".format(inpY, inpB, inpM, res))
elif solve_for.lower() == "n":
    if inpM == 0:
        print("This is a parallel line to x axis in y = {}, has no zero...".format(inpB))
        exit()
    res = solve_for_zero(pair)
    print("The Zero of x = (0 - {}) / {} is {}".format(inpB, inpM, res))
else:
    print("No correct option selected, terminating program")
