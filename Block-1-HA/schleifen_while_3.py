"""
Aufgabe 3 – Summieren bis Hundert
Der Benutzer soll vom Programm so lange dazu aufgefordert werden, Zahlen einzugeben,
bis die Summe aller bisher vom Benutzer eingegebenen Zahlen 100 oder größer ist. Nach jeder eingegebenen
Zahl soll die Summe der bisher eingegebenen Zahlen ausgegeben werden.
"""


def ask_number():
    return int(input("Enter number: "))


num = ask_number()

while num < 100:
    print("Your total is: " + str(num))
    num += int(input("Enter number: "))

print("Your number is equal or bigger than 100: " + str(num))



