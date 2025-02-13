# Ülesanne 17
# Pangakonto – pangakonto.txt
# Sinu ülesandeks on kirjutada Pythoni skript, mis loeb andmeid failist pangakonto.txt. Fail sisaldab eraldi ridadel pangatehingute summasid: positiivsed summad tähistavad sissetulekuid ja negatiivsed summad väljaminekuid. Skript peab arvutama ja väljastama:
# kogu tehingute arvu
# positiivsete tehingute arvu
# positiivsete tehingute kogusumma
# Tulemused tuleb väljastada konsooli
# Palgastatistika – palgad.txt
# Kirjuta Pythoni skript, mis loeb failist palgad.txt töötajate andmed ja arvutab eraldi
# meeste keskmised töötunnid, töötasu ning palk
# naiste keskmised töötunnid, töötasu ning palk
# Tulemused prindi konsooli

#ESIMENE ÜLESANNE

# tehingute_arv = 0
# tehingute_arv_pos = 0
# pos_arv_summa = 0


# with open("pangakonto.txt") as fail:
#     sisu = fail.readlines()
#     for number in sisu:
#         # print(float(number)) 
#         tehingute_arv+=1
#         if float(number) > 0:
#             tehingute_arv_pos+=1
#             tehingute_arv_pos += float(number)

# print(f"tehingute arv: {tehingute_arv}")
# print(f"Positiivsete tehingute arv: {tehingute_arv_pos}")
# print(f"Positiivsete arvude summa: {pos_arv_summa:.2f}")

#Järgmine ülesanne
with open("palgad.txt") as fail:
    sisu = fail.readlines()
    for i in sisu:
        print(i, end="")








