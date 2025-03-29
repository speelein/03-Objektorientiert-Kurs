# in der Klasse wurden auch funktionen definiert. Aber nicht empohlen ausser 

class Archer:
    hp = 100
    mana = 19
    # es wird jetzt diese Funktion eingefuegt
    # printet aber nur eigenartig den Text ich bin.....
    def walk(self):
        print(f'ich bin {self} und laufe')
hp =  +20
print(Archer.mana)
print(Archer.__dict__)
print(type(Archer.__dict__))

# Instanz von Archer erzeuegen
archer1 = Archer() # warum leer {}
archer2 = Archer()
print(archer1.mana)
print(archer2.__dict__)
# { } dict ist leer keine Werte enthalten

archer1.walk()
archer2.walk()
# Es wird in archer1 trozdem die Funktion ausgegebne, offensichtlich an archer1 vererbt