""""
Aufgabe 7:

Geben Sie die O-Notation für die einzelnen Listen-Operationen an und erklären Sie Ihre Antworten
detailliert!

- all read by index operations are O(1) "constant time"
CPUs are really fast fetching data in memory with a known memory address

- all modify by index operations are O(1) "constant time"
CPUs are really fast fetching data in memory with a known memory address

- add a value at the end O(1) "constant time"
CPUs are really fast fetching data in memory with a known memory address

- remove a value at the end O(1) "constant time"
CPUs are really fast fetching data in memory with a known memory address

- inserting a new value at index different than the end O(N) "Linear Time"
Values need to be shifted after the insert N times, worst case scenario the length of the array times

- deleting a value at index different than the end O(N) "Linear Time"
Values need to be shifted after the deletion N times, worst case scenario the length of the array times

- searching a value O(N) "Linear Time"
Hole array in worst case scenario needs to be read

"""