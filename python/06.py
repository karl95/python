"""Ül6"""
import turtle
import math

nurk = 53
korgus = 4.4
rad = math.radians(nurk)
kaugus = korgus / math.tan(rad)
C = math.sqrt(math.pow(kaugus,2) + math.pow(korgus,2))

print(C)

kordaja = 50
turtle.fd(kaugus*kordaja)
turtle.lt(90)
turtle.fd(korgus*kordaja)
turtle.rt(360-143)
turtle.fd(C*kordaja)

turtle.done()