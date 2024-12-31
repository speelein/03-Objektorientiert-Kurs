class Archer:
    """
    A class representing an Archer with hp and mana attributes and a walk method.
    """
    hp = 100
    mana = 0

    def walk(self):
        print(f'ich bin {self} und laufe')

# Access class attributes
print(Archer.hp)  # Output: 100
print(Archer.mana)  # Output: 0

# Create an instance of Archer
archer1 = Archer()

# Access instance attributes
print(archer1.__dict__)  # Output: {}

# Call the walk method
archer1.walk()  # Output: ich bin <__main__.Archer object at 0x...> und laufe

# Print the class dictionary
print(Archer.__dict__)
print(type(Archer.__dict__))