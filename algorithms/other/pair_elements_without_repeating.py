"""
This algorith pairs elements of a list without repeating them
"""


def pair_values_of_list(liste):
    length = len(liste)
    start_l1 = 0
    start_l2 = 0
    while start_l1 < length:
        while start_l2 < length:
            print(liste[start_l1], " ", liste[start_l2])
            start_l2 += 1
        start_l1 += 1
        start_l2 = start_l1 + 1


pair_values_of_list(["s1", "s2", "s3", "s4"])
