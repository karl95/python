# Python+json harjutamiseks

# import json

# # Oletame, et olete salvestanud API vastuse JSON faili nimega 'users.json'.
# with open('users.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# # Siin kasutame 'users' võtit, et pääseda ligi kasutajate andmetele
# users = data.get('users', [])

# # Kontrollime, kas 'users' võti on olemas ja see on loend
# if isinstance(users, list):
#     for user in users:
#         firstName = user.get('firstName')
#         lastName = user.get('lastName')
#         maidenName = user.get('maidenName')
#         gender = user.get('gender')
#         email = user.get('email')
#         phone = user.get('phone')
#         username = user.get('username')

#         print(f"Eesnimi: {firstName}, Perenimi: {lastName}, Neiupõlvenimi: {maidenName}, Sugu: {gender}, Email: {email}, Telefon: {phone}, Kasutajanimi: {username}")

# otsing = print("Milliseid andmeid soovid kuvada? Eesnimi, perenimi, neiupõlvenimi, sugu, email, telefon või kasutajanimi?: ")

# otsitav = input("Sisesta märksõna: ")

# leitud = False

# for user in users:
#     if otsing == "Eesnimi" and user.get('firstName').lower() == otsitav.lower():
#         print(f"Leitud kasutaja: {user}")
#         leitud = True
#     elif otsing == "Perenimi" and user.get('lastName').lower() == otsitav.lower():
#         print(f"Leitud perekonnanimi: {user}")
#         leitud = True
#     elif otsing == "email" and user.get('email').lower() == otsitav.lower():
#         print(f"Leitud email: {user}")
#         leitud = True
#     elif otsing == "kasutajanimi" and user.get('username').lower() == otsitav.lower():
#         print(f"Leitud kasutajanimi: {user}")
#         leitud = True

#     if not leitud:
#         print(f"Viga! Otsitud väärtust '{otsitav}' ei leitud.")

# else:
#     print("Kasutajate andmed ei ole oodatud formaadis.")




# ÜL-mis võtab mingid andmed veebist APIGA ja siis kuvame ja laseme kasutaja ise valida!

import requests

# API URL, kust andmed tulevad
url = "https://dummyjson.com/products"

# Teeme päringu veebilehele
response = requests.get(url)

# Kontrollime, kas päring oli edukas
if response.status_code == 200:
    data = response.json()  # Muudame JSON andmed sõnastikuks
    products = data.get('products', [])  # Saame kätte 'products' andmed

    otsing = "Fish Steak"

    counter = 0

    for product in products:

        # print(product["title"])

        if otsing in product["title"]:
            counter+=1
            print(product["title"])

            print(f"Leiti: {counter} tulemus")

        else:
            print(f"Viga! Ei suutnud andmeid laadida. Staatuskood: {response.status_code}")

    # otsing = input("Sisesta otsingukriteerium (title, category, price, description, rating): ").strip().lower()

    # otsinguväärtus = input(f"Sisesta otsitav väärtus {otsing} järgi: ").strip().lower()

    # leitud_tooted = False

    # for product in products:
    #     if otsing == 'title' and otsinguväärtus in product.get('title', '').lower():
    #         leitud_tooted = True
    #         print(product)
    #     elif otsing == 'category' and otsinguväärtus in product.get('category', '').lower():
    #         leitud_tooted = True
    #         print(product)
    #     elif otsing == 'price':
    #         try:
    #             if float(otsinguväärtus) == product.get('price'):
    #                 leitud_tooted = True
    #                 product(product)
    #         except ValueError:
    #             print("Hind peab olema arvuline!")
    #     elif otsing == 'description' and otsinguväärtus in product.get('description', '').lower():
    #         leitud_tooted = True
    #         print(product)
    #     elif otsing == 'rating':
    #         try:
    #             if float(otsinguväärtus) == product.get('rating'):
    #                 leitud_tooted = True
    #                 product(product)
    #         except ValueError:
    #             print("Hinne peab olema arvuline!")

    # if not leitud_tooted:
    #     print(f"Toodet ei leitud {otsing} väärtusega '{otsinguväärtus}'.")







# ÜL3
# sihtkoht = "Rooma"
# paevade_arv = 7
# oobimise_hind = 700.9

# print(sihtkoht, "reis kestab ", paevade_arv, "päeva, mille ööbimise hind on ", oobimise_hind,"€")

# # ÜL4

# arv_a = int(input("Sisesta palun aia esimese külje pikkus: "))
# arv_b = int(input("Sisesta palun aia teise külje pikkus: "))

# summa = 2*(arv_a+arv_b)
# print(f"Aia kogupikkus on: ",summa,"meetrit")

# ÜL4.1

# hind = 12.53
# raamatud = int(input("Sisesta palun mitu raamatut soovid?: "))
# soodustus = hind * 0.3
# print(f"Raamatute hind on: {raamatud + soodustus:.1f}€")


