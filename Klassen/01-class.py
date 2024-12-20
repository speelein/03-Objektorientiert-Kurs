class Archer:
    """
    This module defines the Archer class.

    Classes:
        Archer: A class representing an archer with attributes for health points (hp) and mana, 
                and a method to simulate walking.

    Usage Example:
        # Create an instance of Archer
        
        # Access class attributes
        print(Archer.hp)  # Output: 100
        print(Archer.mana)  # Output: 0
        
        # Access instance attributes
        print(archer1.__dict__)  # Output: {}
        
        # Call the walk method
        archer1.walk()  # Output: ich bin <__main__.Archer object at 0x...> und laufe
    """
    hp = 100
    mana = 0
    def walk(self):
        print(f'ich bin {self}und laufe')

#print(Archer.hp())
print(Archer.__dict__)
print(type(Archer.__dict__))

# Instanz von Archer erzeuegen
archer1 = Archer()
print(archer1.__dict__)
# { } dict ist leer keine Werte enthalten

archer1.walk()
# Es wird in archer1 trozdem die Funktion ausgegebne, offensichtlich an archer1 vererbt