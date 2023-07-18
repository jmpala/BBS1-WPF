'''
Aufgabe 1:
Erstellen Sie eine Liste, welche aus 5.000 zufälligen Zahlen zwischen 0 und 1.000.000.000 besteht
'''
import numpy as np


def create_list_into_file():
    new_list = []
    for i in range(10000):
        new_list.append(np.random.randint(0, 1000000000))
    return sorted(new_list)
    # return new_list


def save_list_into_file():
    with open("list.txt", "w") as file:
        for i in create_list_into_file():
            file.write(str(i) + "\n")


print("Creating list...")
save_list_into_file()
print("Done!")
