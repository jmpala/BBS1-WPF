'''
Aufgabe 7:
Erstellen Sie eine Liste numbers_sorted, welche aus 10.000 zufälligen Zahlen zwischen 0 und
1.000.000.000 besteht.
Erstellen Sie eine Liste numbers_searched, welche aus 10.000 zufälligen Zahlen zwischen 0 und
1.000.000.000 besteht.
Ermitteln Sie mithilfe von BinarySearch, wie viele Zahlen aus letzterer Liste auch in ersterer Liste
vorkommen.
'''


def create_list_from_file() -> list:
    with open("list.txt", "r") as file:
        return [int(line) for line in file]


def binary_search(needle: int, haystack: list) -> list:
    iterations = 0
    c_haystack = haystack.copy()
    while len(c_haystack) > 1:
        iterations += 1
        middle = len(c_haystack) // 2
        if needle < c_haystack[middle]:
            c_haystack = c_haystack[:middle]
        else:
            c_haystack = c_haystack[middle:]
    return [
        iterations,
        c_haystack.pop() == needle
        ]


# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_list = create_list_from_file()
print(binary_search(999916955, test_list))
