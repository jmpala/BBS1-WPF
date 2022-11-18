"""
Aufgabe 2:

Erstellen Sie ein Programm, welches zwei Zahlen einliest. Es dürfen nur positive Zahlen oder 0
eingegeben werden – wird eine negative eingegeben, so soll eine Fehlermeldung ausgegeben
werden.
Die größere der beiden Zahlen ist nun durch die kleinere zu teilen. Anschließend soll der Quotient
ausgegeben werden.
Beachten Sie, dass man durch 0 nicht teilen kann. In diesem Fall muss ebenfalls eine Fehlermeldung
ausgegeben werden
"""

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

maxnum = num1 if num1 > num2 else num2
minnum = num1 if num1 < num2 else num2

if minnum == 0:
    print("Cant divide by 0")
    exit()

print("result: " + str(maxnum / minnum))
