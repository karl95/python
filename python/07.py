"""Ülesanne 07
Loo lugudest loend (koos numbrite ja jutumärkidega)
1. ALIKA – “Bridges”
2. Anett x Fredi – “Read Between The Lines”
3. villemdrillem – “leekiv armastus”
4. Clicherik & Mäx – “PAKSUD”
5. nublu – “ära ärata”
6. NOËP – “Move Your Feet”
7. Trad.Attack! – “Bring It On”
8. Bedwetters – “It Is What It Is”
9. Reket – “Panama paberid”
10. Grete Paia – “Võluväel”
Kuva kasutajale kõik lood massiivist
Küsi millist lugu ta “kuulata” soovib
Kuva kasutaja valitud lugu
Kasuta etteantud loendit ja toesta nõutud operatsioonid. Lisa igale tegevusele kommentaar ja vasta täislausega:
“jaanuar”,-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3
Kuva mõõdetava kuu nimetus
Kuva viimase mõõtmise tulemus
Kuva ainult temperatuurid
Leia kuu maksimaalne ja minimaalne temperatuur
Leia kuu keskmine temperatuur
Mitu korda esines -20 kraadi
Eemalda element nr 5
Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
Sorteeri temperatuurid nimekirjas kasvavas järjekorras"""

nimi = ["Jyri","Mari","Maali","Maaja","Karin Eegreid","Anna Nuga","Juuli","Mai","Hug Mungus"]

#print(nimi[0])

#for i in nimi:
#    print(i)
    
for i in range(4):
    print(f"{i+1}. {nimi[i]}")
valik = int(input("Vali lugu (1-4): "))
print(f"Mängin: {nimi[valik-1]}")

    