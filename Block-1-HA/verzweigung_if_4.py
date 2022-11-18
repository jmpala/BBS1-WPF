"""
Aufgabe 4:

Schreiben Sie ein Programm, dass drei vom Benutzer eingegebene Zahlen aufsteigend, der Größe
nach ausgibt.

"""


def order(array):
    for x in range(0, len(array)):
        for y in range(x+1, len(array)):
            if array[x] > array[y]:
                aux = array[y]
                array[y] = array[x]
                array[x] = aux


num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))

nums = [num1, num2, num3]

order(nums)

print(nums)