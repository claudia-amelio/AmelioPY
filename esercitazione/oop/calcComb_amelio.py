#impostando il programma
#costruzione classe
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
            fact *= num
    return fact

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

    def disposizioniRipetizioni(self, k):      #metodo che fa pare della calcomb
        return len(self.__stringa)**k #k è il valore dei posti della combinazione

    def factorial(n):
        fact = 1
        for num in range(2, n + 1):
            fact *= num
        return fact

    def disposizioni(self,k,):
        n=len(self.__stringa)
        k=k
        if k<=n:
            while k>1:
                    k-=1
                    fact = 1
                    for num in range(2, n + 1,):
                         fact *= num
                    
                    return fact

        else:
            print("k non può essere maggiore di n")
            return("errore")

    def permutazioniSemplici(self):
                n=len(self.__stringa)
                return factorial(n)
            

GalileoGalilei = calcComb("stringaDiRiferimento") #è un oggetto che si trova in questa classe di oggetti)

GalileoGalilei.setStringa("lolfh")


print("il numero di disposizioni con ripetizioni è:",GalileoGalilei.disposizioniRipetizioni(5)) 
print ("il numero di disposizioni semplici è:",GalileoGalilei.disposizioni(2))
print ("il risultato della permutazione è:",GalileoGalilei.permutazioniSemplici())



