
#IMPOSTANDO IL PROGRAMMA

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

class calcComb: #costruzione classe

    def __init__(self,stringa): #creazione di una classe di oggetti
     
        self.__stringa = stringa 
        self.stringalist = list(stringa) #prende la stringa e ti crea l'insieme di elementi di quella stringa

    def getStringa(self):       #definisco una funzione(che è una serie di azioni che si possono attuare su un oggetto)
        return self.__stringa   #non c'è "k" --> non è una funzione che prende una variabile in input

    def getStringalist(self):    
        return self.stringalist

    def setStringa(self, str):      #sto cambiando la stringa
        self.__stringa = str
        self.stringalist = list(str)
    
    def permutazioniConRipetizione(self,n,k,h):
        if k + h <= n:
            a = factorial(n)
            b = factorial(k)
            c = factorial(h)
            d = b*c
            return (a/d)

galileoGalilei = calcComb("stringaDiRiferimento") #è un oggetto che si trova in questa classe di oggetti)
galileoGalilei.setStringa("matematico")

print ("il risultato della permutazione è:",galileoGalilei.permutazioniConRipetizione(7,3,4))