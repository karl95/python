#https://www.metshein.com/course/python-turtle-graphics/?action=curriculum // ülesanne 4 // ITS24 Karl-Gustav Kessel

"""
4.4 Kingituste pakkumine ->
Sa töötad kingipoes ja sinu ülesanne on pakkida kingitusi.
Igasse kinkekarpi mahub täpselt 5 kingitust.
Sinu ülesandeks on arvutada, mitu täis kinkekasti saad teha ja mitu kingitust jääb üle, kui need kõik ei mahu karpidesse.
Loo programm, mis küsib kasutajalt, mitu kingitust on vaja pakkida.
Programm peaks seejärel arvutama, mitu täis kinkekasti saab teha ja mitu kingitust jääb üle. Kasuta täisarvulist jagamist (//) kinkekarpide arvu leidmiseks ja jäägi (%) operaatorit ülejäävate kingituste arvu leidmiseks.
Kasuta veakontrolli ja vastuse vormindamist
Näide:
Kasutaja sisestab: 23
Programm väljastab: Saad teha 4 täis kinkekasti. Üle jääb 3 kingitust.
"""
try:
    karbi_suurus = 5
    kingitused = int(input("Lisa kingutuste arv: "))
    kastid =  kingitused//karbi_suurus
    jaak = kingitused % karbi_suurus
    print(F"Saad teha {kastid} täis kinkekasti. Üle jääb {jaak} kingitust!")
except:
    print("Jälle tekitad probleeme!")

# ül 4.1 Aia pikkus
a = int(input("Sisesta külg 1: "))
b = int(input("Sisesta külg 2: "))

ymbermoot=2*(a+b)
print(f" Aia kogupikkus on {ymbermoot} meetrit.")