# ÜL4.2

# faili_suurus = int(input("Sisesta faili suurus MB's: "))

# if faili_suurus <= 1:
#     print("Viga!")
# else:
#     print("Korras")

# allalaadimiskiirus = int(input("Sisesta allalaadimiskiirus MB/s: "))

# if allalaadimiskiirus > 0:
#     print("korras!")
# else:
#     print("viga")
   
# aeg_kokku = faili_suurus / allalaadimiskiirus
# print(f"Kokku läheb: ", aeg_kokku, "sekundit")

# ÜL4.3

# try: 
#     kinkekarbi_suurus = 5
#     kingitused = int(input("Lisa kingituste arv: "))
#     print("Kingitusi on: ",kingitused)
#     kastid = kingitused//kinkekarbi_suurus
#     jaak = kingitused % kinkekarbi_suurus
#     print(F"Saad teha {kastid} täis kinkekasti. Üle jääb {jaak} kingitust")

# except:
#     print("Viga")

# ÜL4.4

# import turtle

# pi = 3.14159265

# while True:
#     try:

#         ring = float(input("Sisesta ringi raadius: "))
#         if ring > 0:
#             break
#         else: 
#             print("Raadius peab olema positiivne")

#     except ValueError:
#         print("Viga")

# umbermoot = pi * 2 * ring
# print(f"Ringi Ümbermõõt on: {umbermoot:.2f}")

# pindala = ring ** pi
# print(f"Ringi pindala on: {pindala:.2f}")

# turtle.penup()
# turtle.goto(0, -ring)
# turtle.pendown()
# turtle.color("blue")
# turtle.circle(ring)

# turtle.done()

# ÜL5.1

# try:
#     vanus = int(input("palun sisesta oma vanus: "))
#     if vanus >= 18:
#         print("korras")
#     else: 
#         print("liiga noor")
# except:
#     print("Viga sisestamisel")


# ÜL5.2

# try:
#     temp = 30
#     temp = float(input("Sisesta temperatuur C: "))
#     if temp < 0:
#         print("Pane soojalt riidesse")
#     elif temp > 0 and temp < 15:
#         print("Kanna kevadisi riideid")
#     else:
#         print("Pane suviselt riidesse")

# except:
#     print("Viga")

# ÜL5.3

# import random

# try:
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     vastus = int(input(f"Mis on {arv1} * {arv2} vastus? \n Sisesta vastus: "))
#     korrutis = arv1 * arv2
#     print(vastus)
#     print(korrutis)
#     if korrutis == vastus:
#         print("Õige")
#     else:
#         print("Vale")
            
# except:
#     print("Viga sisestuses")

# ÜL5.4

# import random
# import turtle
# 1
# try:
#     valik = random.randint(0,1)
#     arvamus = int(input("Vali kull 1 või kiri 0: "))
#     if valik == arvamus:
#         print("Õige")
#         turtle.color("green")
#         turtle.circle(50)

#     else: 
#         print("Vale")
#         turtle.color(red)
#         turtle.circle(50)
#         turtle.done()

# except:
#     print("Viga")

# ÜL7.1

# laulud = [
#     [1, "ALIKA “Bridges”"],
#     [2, "Anett x Fredi “Read Between The Lines”"],
#     [3, "villemdrillem “leekiv armastus”"],
#     [4, "Clicherik & Mäx “PAKSUD”"],
#     [5, "nublu “ära ärata”"],
#     [6, "NOËP “Move Your Feet”"],
#     [7, "Trad.Attack! “Bring It On”"],
#     [8, "Bedwetters “It Is What It Is”"],
#     [9, "Reket “Panama paberid”"],
#     [10, "Grete Paia “Võluväel”"]
# ]

# print(laulud)
# laulud = (input("Millist lugu soovid? "))
# print(*laulud)



# ÜL7.2

# # Antud loend
# loend = ["jaanuar", -16, -12, -15, -20, 0, -1, -20, -2, -20, -14, -18, -8, 2, -1, -14, -7, -15, -17, -6, -17, -17, -7, 0, 3, -20, -17, -15, -8, -12, 3]

# # Kuvame mõõdetava kuu nimetuse
# kuu_nimi = loend[0]
# print(f"Mõõdetav kuu on: {kuu_nimi}")  # Kuvab: jaanuar

# # Kuvame viimase mõõtmise tulemuse
# viimane_mootmine = loend[-1]
# print(f"Viimase mõõtmise tulemus: {viimane_mootmine}")  # Kuvab viimase temperatuuri

# # Kuvame ainult temperatuurid (kõik peale esimese elemendi, mis on kuu nimi)
# temperatuurid = loend[1:]
# print(f"Kuu temperatuurid: {temperatuurid}")  # Kuvab kõik temperatuurid peale kuu nime

