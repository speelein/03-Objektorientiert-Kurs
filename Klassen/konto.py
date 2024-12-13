class Konto(object): 

    def __init__(self, inhaber, kontonummer, 
                 kontostand, 
                 kontokorrent=0): 
        self.__Inhaber = inhaber 
        self.__Kontonummer = kontonummer 
        self.__Kontostand = kontostand 
        self.__Kontokorrent = kontokorrent

    def ueberweisen(self, ziel, betrag):
        if(self.__Kontostand - betrag < -self.__Kontokorrent):
            # Deckung nicht genuegend
            return False  
        else: 
            self.__Kontostand -= betrag 
            ziel.__Kontostand += betrag 
            return True
 
    def einzahlen(self, betrag): 
       self.__Kontostand += betrag 
 
    def auszahlen(self, betrag): 
       self.__Kontostand -= betrag 
 
    def kontostand(self): 
        return self.__Kontostand