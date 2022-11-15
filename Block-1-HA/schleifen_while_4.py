"""
Aufgabe 4 – Hauptstädte der Bundesländer

Das Programm soll den Benutzer wiederholt dazu auffordern, den Namen eines Bundeslandes einzugeben.
- Wenn der Benutzer den Namen eines Bundeslandes eingibt, gibt das Programm die Hauptstadt dieses Bundeslandes aus.
Und fragt den Benutzer erneut nach dem Namen eines Bundeslandes.

- Wenn der Benutzer jedoch „Ende“ eingibt, soll das Programm aufhören, den Benutzer nach weiteren Namen von
Bundesländern zu fragen und sich beenden.

- Wenn der Benutzer irgendeine Eingabe tätigt, die weder der Name eines Bundeslandes noch „Ende“ ist, soll das
Programm „Falsche Eingabe“ ausgeben und erneut nach dem Namen eines Bundeslandes fragen.
"""


def user_input():
    return str(input("Please enter a Bundesland: "))


def sanitize(string):
    string = string.lower()
    string = string.replace("ä", "ae")
    string = string.replace("ö", "oe")
    string = string.replace("ü", "ue")
    string = string.replace(" ", "-")
    return string


# Game Data
bundeslandes = {
    "baden-wuerttemberg": "stuttgart",
    "bayern": "muenchen",
    "berlin": "berlin",
    "brandenburg": "potsdam",
    "bremen": "bremen",
    "hamburg": "hamburg",
    "hessen": "wiesbaden",
    "mecklenburg-vorpommern": "schwerin",
    "niedersachsen": "hannover",
    "nordrhein-westfalen": "duesseldorf",
    "rheinland-pfalz": "mainz",
    "saarland": "saarbruecken",
    "sachsen": "dresden",
    "sachsen-anhalt": "magdeburg",
    "schleswig-holstein": "kiel",
    "thueringen": "erfurt"
}

print("Game starting...")
print("Enter the name of a Bundesland an get the capital...")
print("Enter 'End' to exit the game...")

# Game Loop
while True:
    name = sanitize(user_input())
    if name in bundeslandes:
        print("The capital of " + name.capitalize()
              + " is " + bundeslandes[name].capitalize())
    elif name == "end":
        break
    else:
        print("Wrong input, try again...")

print("Ending game...")
print("EXIT")
