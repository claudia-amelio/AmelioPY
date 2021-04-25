cognomi_3d = ["Amelio", "Avallone", "Aversa", "Barbato", "Calabrese", "Cannarsa", "Cante", "Capurro", "Carola", "Caturano", "Corvaglia", "Gargiulo", "Gentile", "Grillo", "Guglielmetti", "Lucarelli", "Mazzella", "Miranda", "Pagliarulo", "Parente", "Pavone", "Pignalosa", "Pirovine", "Sacco", "Saturno", "Stanziola", "Trifoni", "Triunfo", "Zambardino", "Zubbo"]

while True:
    try:
        n = int(input("inserisci un numero, in modo da avere il cognome corrispondente:"))
        n -= 1 #per non introdurre lo 01
        print(cognomi_3d[n])
        break

    except ValueError: #non hai introdotto il numero
        print("indroduci un numero")

    except IndexError: #hai introdotto un numero che supera la numerazione dei cognomi
        print("non hai introdotto un numero valido")

    except: #quando non ho calcolato l'errore che hai fatto (non so quale sia l'errore)
        print("Errore non calcolato")
