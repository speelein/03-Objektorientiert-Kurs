print(9+3)
print("ab"+ "cd")
print([1, 2] + [3, 4])

# Der plusopperator hat jeweils eine ander Bedeutung

print((9).__add__ (3))
print("ab".__add__("cd"))
print([1, 2].__add__([3, 4]))


print(type((9).__add__ (3)))
print(type("ab".__add__("cd")))
print(type([1, 2].__add__([3, 4])))

"""
Es sind Objekte. 
__xx__ solche ...... sind bereits in Pyhon vorhanden, brauchen nicht neu definiert werden
die __add__ erkennt also den Typ 
automatisch, so programmiert in Python


"""