# # Leia kuu maksimaalne ja minimaalne temperatuur
# max_temp = max(temperatuurid)
# min_temp = min(temperatuurid)
# print(f"Kuu maksimaalne temperatuur: {max_temp}")  # Kuvab maksimumtemperatuuri
# print(f"Kuu minimaalne temperatuur: {min_temp}")  # Kuvab miinimumtemperatuuri

# # Leia kuu keskmine temperatuur
# keskmine_temp = sum(temperatuurid) / len(temperatuurid)
# print(f"Kuu keskmine temperatuur: {keskmine_temp:.2f}")  # Kuvab keskmise temperatuuriga täpsusega 2 komakohta

# # Mitu korda esines -20 kraadi
# miinus_20_kordi = temperatuurid.count(-20)
# print(f"-20 kraadi esines: {miinus_20_kordi} korda")  # Kuvab mitu korda -20 kraadi esines

# # Eemalda element nr 5 (element indeksiga 4, sest loendid algavad nullist)
# eemaldatud_temp = temperatuurid.pop(4)
# print(f"Eemaldatud temperatuur indeksil 5: {eemaldatud_temp}")  # Kuvab eemaldatud temperatuuri

# # Lisa 5. elemendi kohale temperatuur, mis on minu vanus (näiteks 25)
# temperatuurid.insert(4, 25)
# print(f"Uuendatud temperatuurid (vanus lisatud): {temperatuurid}")  # Kuvab uuendatud loendi

# # Sorteeri temperatuurid kasvavas järjekorras
# temperatuurid.sort()
# print(f"Sorteeritud temperatuurid: {temperatuurid}")  # Kuvab sorteeritud loendi

# ÜL9.1

# for i in range(1, 21):
#     print(i)

# ÜL9.2

# import random
# for i in range(20):
#     arvud = random.randint(1, 101)
#     print(arvud)





# ÜL9.3

# arvud = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]

# paaris = []
# paaritud = []
# for nr in arvud:
#     if nr%2==0:
#         paaris.append(nr)
#     else:
#         paaritud.append(nr)
    
# print("Paaris arvud: ", paaris)
# print("Paaritud: ", paaritud)
# print("Paaris arvud kokku: ", sum(paaris))
# print("Paaris arvud kokku: ", sum(paaritud))


# ÜL9.4

# for i in range(1,43):
#     if i%3==0 and i%5==0:
#         print(f"{i} TIK")
#     elif i%3==0:
#         print(f"{i} TAK")
#     elif i%5==0:
#         print(f"{i} TIKTAK")
#     else:
#         print(i)

# ÜL9.5
    
# for i in range(200, 321):
#     if i%7==0:
#         print(i, end = " Jaguneb 7-ga" )
#     elif i%5!=0:
#         print(i, end = " Ei jagune 5-ga" )

# ÜL9.6

# nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']

# unikaalsed_nimed = list(set(nimed))
# print(unikaalsed_nimed)


# ÜL9.7

# ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]

# hinded = [float(info.split()[1]) for info in ryhma_hinded]

# parim_hinne = max(hinded)
# kehvem_hinne = min(hinded)

# keskmine_hinne = sum(hinded) / len(hinded)

# print(f"Parim hinne rühmas: {parim_hinne}")
# print(f"Kehvem hinne: {kehvem_hinne}")
# print(f"Rühma keskmine hinne: {keskmine_hinne:.2f}")


# ÜL9.8

# for i in range(11):
#     print(f"{i} * {i} = {i * i}")


# ÜL9.9

# import random

# try:
#     tehted = ['+', '-', '*', '/']
#     oiged_vastused = 0
#     kordused = 10

#     for _ in range(kordused):
#         arv1 = random.randint(1, 10)
#         arv2 = random.randint(1, 10)

#         tehe = random.choice(tehted)

#         if tehe == '+':
#             oige_vastus = arv1 + arv2
#         elif tehe == '-':
#             oige_vastus = arv1 - arv2
#         elif tehe == '*':
#             oige_vastus = arv1 * arv2
#         elif tehe == '/':
#             if arv2 != 0:
#                 oige_vastus = arv1 / arv2
#             else:
#                 continue

#         print(f"{arv1} {tehe} {arv2}=")

#         try:

#             tehte_vastus = float(input("Mis on tehte vastuseks?: "))

#             if round(tehte_vastus, 2) == round(oige_vastus, 2):
#                 print("Õige vastus")
#                 oiged_vastused += 1
#             else:
#                 print(f"Vale vastus! Õige vastus on: {oige_vastus:.2f}")
            
#         except ValueError:
#             print("Palun sisesta õige nr!")

#     if oiged_vastused >= kordused / 2:
#         hinne = "A"
#     else:
#         hinne = "MA"
#     print(f"Said {oiged_vastused}/{kordused} vastust õigesti. Hinne on: {hinne}")

# except Exception as e:
#     print(f"Viga: {e}")










