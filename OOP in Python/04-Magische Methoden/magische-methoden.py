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
        return self.titel
    
    def __add__(self, other):  # muss nicht mit other, XXX moeglich, nur fuer Zweiten Wert steht other oder ..... XXX
        return self.anzahl_seiten + other.anzahl_seiten # Opperatoroverload
    
titel_1 = "Harry Potter und der Feuerkelch"
titel_2 = "Harry Potter und der Halbblutprinz"
autor  = "J.K.Rowling"

feuerkelch = Buch(titel_1, autor, 767)
halbblutprinz = Buch(titel_2, autor, 656)
print(feuerkelch.ueber_tausend_seiten())  # erst das Objekt, dann die Funktion, def ueber_tausend_seiten
print(len(feuerkelch)) # __len__ aufruf
print(feuerkelch.__len__())
print(str(halbblutprinz))
print(titel_2.__str__()) # so oder
print(str(feuerkelch))  # auch so
print(feuerkelch) # str automatisch
print(feuerkelch + halbblutprinz) # siehe def __add__

"""
5, "strings", listen..... werden in Python als Objekte behandelt.

"""