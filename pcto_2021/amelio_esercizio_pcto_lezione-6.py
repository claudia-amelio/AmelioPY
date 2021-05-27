from array import*

#prima parte da inserire in una funzione

Max=int(input('inserire un valore massimo:'))

def Numeri_Primi(Max):
    Cr=array('i',[1 for i in range(Max+1)])

    Cr[0]=0
    Cr[1]=0

    i=2

    while i*i<=Max:
        if Cr[i]==1:
            j = i+i
            while j<= Max:
                Cr[j] = 0
                j+=i
        i+=1
    return Cr


#seconda parte da inserire in una funzione
def conteggio(Max, Cr): 
    print('Numeri Primi')
    Cont = 0
    for i in range (0, Max+1):
        if Cr[i] == 1:
            print(i, end=' ')
            Cont +=1

print('\n Ci sono', Cont, 'numeri primi <=', Max)

Max= int(input('inserisci un valore massimo'))

Cr = numeri_primi(Max)

conteggio(Max, Cr)
