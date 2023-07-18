'''
Aufgabe 3:
Erstellen Sie eine Liste numbers_unsorted, welche aus 10.000 zufälligen Zahlen zwischen 0 und
1.000.000.000 besteht.
Erstellen Sie eine Liste numbers_searched, welche aus 10.000 zufälligen Zahlen zwischen 0 und
1.000.000.000 besteht.
Ermitteln Sie, wie viele Zahlen aus letzterer Liste auch in ersterer Liste vorkommen
'''
import random


def create_list():
    new_list = []
    for i in range(10000):
        new_list.append(random.randint(0, 1000000000))
    new_list.append(1)
    return new_list


def lists_intersection(list1: list, list2: list):
    iterations = 0
    intersection = []
    for list1_item in list1:
        iterations += 1
        for list2_item in list2:
            iterations += 1
            if list1_item == list2_item:
                intersection.append(list1_item)
    return [
        iterations,
        intersection,
        ]


numbers_unsorted = create_list()
numbers_searched = create_list()
res = lists_intersection(numbers_unsorted, numbers_searched)
iterations = res[0]
intersection = res[1]
print("Intersection of " + str(len(numbers_unsorted)) + " and " + str(len(numbers_searched)) + " elements")
print("Took " + str(iterations) + " iterations")
print("Intersection: " + str(intersection))
