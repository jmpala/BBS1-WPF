'''
Aufgabe 8:
Geben Sie die O-Notation für die einzelnen Algorithmen an und erklären Sie Ihre Antworten
detailliert!

Bubble Sort O(n^2)
- is build of two for-structures with n iterations
- both will always be traverse fully, dow n * n = n^2

Improved Bubble Sort O(n^2)
- it is the same as the bubble sort
- it only traverse the hole for-structures, till there is no "swap"
- a swap happens when 2 values change their indexes
- it will only be fully traversed when the list reverse ordered is
- the tendency is still O(n^2)

Merge Sort O(n*log(n))
- divide and conquer principle
- it is easily implemented with recursions
- it builds a tree-like structure till only one value per node is left
- the division is made by halving in two the list and it`s sub-lists
- then it merge everything together
- merge is fast because the nodes are already ordered

Binary Search O(log(n))
- divide and conquer principle
- it is easily implemented with recursions
- it works on an ordered list
- it divides the list into two and selects the set that may contain the searched value
- repeat till only one value is left and compare it to the search term

'''