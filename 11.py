# def liitmine(a, b):
#     c = a+ b
#     print(c)
#     return c

# nr = 10
# nr2 = 20

# s = liitmine(liitmine(nr, nr2), 100)
# print(s)


def pikim_sona(s):
    sona = ""
    for i in s:
        if len(sona)<len(i):
            sona=i
    print("Pikim sõna on: " +sona)

sonad = ["Viisnurk", "ring", "ruut", "suvaline"]
pikim_sona(sonad)