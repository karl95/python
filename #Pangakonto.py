#Prog is.töö nr2 PANGAKONTO

def kontohaldur(saldo):
    if saldo == 100:
        print("Teie algne saldo on: 100€")
    else:
        print("vale summa")
        return

    kasutaja_soov = input("Kas soovite teha sissemakset?: (Jah/Ei)").lower() #väga vabandan! selle googeldasin!
    if kasutaja_soov == "jah":
        sissemakse = int(input("Tee sissemakse 50€ täpselt: "))
        if sissemakse != 50:
            print("Vale summa")
            return
    
        saldo += sissemakse
        print(f"Kontojaak parast sissemakset on: {saldo}€")
    elif kasutaja_soov == "ei":
        print("Sissemakset ei tehtud")
    else:
        print("Vale sisend, palun vastake 'jah' voi 'ei' ")
        return

    kasutaja_soov = input("Kas soovite raha kontolt valja votta?: (Jah/Ei)").lower()
    if kasutaja_soov == "jah":
        valjavote = int(input("Vota 20€ kontolt valja?: "))
        if valjavote != 20:
            print("Vale summa")
            return

        saldo -= valjavote
        print(f"Kontojaak parast valjavotet on: {saldo}€")
    elif kasutaja_soov == "ei":
        print("Valjavote ei toimunud")
    else:
        print("Vale sisend, palun vastake 'jah' voi 'ei' ")
        return

kontohaldur(100)











