
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

#metodi matematica

    def disposizioniConRipetizioni(self, k):   #metodo che fa pare della calcomb
        return len(self.__stringa)**k          #k è un gruppo di elementi combinati

    def factorial(n):
        fact = 1
        for num in range(2, n + 1):
            fact *= num
        return fact

    def disposizioniSemplici(self,k,):
        n=len(self.__stringa)
        if k<=n:
            x=factorial(n)
            y=factorial(n-k)
            return (x/y)

        else:
            print("k non può essere maggiore di n")
            return("errore")

    def permutazioniSemplici(self):
                n = len(self.__stringa)
                return factorial(n)

    def permutazioniConRipetizione(self,n,k,h):
        if k + h <= n:
            a = factorial(n)
            b = factorial(k)
            c = factorial(h)
            d = b*c
            return (a/d)

    #def lettereMaiuscole(self):
     #   self.__stringa = upper(str)
      #  self.stringalist = list(upper(str))

#CREAZIONE DELL'OGGETTO

galileoGalilei = calcComb("stringaDiRiferimento") #è un oggetto che si trova in questa classe di oggetti)
galileoGalilei.setStringa("matematico")

print("la lista relativa alla stringa è:",galileoGalilei.getStringalist())
print("la stringa è",galileoGalilei.getStringa())
print("il numero di disposizioni con ripetizioni è:",galileoGalilei.disposizioniConRipetizioni(5)) 
print ("il numero di disposizioni semplici è:",galileoGalilei.disposizioniSemplici(2))
print ("il risultato della permutazione è:",galileoGalilei.permutazioniSemplici())
print ("il risultato della permutazione è:",galileoGalilei.permutazioniConRipetizione(10,4,3))