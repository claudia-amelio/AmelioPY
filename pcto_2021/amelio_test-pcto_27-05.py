#CALCOLO STATISTICO DEL PIGRECO

# Al crescere di N, il valore stimato di PiGreco si avvicinerà a quello effettivo
# Seguenza di numeri casuali x e y

#Formula : PiGreco = 4* Dentro / Ntotale


D = 0 # Per impostare una variabile
N = 10000000 # Numeri di tentativi

import random # Per generare la sequenza dei numeri casuali

for i in range(N):
    x = random.random()
    y = random.random()

    # Se la distanza dei punti generati rientra nella circonferenza
    if x*x+y*y<=1:
        D+=1  # Se la condizione precedente è soddisfatta, il valore di D aumenta

#Formula
PiGreco = (4*D)/N

#Prodotto finale
print("il valore di PiGreco è:",PiGreco)
