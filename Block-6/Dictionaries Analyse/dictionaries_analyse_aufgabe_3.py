'''
Aufgabe 3:
Erstellen Sie eine Variable namens text, die einen längeren Text Ihrer Wahl speichert (mindestens
500 Wörter). Der Text darf ruhig komplex sein und Fremdwörter enthalten, die vermutlich nicht in
dem von uns importierten Vokabular vorkommen.
Strings können Sie übrigens über mehrere Codezeilen strecken, indem Sie diese in dreifache
Anführungszeichen setzen.
text = “““Hier könnte
ein ganz langer
Text stehen.“““
Da wir in der nächsten Aufgabe alle Worte in dem von Ihnen gewählten Text im Vokabular
nachschlagen wollen, müssen wir die einzelnen Worte Ihres Textes in ein Array packen. Das
funktioniert so:
words = text.split()
Nun liegt der von Ihnen gewählte Text in Array- bzw. Listenform vor – lassen Sie sich den Inhalt der
beiden Variablen ruhig einmal auf der Konsole ausgeben, um sie sich zu visualisieren.
'''

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
