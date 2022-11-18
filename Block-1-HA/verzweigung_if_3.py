"""
Aufgabe 3:

Das geforderte Programm liest vom Benutzer vier Zahlen ein.
Im Anschluss soll von den vier eingegebenen Zahlen die größte
und die kleinste Niederschlagsmenge ausgegeben werden.
"""

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
num4 = int(input("Enter number 4:"))

nums = [num1, num2, num3, num4]
min = num1
max = num1

for num in nums:
    min = min if min < num else num
    max = max if max > num else num

print("Min: " + str(min))
print("Max: " + str(max))
