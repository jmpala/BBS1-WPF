'''
Aufgabe 1:
Verwenden Sie pip (den Python-Package-Installer), um ein Package runterzuladen,
welches die häufigsten englischen Worte enthält. Hier bietet sich bspw. das Package
„english-words“ an (enthält die häufigsten 25487 englischen Wörter).
Wir installieren es so (Befehl in Konsole eingeben):
pip install english-words
Das ist schon alles.
In unseren Python-Programmen können wir nun das auf unserem System installierte Package ganz
einfach importieren:
from english_words import english_words_set
Nun haben wir in unserem Programm eine Variable namens english_words_set, welche die
häufigsten 25487 englischen Wörter enthält. Wie wir am Namen erkennen können, liegen diese
jedoch nicht in Form einer Liste oder eines Dictionaries vor, sondern in Form eines Sets.
Ein Set ist, genau wie eine Liste oder ein Dictionary auch, eine Datenstruktur. Ein Set funktioniert
sehr ähnlich wie ein Dictionary – der Unterschied ist, dass wir in Dictionaries „key-value-Paare“
speichern, in Sets jedoch nur eine Menge an keys.
Wir wollen in den nächsten Aufgaben herausfinden, welche Datenstruktur sich am besten eignet, um
schnell Worte nachzuschlagen.
'''

from english_words import get_english_words_set

print(len(get_english_words_set(['web2'])))
