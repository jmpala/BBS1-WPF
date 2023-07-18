'''
Aufgabe 5:
Implementieren Sie ImprovedBubbleSort – den verbesserten BubbleSort-Algorithmus, der im
Unterricht besprochen wurde – und sortieren Sie die in A1 erstellte Liste.
Messen Sie, wie viel Zeit der Algorithmus in Anspruch nimmt.
Spielen Sie mit unterschiedlichen Listenlängen herum und beschreiben Sie, wie sich die Laufzeit in
Abhängigkeit von der Listenlänge verhält
'''


def create_list_from_file() -> list:
    with open("list.txt", "r") as file:
        return [int(line) for line in file]


def improved_bubble_sort(unsorted_list: list) -> list:
    iterations = 0
    new_list = unsorted_list.copy()
    for i in range(len(new_list) - 1):
        swap = False
        iterations += 1
        for j in range(len(new_list) - 1):
            iterations += 1
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
                swap = True
        if not swap:
            break
    return [
        iterations,
        new_list
        ]


unordered_list = create_list_from_file()
res = improved_bubble_sort(unordered_list)
inters = res[0]
ordered_list = res[1]
print("Improved Bubblesort of " + str(len(unordered_list)) + " elements")
print("Took " + str(inters) + " iterations")
