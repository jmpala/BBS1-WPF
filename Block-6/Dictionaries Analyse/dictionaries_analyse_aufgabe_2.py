'''
Aufgabe 2:
Zunächst einmal wollen wir, um Vergleiche anstellen zu können, das englische Vokabular nicht nur in
unserem Set gespeichert haben, sondern auch noch einmal in Form einer Liste und einmal in Form
eines Dictionaries. Das funktioniert so:
english_words_dictionary = dict.fromkeys(english_words_set,0)
english_words_list = list(english_words_set)
Wir haben nun drei Variablen, english_words_set, english_words_dictionary, english_words_list.
Alle drei enthalten das englische Vokabular (die häufigsten 25k Wörter) – die eine als Set
gespeichert, die andere als Dictionary gespeichert, die letzte als Liste gespeichert.
Machen Sie sich mit den drei Datenstrukturen vertraut, indem Sie bspw. einmal durch diese
durchiterieren und die Elemente ausgeben lassen oder indem Sie nach bestimmten Elementen
suchen (z.B. „the“, „apple“, „qwertzuiopü“...).
'''

from english_words import get_english_words_set

english_words_set = get_english_words_set(['web2'])
english_words_dictionary = dict.fromkeys(english_words_set, 0)
english_words_list = list(english_words_set)

print(len(english_words_set))
print(len(english_words_dictionary))
print(len(english_words_list))

such_begriff = "chair"
if such_begriff in english_words_set:
    print(such_begriff, " is inside the Set")

if english_words_dictionary.get(such_begriff) is not None:
    print(such_begriff, " is inside the Dictionary")

if such_begriff in english_words_list:
    print(such_begriff, " is inside the List")
