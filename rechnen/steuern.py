def berechnen(betrag, prozent=10):
    ergebnis = betrag / 100 * prozent
    return ergebnis


def abgaben(betrag):
    ergebnis = betrag * 0.1
    return ergebnis
""""
steuer_betrag = steuern (100)
print (steuer_betrag)

buch_steuer = steuern(100, prozent=5)
print (buch_steuer)
"""