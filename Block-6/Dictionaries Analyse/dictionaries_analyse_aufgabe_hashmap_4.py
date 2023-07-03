'''
Aufgabe 4:
Nun wollen wir für jedes Wort in Ihrem Text (also im words-Array) schauen, ob sich dieses im
importierten englischen Vokabular befindet. Mit zwei Zählvariablen wollen wir zählen, wie viele der
Worte Ihres Textes im englischen Vokabular enthalten sind und wie viele nicht.

Nun ist es so, dass wir das importierte englische Vokabular ja nicht nur einmal, sondern gleich
dreimal vorliegen haben – einmal als Set, einmal als Dictionary und einmal in Form einer Liste.
Lösen Sie Aufgabe 4 also einmal separat für jede Datenstruktur.

Verwenden Sie anschließend die time-Bibliothek (Anwendungsbeispiele wurden zusammen im
Unterricht erarbeitet und sind auf Teams hochgeladen), um zu messen, welches Ihrer drei
Programme am schnellsten läuft.
'''
import time

from english_words import get_english_words_set

english_words_set = get_english_words_set(['web2'])
english_words_dictionary = dict.fromkeys(english_words_set, 0)
english_words_list = list(english_words_set)

try:
    f = open('./book.txt', 'r')
    content = f.read()
except Exception:
    print("Error opening file...")
    exit(-1)
finally:
    f.close()

book_words = content.split()
print("Total words on book: ", len(book_words))

words_set = set(book_words)
words_list = list(words_set)
words_list.sort()
print("Total unique words: ", len(words_list))

total_matches = 0
iterations = 0

start = time.time()
for word in words_list:
    if english_words_dictionary.get(word) is not None:
        total_matches += 1
end = time.time()

print("Total matched words: ", total_matches)
print("Lasted ", str(end - start), " seconds...")
