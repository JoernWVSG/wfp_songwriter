import random

vokale = ['a', 'e', 'i', 'o', 'u']
# Nur geeignete Vokale - Geschmackssache
konsonanten = ['b', 'd', 'g', 'l', 'n', 's']
# mögliche Calls - auch leere Calls
calls = ['yeah!', 'fake that!', 'BwInf rocks!', '', '']
# mögliche Silbenanzahlen in den Zeilen - müssen ungerade sein
silbenzahlen = [3, 5, 7]
# mögliche Zeilenanzahlen in den Strophen
zeilenzahlen = [2, 3, 4, 5]
# mögliche Strophenanzahlen in einem Song
strophenzahlen = [2, 3, 4, 5]


def silbe(kons, voks):
    """Bildet eine Silbe aus einem der Konsonanten und einem der Vokale"""
    return random.choice(kons) + random.choice(voks)


def zeile(kons, voks, anzahl_silben):
    """Bildet eine Zeile mit der gegebenen Anzahl von Silben"""
    # Die Silbe wird für die ganze Zeile einmal bestimmt
    zeilensilbe = silbe(kons, voks)
    zeilenergebnis = ""
    for i in range(anzahl_silben):
        zeilenergebnis += zeilensilbe
        if i == (anzahl_silben - 1) / 2:
            zeilenergebnis += "p di"
        zeilenergebnis += " "
    return zeilenergebnis


def call():
    """Sucht aus der Menge der Calls einen(eventuell leeren) Call heraus """
    return random.choice(calls)


def strophe(anzahl_zeilen, anzahl_silben):
    """Bildet eine Strophe mit den gegebenen Anzahlen fuer Zeilen und Silben."""
    anzahl_konsonanten = random.randint(2, 3)  # zwei oder drei Konsonanten
    auswahl_konsonanten = random.sample(konsonanten, anzahl_konsonanten)
    anzahl_vokale = random.randint(2, 3)  # zwei oder drei Vokale
    auswahl_vokale = random.sample(vokale, anzahl_vokale)
    for i in range(anzahl_zeilen):
        print(zeile(auswahl_konsonanten, auswahl_vokale, anzahl_silben))
    strophen_call = call()
    # ein nicht-leerer Call wird an die Strophe angehängt
    if strophen_call != "":
        print(strophen_call)
    print("")  # leere Zeile am Ende der Strophe


def muster(laenge, grundfolge):
    """Waehlt eine Folge (der gegebenen Laenge) von Elementen der gegebenen Grundfolge auf drei verschiedene Arten aus."""
    folge = []
    auswahl = random.randint(1, 3)
    if auswahl == 1:  # Art 1: abwechselnd zwei verschiedene Elemente
        elementpaar = random.sample(grundfolge, 2)  # zwei Elemente auswählen
        for i in range(laenge):
            folge.append(elementpaar[i % 2])  # i%2 ergibt abwechselnd 0 und 1
    elif auswahl == 2:  # Art 2: immer das gleiche Element
        element = random.choice(grundfolge)  # Element auswählen
        for i in range(laenge):
            folge.append(element)
    else:  # auswahl == 3; Art 3: Grundmenge der Reihe nach
        for i in range(laenge):
            folge.append(grundfolge[i % len(grundfolge)])
    return folge


def song():
    """Bildet einen vollständigen Song."""
    strophenzahl = random.choice(strophenzahlen)
    zeilenzahlmuster = muster(strophenzahl, zeilenzahlen)
    silbenzahlmuster = muster(strophenzahl, silbenzahlen)
    for i in range(strophenzahl):
        strophe(zeilenzahlmuster[i], silbenzahlmuster[i])


#print (silbe(['s', 'g', 't'], ['u', 'a']))
#print (zeile(['s', 'g', 't'], ['u', 'a'], 3))
#strophe(3,5)
#strophe(4,5)
#strophe(3,5)
#strophe(4,5)

song()