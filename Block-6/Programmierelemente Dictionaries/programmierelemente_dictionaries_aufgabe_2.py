'''
Aufgabe 2
Erkundigen Sie sich auf w3schools, YouTube, Google oder Ähnlichem (siehe Quellen unten) nach
(weiteren) Möglichkeiten, wie man...
'''

key_pair_dic = {
    1: "val-1",
    2: "val-2",
    3: "val-3",
    4: "val-4",
    5: "val-5",
    }

# - erfragen kann, ob ein bestimmter Key im Dictionary vorhanden ist.
if 1 in key_pair_dic:
    print("1 ist im Dictionary vorhanden")

if key_pair_dic[1]:  # Fehler bei Undefined
    print("1 ist im Dictionary vorhanden")

if key_pair_dic.get(1, None):
    print("1 ist im Dictionary vorhanden")

# - erfragen kann, ob ein bestimmter Value im Dictionary vorhanden ist.
print("Finding value 'val-5'")
for key, value in key_pair_dic.items():
    if "val-5" == value:
        print("Key: ", str(key), " Value: ", value)

if "val-5" in key_pair_dic.values():
    print("val-5 is in dictionary")

# - den zu einem bestimmten Key gehörenden Value aus einem Dictionary auslesen kann.
print("Val auslesen", str(key_pair_dic.get(1)))
print("Val auslesen", str(key_pair_dic[1]))  # Fehler bei Undefined

# - alle Keys aus einem Dictionary auslesen kann.
print(key_pair_dic.keys())

# - alle Values aus einem Dictionary auslesen kann.
print(key_pair_dic.values())

# - zu einem bestimmten Key einen Value ins Dictionary speichern kann.
key_pair_dic.update({6: "val-6"})
key_pair_dic[7] = "val-7"
print(key_pair_dic)

# - einen bestimmten Key und den dazugehörenden Value aus einem Dictionary entfernen kann.
key_pair_dic.pop(7)
del key_pair_dic[6]
print(key_pair_dic)

# - alle Einträge aus einem Dictionary entfernen kann.
# key_pair_dic.clear()
# print(key_pair_dic)

# - die Länge eines Dictionaries erfragen kann (also die Anzahl an Einträgen im Dictionary).
print(len(key_pair_dic.keys()))
print(len(key_pair_dic))

# - durch ein Dictionary iterieren kann (um bspw. für jedes/mit jedem Element etwas zu tun).
for key, val in key_pair_dic.items():
    print("Key: ", str(key), " Value: ", value)
