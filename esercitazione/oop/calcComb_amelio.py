#impostando il programma
#costruzione classe
class calcComb:

    def __init__(self,stringa): #definisco una funziona
     #(che è una serie di azioni che si possono attuare su un oggetto, variabile)
     
        self.__stringa = stringa 
        self.stringalist = list(stringa)

    def getStringa(self):
        return self.__stringa

    def getStringalist(self):
        return self.stringalist

    def setStringa(self, str):
        self.__stringa = str
        self.stringalist = list(str)

    def permutazioni(self, k):      #metodo che fa pare della calcomb
        return len(self.__stringa)**k #k è il valore dei posti della combinazione

    def posizioni(self,k):
        return 
#impostando le variabili, che diventano degli oggetto

GalileoGalilei = calcComb("Misura ciò che è misurabile, e rendi misurabile ciò che non lo è.") #è un oggetto che si trova in questa classe di oggetti)
print(GalileoGalilei.permutazioni(2)) 
print(GalileoGalilei.stringa)
print(GalileoGalilei.getStringa())