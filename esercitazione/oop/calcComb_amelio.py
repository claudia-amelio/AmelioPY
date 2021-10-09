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
        d=len(self.__stringa)
        if k<d:
            while k>1:
                y=(d-k)
                k=k-1
                
        else:
            print("k non può essere maggiore di n")
            return("errore")


    
    #def eliminazioniRipetizioni(self):
        #for lettera in GalileoGalilei.getStringalist:
          #  str.count(lettera)
          #  i=+lettera
#impostando le variabili, che diventano degli oggetto

GalileoGalilei = calcComb("stringaDiRiferimento") #è un oggetto che si trova in questa classe di oggetti)

GalileoGalilei.setStringa("lolfddfll")
print(GalileoGalilei.permutazioni(5)) 
#print(GalileoGalilei.eliminazioniRipetizioni())
print (GalileoGalilei.disposizioni(5))



