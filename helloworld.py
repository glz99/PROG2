def hallo(name="Welt", lang="en"):

    if lang == "en":
        print("Hallo" + name + "!")
    elif lang == "de":
        print("Hallo" + name + "!")
    elif lang == "ch":
        print("Hoi" + name + "!")
    else:
        print("Tach")

hallo(name="Annalena", lang="en")
