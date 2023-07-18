'''
Aufgabe 4:
Sowohl der im Unterricht besprochene ImprovedBubbleSort-Sortieralgorithmus als auch der
verbreitete MergeSort-Sortieralgorithmus verdanken ihre Geschwindigkeitsgewinne dem schnellen
Zusammenfügen („mergen“) von zwei bereits vorsortierten Listen in eine sortierte Liste. Schreiben
Sie daher eine Funktion merge(list1,list2), welche zwei sortierte Listen entgegennimmt, und diese
beiden Listen zusammenführt in eine einzelne sortierte Liste.
'''
import random


def create_ordered_list():
    new_list = []
    for i in range(100):
        new_list.append(random.randint(0, 100))
    return sorted(new_list)


def merge(list1: list, list2: list):
    i = j = iterations = 0
    new_list = []
    while i <= len(list1) or j <= len(list2):
        iterations += 1
        if i > len(list1) - 1:
            new_list.extend(list2[j:])
            break
        if j > len(list2) - 1:
            new_list.extend(list1[i:])
            break
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    return [
        iterations,
        new_list,
        ]


first_list = create_ordered_list()
second_list = create_ordered_list()
total_elements = len(first_list) + len(second_list)
res = merge(
    first_list,
    second_list
    )
iters = res[0]
merged_list = res[1]
print("Merging two list of " + str(total_elements) + " elements")
print("Took " + str(iters) + " iterations")
print("Merged list: " + str(merged_list))
