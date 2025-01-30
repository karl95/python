# Iseseisev töö 2.py
# Otil on hommikuti raske tõusta ja tal on äratuskell, mis äratab teda teatud arv kordi koos tervitustekstiga. Koostada programm, mis
# küsib kasutajalt, mitu korda äratus heliseb ning
# väljastab sama arv kordi ekraanile Tõuse ja sära!.
# Näited programmi tööst:


# kordade_arv = int(input("kordade arv: "))

# for i in range(kordade_arv):
#     print("Tõuse ja Sära!")


# MURELIKUD LAPSEVANEMAD
# Jänesevanemad on mures, et lapsed ei liigu piisavalt. Laste motiveerimiseks mõtlesid nad välja süsteemi, kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 4. metsaringi läbimisel 4 porgandit juurde, 6. metsaringi läbimisel 6 porgandit juurde jne. Paarituarvulistel ringidel porgandeid juurde ei saa. 
# Koostada programm, mis
# küsib kasutajalt ringide arvu (mittenegatiivne täisarv);
# arvutab while-tsükli abil saadavate porgandite koguarvu;
# väljastab saadavate porgandite koguarvu ekraanile.
# Näiteks, kui kasutaja sisestas 6, siis summa on 12, sest 2 + 4 + 6 = 12. Kui kasutaja sisestas 7, siis on summa samuti 12, sest 2 + 4 + 6 = 12.
# Näited programmi tööst:

# porgandid = 0
# ringide_arv = 100

# while ringide_arv > 0:
#     # print(ringide_arv)
#     if ringide_arv % 2 == 0:
#         porgandid += ringide_arv
#     ringide_arv -=1

# print(porgandid)




# TÄRINGUD
# Erinevate täringumängude jaoks on vajalik erinev arv täringuid. Näiteks Yahtzee (Yatzy) jaoks on vaja 5 täringut, Crapsi jaoks aga 2 täringut. Koostada programm, mis
# küsib kasutajalt vajalike täringute arvu;
# viskab vastava arvu täringuid (genereerib vastava arvu suvalisi arve, mis jäävad 1 ja 6 vahele);
# väljastab iga arvu eraldi reale.
# Vihje: Kui kasutada tsüklit, mis teeb kasutaja sisestatud arvu samme, siis igal sammul tuleb genereerida üks juhuslik arv ja see väljastada.
# Näited programmi tööst:






# MALE
# Legend räägib, et malemängu leiutajale olla tollane valitseja pakkunud tasu. (Sellest legendist räägib ka Tõnu Tõnso paarikümne aasta taguses leheloos.) Leiutaja oli “tagasihoidlik” ja palus tasuks
# esimese ruudu eest 1 nisutera;
# teise ruudu eest 2 korda rohkem ehk 2;
# kolmanda ruudu eest veel 2 korda rohkem ehk 4;
# neljanda ruudu eest siis 8;
# viienda ruudu eest 16 jne.
# Malelaual on 64 ruutu. Koostada programm, mis
# küsib kasutajalt ühe täisarvu;
# arvutab while-tsükli abil, mitu nisutera sellise järjekorranumbriga ruudu eest leiutaja küsis;
# tulemus väljastatakse ekraanile pärast tsüklit.
# Näide programmi tööst:





# ÕUNAD
# Lumivalgekesel oli 14 õuna ja ta tahtis neid pöialpoistega jagada. Ta sai aru, et kui kõik seitse pöialpoissi tahavad õunu ja ta annaks kõigile kaks õuna, jääks ta ise üldse ilma. Nüüd otsustas ta õunu jagada nii, et küsib, mitu pöialpoissi tahab õunu, ja seejärel loosib iga soovija korral, kas anda talle üks või kaks õuna. Koostada programm, mis
# küsib kasutajalt, mitu pöialpoissi tahab õunu (võib eeldada, et sisestatakse täisarv lõigust [0; 7]);
# leiab ja väljastab eraldi ridadele, mitu õuna saab iga pöialpoiss (programm genereerib iga kord juhuslikult arvu 1 või 2);
# leiab ja väljastab eraldi reale, mitu õuna jääb Lumivalgekesele.
# Näide programmi tööst:

import random

ounad = 14
pp = int(input("Mitu PP tahab õuna: "))

for i in range(pp):
    suv_oun = random.randint(1,2)
    print(suv_oun)

    ounad -= suv_oun

print(f"Lumivalgukesel jäi {ounad} õuna: ")

