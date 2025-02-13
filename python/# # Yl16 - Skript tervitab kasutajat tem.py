# # Yl16 - Skript tervitab kasutajat tema operatsioonisüsteemi sisselogimisnime alusel
# Skript kuvab kasutajale praeguse töökataloogi tee
# Kataloogide loomine:
# Skript küsib kasutajalt, mitu kataloogi ta soovib luua
# Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)
# Kataloogi kustutamine:
# Pärast kataloogide loomist küsib skript kasutajalt, millist äsja loodud või olemasolevat kataloogi soovitakse kustutada, esitades kataloogi nime 1, 2 jne
# Kui sisestatud kataloogi nimi eksisteerib, kustutatakse see
# Kuva kuupäeva kasutas olevad kataloogid

import os
from datetime import date

print(os.name)
print(f"Tere {os.getlogin()}")
print(f"sinu rada {os.getcwd()}")

kataloogidearv = 10
kustuta = 5 #kustutab viienda kausta
kp = str(date.today())
try:
    os.mkdir(kp)
    print(f"{kp} kaust loodud")
    for i in range(1, kataloogidearv):
        os.mkdir(str(i))
except:
    print("kataloog juba olemas")

#KUSTUTAB KAUSTA

# os.rmdir(str(kustuta))

#kuvab kataloogi sisu
dir_list = os.listdir(kp)
print("Kataloogi sisu: ")
for i in dir_list:
    print(i)







