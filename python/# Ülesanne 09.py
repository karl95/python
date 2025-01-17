# Ülesanne 09
# Kuna tsüklid on oluline osa programmeerimisel, siis on oluline mõista selle kasutamist. Seepärast leiad natuke pikema nimekirja ülesannetega.
# Genereeri ja kuva arvud arvud 1-20
# Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
# import random
# random.randint(min, max)
# Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75
# Leia paaris ja paaritud arvud ning lisa oma loendisse
# Kuva paaris ja paritute arvude summad
# Kuva arvud 1-42
# Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
# Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
# Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)
# Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.
# Kuva nimekirjast unikaalsed nimed:
# nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
# Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.
# ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
# Koosta programm, mis genereerib ja kuvab korrutustabeli, kus iga number korrutatakse iseendaga:
# Näiteks:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
# Loo programm, mis loob suvalised tehted 1-100 arvudega.
# Kasuta tsükli puhul alakriipsu
# kasuta suvalise tehte märgi jaoks loendit ja sealt suvalise märgi leidmiseks random.choice()
# Näiteks:
# 7 – 2=
# 45 * 69=
# 71 – 45=
# 84 / 57=
# 59 * 87=
# 84 – 71=
# 65 * 32=
# 63 – 11=
# 72 – 90=
# 29 / 93=
# Täienda eelmist ülesannet ja kasutaja käest küsitakse vastust.
# Õiged vastused loetakse kokku
# Kui saab vähemalt poole punktid, siis saab A, muul juhul MA




# for i in range(1,21):
#     print(i, end=" ")
# import random
# for i in range(1,21):
#     print(random.randint(1, 99), end=" ")

# numbrid = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]

# paaris = []
# paaritud = []
# for nr in numbrid:
#     if nr%2==0:
#         paaris.append(nr)
#     else:
#         paaritud.append(nr)
    
# print(paaris)
# print(paaritud)





# Kuva arvud 1-42
# for i in range(1,43):
#     if i%3==0 and i%5==0:
#         print(f"{i} TIK")
#     elif i%3==0:
#         print(f"{i} TAK")
#     elif i%5==0:
#         print(f"{i} TIKTAK")
#     else:
#         print(i)






#tärnide kolmnurga harjutus

# for i in range(1,6):
#     print(" " * i, end="")
#     print("*" * (6*i))






ev_data = [
    ['vehicle', 'range', 'price'],
    ['Tesla Model Y Long Range', '330', '58990'],
    ['Volkswagen ID.4 Pro', '260', '39995'],
    ['Ford Mustang Mach-E', '300', '42995'],
    ['Audi e-tron GT', '238', '102700'],
    ['Nissan Leaf', '149', '27400'],
    ['BMW iX xDrive50', '324', '83995'],
    ['Polestar 2', '265', '45500'],
    ['Kia EV6 Long Range', '310', '47795'],
    ['Mercedes-Benz EQS 450+', '350', '102310'],
    ['Hyundai Kona Electric', '258', '37400']
]

ranges = []

for autod in ev_data:
    print(f"{autod[0]:30} {autod[1]:5} {autod[2]:7}")
    if autod[1].isnumeric():
        ranges.append(int(autod[1]))
        # for i in autod:
        #     print(i)
print(f"Keskmine ulatus: {sum(ranges)/len(ranges)}")

for autod in ev_data:
    if autod[1].isnumeric():
        if int(autod[1]) > 300:
            print(autod[0])
