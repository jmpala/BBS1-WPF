"""
Aufgabe 1:

Schreiben Sie ein Programm, welches eine Ganzzahl einliest und anschließend den Namen der
entsprechenden Note ausgibt.
Wird bspw. eine 1 eingegeben, soll das Programm „sehr gut“ ausgeben. Wird bspw. eine 2
eingegeben, soll das Programm „gut“ ausgeben usw. Falls eine Zahl <1 oder eine Zahl >6 eingegeben
wird, soll eine Fehlermeldung ausgegeben werden.
"""

grade = int(input("Insert grade:"))

if grade == 1:
    print("Sehr gut")
elif grade == 2:
    print("gut")
else:
    print("no valid grade")
