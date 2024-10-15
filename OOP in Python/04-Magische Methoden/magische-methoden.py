class Buch:

    def __init__(self, titel, autor, anzahl_seiten):
        self.titel = titel
        self.autor = autor
        self.anzahl_seiten = anzahl_seiten

    def ueber_tausend_seiten(self):
        return self.anzahl_seiten > 1000
    
    def __len__(self): # magig method fuer len, dann kann unten aufgerufen werden
        return self.anzahl_seiten
    
    def __str__(self):
        return self.titel + ", " + autor
    
    def __add__(self, other):  # muss nicht mit other, XXX moeglich, nur fuer Zweiten Wert steht other oder ..... XXX
        return self.anzahl_seiten + other.anzahl_seiten # Opperatoroverload
    
titel_1 = "Harry Potter und der Feuerkelch"   # titel gesetzt fuer titel_1
titel_2 = "Harry Potter und der Halbblutprinz"  # titel gesetzt fuer titel_2
autor  = "J.K.Rowling"  # autor fur Buch gesetzt

feuerkelch = Buch(titel_1, autor, 767)  # variable feuerkelch uber Buch titel_1 und autor seitenzahl gesetzt
halbblutprinz = Buch(titel_2, autor, 656) # variable feuerkelch uber Buch titel_2 und autor seitenzahl gesetzt
print(feuerkelch.ueber_tausend_seiten())  # erst das Objekt, dann die Funktion, def ueber_tausend_seiten
print(len(feuerkelch)) # __len__ aufruf
print(feuerkelch.__len__()) # siehe __len__
print(titel_2.__str__()) # so oder

print(str(halbblutprinz)) # auch so
print(str(feuerkelch))  # auch so
print(feuerkelch) # str automatisch
print(feuerkelch + halbblutprinz) # siehe def __add__

"""
5, "strings", listen..... werden in Python als Objekte behandelt.

"""