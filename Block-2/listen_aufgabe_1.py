
print("I dont have friends")
friends = []

print("but after going to Roxy, I befriend some cool people")
friends.append("John")
friends.append("Greta")
friends.append("Anna")
print("My friends:", friends)

print("some parties later, I knew Gretas friends und now are my friends to")
gretas_friends = ["Sofia", "Alina", "Max"]
print("Gretas friends:", friends)
friends.extend(gretas_friends)
print("My friends:", friends)

print("some time later I went out on dates with Sofia")
print("but things went south, and we broke up")
friends.remove("Sofia")
print("My friends:", friends)

print("so now I only have 5 friends more, lucky me")
print("Remaining friends:", len(friends))

print("one day I was testing my brain capabilities and decided")
print("to order my friends alphabetically, and I could")
friends.sort()
print("My ordered friends:", friends)

print("Suddenly later I knew Amanda and after dancing Mambo N° 5")
print("We become good friends, so I wanted to add her into my friends list...")
print("But I want that the alphabetic order remains...")
print("So I added into the second place")
friends.insert(1, "Amanda")
print("My ordered friends:", friends)

print("Some days later, I woke up on opposite day")
print("And I just celebrate it ordering my friends list accordingly")
friends.reverse()
print("My reversed friends:", friends)

print("After some time, I met a person with no friends")
print("So without telling my friends, I clone them and gave him some")
stranger_friends = []
stranger_friends = friends.copy()
print("Stranger friends:", stranger_friends)
print("My friends:", friends)

print("One of the clones actually become my friend")
friends.append("John")
print("But now I habe 2 cloned friends!!!")
print("Cloned friend", friends.count("John"))
print("My friends:", friends)

print("I dont know if it was ethically correct my action")
print("but I poped him! Hope he does not get angry")
friends.pop()
print("My friends:", friends)

print("Then I heard the Clock, it's 8:20 and I am late")
print("Need to hurry up to go to BBS")
print("It was a long dream")
friends.clear()
print("My friends:", friends)
