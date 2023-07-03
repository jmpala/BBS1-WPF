wochentage = {
    "Mo": "Montag",
    "Di": "Dienstag",
    "Mi": "Mittwoch",
    "Do": "Donnerstag",
    "Fr": "Freitag",
    "Sa": "Samstag",
    "So": "Sontag"
    }


def name_des_wochentages_erfragen():
    eingabe = input("Bitte geben Sie einen Wochentag ein: ")
    while eingabe != "END":
        print(wochentage.get(eingabe, "Ungültige Eingabe"))
        eingabe = input("Bitte geben Sie einen Wochentag ein: ")
    return


name_des_wochentages_erfragen()
