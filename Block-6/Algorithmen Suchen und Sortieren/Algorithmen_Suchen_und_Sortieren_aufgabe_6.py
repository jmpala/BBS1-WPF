'''
Aufgabe 6:
Implementieren Sie MergeSort und sortieren Sie die in A1 erstellte Liste.
Messen Sie, wie viel Zeit der Algorithmus in Anspruch nimmt.
Spielen Sie mit unterschiedlichen Listenlängen herum und beschreiben Sie, wie sich die Laufzeit in
Abhängigkeit von der Listenlänge verhält.
'''
import math
import numpy as np


def create_list_from_file() -> list:
    with open("list.txt", "r") as file:
        return [int(line) for line in file]


def divide_list_into_two(list_to_divide: list, iterations: int = 0) -> list:
    iterations += 1
    # if list is empty or has only one element, return list
    if len(list_to_divide) <= 1:
        return [
            iterations,
            list_to_divide
            ]
    middle = len(list_to_divide) // 2
    # divide list into two lists
    left_res = divide_list_into_two(list_to_divide[:middle], iterations)
    left_iter = left_res[0]
    left = left_res[1]
    right_res = divide_list_into_two(list_to_divide[middle:], iterations)
    right_iter = right_res[0]
    right = right_res[1]
    return merge(left, right, left_iter + right_iter)


def merge(list1: list, list2: list, iterations: int = 0) -> list:
    i = j = 0
    merged = []
    while i < len(list1) and j < len(list2):
        iterations += 0
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return [
        iterations,
        merged
        ]


# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_list = create_list_from_file()
print(divide_list_into_two(test_list))
