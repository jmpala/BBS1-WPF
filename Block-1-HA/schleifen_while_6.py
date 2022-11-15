"""
Aufgabe 6 – Notenschnitt

Das Programm soll vom Benutzer Schulnoten einlesen und den Notenschnitt aus diesen berechnen. Falls der Benutzer
keine gültige Schulnote (1, 2, 3, 4, 5 oder 6) eingibt, soll ihn daraus Programm darauf hinweisen
(z.B. „keine gültige Schulnote!“). Falls der Benutzer „Ende“ eingibt, soll das Programm aufhören, nach neuen Schulnoten
zu fragen und den Notenschnitt der bisher eingegebenen Noten ausgeben.
"""


def user_input():
    return input("Enter your grade: ")


print("Please enter your grades...")

counter = 0
summ = 0

while True:
    inp = user_input()
    if inp.isalpha() and inp == "end":
        break
    if not inp.isnumeric() or not (1 <= int(inp) <= 6):
        print("No valid grade inputted...")
        continue

    summ += int(inp)
    counter += 1

if counter > 0:
    average = summ / counter
    print("your average is " + str(average))
else:
    print("No grades inputted")
