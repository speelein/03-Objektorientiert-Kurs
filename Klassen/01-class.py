class Archer:
    hp = 100
    mana = 0
    def walk(self):
        print(f'ich bin {self}und laufe')

print(Archer.hp)
print(Archer.__dict__)
print(type(Archer.__dict__))

# Instanz von Archer erzeuegen
archer1 = Archer()
print(archer1.__dict__)
# { } dict ist leer keine Werte enthalten

archer1.walk()
# Es wird in archer1 trozdem die Funktion ausgegebne, offensichtlich an archer1 vererbt