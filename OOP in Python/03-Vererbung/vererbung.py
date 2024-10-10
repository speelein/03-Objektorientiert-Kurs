
class Haustier:

    NIEDLICH = True

    def __init__(self, name, alter, hunger, zufriedenheit):
        self.name = name
        self.alter = alter
        self.hunger = hunger
        self.zufriedenheit = zufriedenheit
    
    def essen(self):
        self.hunger = False
        print("lecker")

    def streicheln(self):
        self.zufriedenheit += 8
        print("ich werde gestreichelt")

    def schlafen(self):
        print("ich schlafe")


class Hund(Haustier):

    def __init__(self, name, alter, hunger, zufriedenheit,rasse): # automatisch eingefuegt
        super().__init__(name, alter, hunger, zufriedenheit)  # bezieht sich auf die Oberklasse, self wird automatsch uebergeben
        self.rasse = rasse

    def stoeckchen_holen(self):
        self.zufriedenheit += 10
        self.hunger = True
        print("Stoechen geholt")
        self.schlafen()


class Katze(Haustier):
    def __init__(self, name, alter, hunger, zufriedenheit, augenfarbe): # augenfarbe hinzugefuegt
        super().__init__(name, alter, hunger, zufriedenheit) 
        self.augenfarbe = augenfarbe

    def streicheln(self):  # ueberschreibt streichelmethode aus Haustier
        self.zufriedenheit += 20
        print("Katze schlaeft")
        print("Miau")   

    def kratzbaum_kratzen(self):
        self.zufriedenheit += 18
        self.hunger = False
        print("Katze hat keinen Hunger")

hund_1 = Hund("Fox", 7, True, 5, "Dackel")
katze_1 = Katze("Peter", 5, True, 10, "blau")

print(hund_1.rasse)
print(hund_1.stoeckchen_holen())

print(katze_1.augenfarbe)
print(katze_1.streicheln())
print("katze", katze_1.schlafen())
print(katze_1.NIEDLICH)