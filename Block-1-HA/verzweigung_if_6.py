"""
Aufgabe 6:

Schreiben Sie ein Programm, das für eine eingegebene Jahreszahl eingibt, ob es sich dabei um ein
Schaltjahr handelt.
Ein Jahr ist ein Schaltjahr, wenn es ein Vielfaches von 4 ist.
Wenn es allerdings ein Vielfaches von 100 ist, ist es wiederum doch kein Schaltjahr.
Und wenn es nun zusätzlich auch ein Vielfaches von 400 ist, ist es doch wieder eins
"""

year = int(input("Insert a year: "))

is_leap = False

if year % 4 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 400 == 0:
    is_leap = True
else:
    is_leap = False

if is_leap:
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")
