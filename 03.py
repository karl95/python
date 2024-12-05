#https://www.metshein.com/course/python-turtle-graphics/?action=curriculum // ülesanne 3 // ITS24 Karl-Gustav Kessel

nimi = "Karin Eegreid" #sõne, string
vanus = 20 #int, integet, täisarv
keskmine_hinne = 6.5 #koma-arv, float
#plussiga saan stringid kokku
print(nimi+","+str(vanus)+"aastat vana ja keskmine hinne on "+str(keskmine_hinne))
#komaga saan mitu asja printida
print(nimi,",",vanus,"aastat vana ja keskmine hinne on",keskmine_hinne)
#lause vormindamine lünkadega
print(f"{nimi}, {vanus} aastat vana ja keskmine hinne on {keskmine_hinne}")

# ül 3.2

#kolmnurk
kylje_pikkus = 300
nurk = 120

import turtle
turtle.speed(0)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.done


