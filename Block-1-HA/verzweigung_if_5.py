"""
Aufgabe 5:

Schreiben Sie ein Programm, das zwei Zahlen einliest. Anschließend soll vom Benutzer eingegeben
werden, was mit diesen beiden Zahlen gemacht werden soll:
- (1) Addition
- (2) Subtraktion
- (3) Multiplikation
- (4) „normale Division“
- (5) ganzzahlige Division
- (6) Modulo
- (7) Hoch
- (sonst) Fehler
Das Ergebnis ist am Ende auszugeben
"""

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
opt = int(input("Option:"))
res = 0

match opt:
    case 1:
        res =  num1 + num2
    case 2:
        res = num1 - num2
    case 3:
        res = num1 * num2
    case 4:
        if num2 == 0:
            print("cant divide by 0...")
            exit()
        res = num1 / num2
    case 5:
        if num2 == 0:
            print("cant divide by 0...")
            exit()
        res = num1 // num2
    case 6:
        if num2 == 0:
            print("cant divide by 0...")
            exit()
        res = num1 % num2
    case 7:
        res = num1 ^ num2
    case _:
        print("no correct option selected...")
        exit()

print("res: " + str(res))
