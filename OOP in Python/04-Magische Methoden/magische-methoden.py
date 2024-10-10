class Buch:

    def __init__(self, titel, autor, anzahl_seiten):
        self.titel = titel
        self.autor = autor
        self.anzahl_seiten = anzahl_seiten

    def uber_tausend_seiten(self):
        return self.anzahl_seiten > 1000
    
    def __len__(self): # magig method fuer len, dann kann unten aufgerufen werden
        return print(self.anzahl_seiten)
    
    def __str__(self):
        return self.titel
    
    def __add__(self, other):
        return self.anzahl_seiten + other.anzahl_seiten # Opperatoroverload
    
titel_1 = "Harry Potter und der Feuerkelch"
titel_2 = "Harry Potter und der Halbblutprinz"
autor  = "J.K.Rowling"

feuerkelch = Buch(titel_1, autor, 767)
halbblutprinz = Buch(titel_2, autor, 656)

#len(feuerkelch)
print(str(halbblutprinz))

#print(__len__(feuerkelch))
#print(__str__(feuerkelch))

print(feuerkelch + halbblutprinz)

"""
5, "strings", listen..... werden in Python als Objekte behandelt.

"""