# Iseseisev töö nr.3 (loendid)



# Ülikooli vastuvõetud
# Ülikooli I õppeastmesse (bakalaureuseõpe jm) võetakse igal aastal vastu sadu inimesi. Viimastel aastatel vastuvõetud inimeste arvud on aastate kaupa failis rebased.txt, kus esimesel real on 2011. aastal vastuvõetute arv, teisel real 2012. aastal vastuvõetute arv kuni viimasel real on 2019. aastal vastuvõetute arv. 
# Koostada programm, mis
# loeb failist registreeritud vastuvõetute andmed aastate järgi järjendisse;
# Failist järjendisse saab lugeda järgmise programmijupi abil:


# fail = open("rebased.txt", encoding="UTF-8")
# vastuvõetud = []

# for rida in fail:
#     print(rida)
#     # vastuvõetud.append(int(rida))

# fail.close()

# aasta = input("Lisa aasta 2011 - 2019: ")
# print(vastuvõetud[int(aasta[3]) -1])





# küsib kasutajalt aastat
# võib eeldada, et sisestatakse täisarv, mis kuulub lõiku [2011; 2019].
# väljastab, mitu inimest sel aastal vastu võeti.
# Näide:
#   Palun sisestage, millise aasta andmeid vajate: 2011
#   2011. aastal oli vastuvõetuid 2803
# Jänesevanemate mure ver. 3
# Jänesevanemad on mures, et lapsed ei liigu piisavalt. Laste motiveerimiseks mõtlesid nad välja süsteemi, kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 4. metsaringi läbimisel 4 porgandit juurde, 6. metsaringi läbimisel 6 porgandit juurde jne. Paarituarvulistel ringidel porgandeid juurde ei saa. Koostada programm, mis
# küsib kasutajalt ringide arvu (mittenegatiivne täisarv);
# arvutab for-tsükli ja funktsiooni range() abil saadavate porgandite koguarvu;
# väljastab saadavate porgandite koguarvu ekraanile.
# Näiteks, kui kasutaja sisestas 6, siis summa on 12, sest 2 + 4 + 6 = 12. Kui kasutaja sisestas 7, siis on summa samuti 12, sest 2 + 4 + 6 = 12.
# Porgandite koguarvust võib mõelda kui summast, milles liidetavad on paarisarvud alates 0 kuni esimese paarisarvuni, mis pole suurem kui sisestatud ringide arv.
# Näide
#   Sisestage ringide arv: 6
#   Saadavate porgandite koguarv on 12.

# Sissetulekud
# Failis konto.txt on kirjas ujukomaarvudena pangakonto tehingud (kus positiivsed arvud on sissetulekud ja negatiivsed arvud on väljaminekud). Iga arv on eraldi real. Tekstifaili kasutamiseks programmi sees peab fail asuma programmifailiga samas kaustas.
# Koostada programm, mis
# loeb failist nimega konto.txt andmed;
# väljastab ekraanile kõik sissetulekud ehk failist leitud positiivsed arvud. Iga arv peab olema eraldi real ja positiivsete arvude omavaheline järjekord peab jääma samaks nagu failis. 
# Näide programmi tööst:
# Näiteks antud näitefaili konto.txt puhul peab ekraanile ilmuma


# fail = open("konto.txt", encoding="UTF-8")

# for kirje in fail:
#     if float(kirje) > 0:
#         print(float(kirje), end="\n")
    
# fail.close()






# Jukebox
# Ada tahab valida plaadiautomaadist laulu ja uurib, milliseid laule masin mängib. Muusikapalad on kirjas failis, kus iga laul on eraldi real.
# Programmi testimiseks kasutatakse järgmisi faile, mida võite salvestada või koostada ise mõne tekstiredaktoriga (nt Notepad):
# jukebox.txt
# 80ndad.txt
# eesti_muusika.txt 
# edm.txt
# Koostada programm, mis
# küsib kasutajalt failinime (kasutaja sisestab failinime koos laiendiga, nt jukebox.txt);
# loeb sisestatud nimega failist andmed;
# näitab kõiki laule koos järjekorranumbritega (alates 1);
# küsib kasutajalt, mitmendat laulu ta soovib (kasutaja sisestab alati täisarvu);
# väljastab ekraanile vastavalt valitud arvule muusikapala
# Näide programmi tööst:
# Näiteks antud näitefaili jukebox.txt puhul peab ekraanile ilmuma

fail = open("edm.txt", encoding="UTF-8")
musa = "edm.txt"
fail = open(f"txt/{musa}.txt", encoding="UTF-8")
# print(str(nr)+". "+pala, end="")
nr = 1

for pala in fail:
      print()

print()
valik = int(input("Vali lugu: "))
file.seek(0)
mangin = 1
for pala in fail:
        if valik == mangin:
            print(pala, end="")
            mangin+=1
          
fail.close()


# Tahvli juurde
# Mõned õpetajad on tavatsenud õpilasi tahvli juurde vastama kutsuda kuupäeva järgi vastavalt õpilaste nimekirjale. Näiteks 4. kuupäeval tuleb esimesena vastama nimekirjas 4. olev õpilane.
# Failis nimekiri.txt on õpilaste nimed, igaüks eraldi real. Üks selline, mis on genereeritud leheküljel Random Name Generator. Võite ise koostada ka teistsuguse nimekirja.
# Koostada programm, mis
# küsib failinime (eeldame, et kasutaja sisestatud nimega fail leidub ja seal on vähemalt 31 nime);
# loeb sisestatud nimega failist andmed;
# väljastab vastavalt tänasele kuupäevale õpilase nime, kes peab vastama tulema.
# Programm peab tänase kuupäeva leidma automaatselt, aluseks saab võtta järgmise näite:
# from datetime import * 
# print(datetime.now().day) 
# Näide programmi tööst:

