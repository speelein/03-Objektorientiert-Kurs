class Auto:

    anzahl_reifen = 4 # in Grossbuchstaben wenn Konstante, zB.ANZAHL_AUTOREIFEN

    winterreifen_noetig = False

    anzahl_autos = 0



    def __init__(self, marke, farbe, sitze, kilometerstand):
        self.marke = marke
        self.farbe = farbe
        self.sitze = sitze
        self.kilometerstand = kilometerstand
        Auto.anzahl_autos += 1             # bei jeder Init wird die Anzahl Auto erhoeht
        # self.anzahl_reifen  ????? moeglich aber nicht gut, wuerde uebergeben



    def kilometerstand_ausgeben(self):
        print(self.kilometerstand)

    def fahren(self,kilometer):
        self.kilometerstand += kilometer
        self.kilometerstand_ausgeben()

auto_1 = Auto("BMW" , "rot" , 4 , 30000)
auto_2 = Auto("VW", "blau", 6, 100000)

print(auto_2.farbe)

auto_1.fahren(200)
auto_2.kilometerstand_ausgeben()



print(Auto.anzahl_reifen)  # wird in Auto nachgeschaut, im Klassennamen

print(auto_1.anzahl_reifen)  # zuerst wird in den Objektvariabelen (Atributen) nachgeschaut,

print(auto_2.anzahl_reifen)  # wenn da nicht vorhanden, dann eien Stufe hoeher im Auto usw.

Auto.anzahl_reifen = 3  # ueberschrieben Klassenvariable / in __init__ moeglich ???????

print(auto_2.anzahl_reifen)
print(Auto.anzahl_reifen) 

print(auto_2.winterreifen_noetig)
print(Auto.winterreifen_noetig) 

auto_1.winterreifen_noetig = True   # Es wird so zur Instanzvariablen

print(auto_1.winterreifen_noetig)
print(Auto.winterreifen_noetig) 

print(Auto.anzahl_autos)  