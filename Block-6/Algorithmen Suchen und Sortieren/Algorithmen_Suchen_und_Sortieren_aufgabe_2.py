'''
Aufgabe 2:
Implementieren Sie BubbleSort und sortieren Sie die in A1 erstellte Liste.
Messen Sie, wie viel Zeit der Algorithmus in Anspruch nimmt.
Spielen Sie mit unterschiedlichen Listenlängen herum und beschreiben Sie, wie sich die Laufzeit in
Abhängigkeit von der Listenlänge verhält.
'''
import random


def create_list_from_file() -> list:
    with open("list.txt", "r") as file:
        return [int(line) for line in file]


def bubble_sort(unsorted_list: list) -> list:
    iterations = 0
    new_list = unsorted_list.copy()
    for i in range(len(new_list)):
        iterations += 1
        for j in range(len(new_list) - 1):
            iterations += 1
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    return [
        iterations,
        new_list,
        ]


generated_list = create_list_from_file()
res = bubble_sort(generated_list)
ordered_list = res[1]
iterations = res[0]
print("Bubblesort of " + str(len(generated_list)) + " elements")
print("Took " + str(iterations) + " iterations")
