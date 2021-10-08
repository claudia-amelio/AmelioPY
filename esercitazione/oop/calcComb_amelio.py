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

    def disposizioni(self,k,):
        while k>0:
            y  = len(self.__stringa)*k
            k=-1
            c=+y
        return c


    
    #def eliminazioniRipetizioni(self):
        #for lettera in GalileoGalilei.getStringalist:
          #  str.count(lettera)
          #  i=+lettera
#impostando le variabili, che diventano degli oggetto

GalileoGalilei = calcComb("stringaDiRiferimento") #è un oggetto che si trova in questa classe di oggetti)

GalileoGalilei.setStringa("da")
print(GalileoGalilei.permutazioni(5)) 
#print(GalileoGalilei.eliminazioniRipetizioni())
print (GalileoGalilei.disposizioni(5))



