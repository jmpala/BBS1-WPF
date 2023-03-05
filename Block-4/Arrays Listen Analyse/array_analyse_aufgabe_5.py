""""
Aufgabe 5:

Sie haben nun insgesamt acht unterschiedliche Zeitangaben für die unterschiedlichen Aufgaben
ermittelt.
Versuchen Sie zu erklären, wie die höchst unterschiedlichen Zeitspannen zustande kommen könnten
und wovon diese Zeitspannen genau abhängen.
Spielen Sie hierzu ruhig noch mit anderen Listengrößen herum (es müssen nicht zwangsläufig 10
Millionen Konten sein oder Operationen, die mit 1.000 Datensätzen gleichzeitig arbeiten).
"""

"""
Answer

In this section we are experimenting with the "O Notation". An algorithm can not be measured in time, if not
in steps that takes to it completeness, because not all the computers executes a program on the same deterministic
way. Also and more important, algorithms do not scale on time, they scale on the amount of data that needs to run
though the algorithm.

In case of the Array/List, we have the following measurement for each of its operations:

- all read by index operations are O(1) "constant time"
- all modify by index operations are O(1) "constant time"
- add a value at the end O(1) "constant time"
- remove a value at the end O(1) "constant time"
- inserting a new value at index different than the end O(N) "Linear Time"
- deleting a value at index different than the end O(N) "Linear Time"
- searching a value O(N) "Linear Time"

"""