import numpy
import matplotlib.pyplot

S = 0.99
E = 0.01
I = 0
R = 0
b = 1/9
o = 1
y = 0.1

t0 = 0
tf = 600
x = numpy.linspace(t0, tf, 6001)
h = x[1]-x[0]

def Sp(b,I,S):
    return -b*I*S
def Ep(b,I,S,o,E):
    return b*I*S - o*E
def Ip(o,E,y,I):
    return o*E - y*I
def Rp(y,I):
    return y*I

def F1S (h):
    return h * Sp(b,I,S)
def F2S (h):
    return h * (Sp(b,I,S) + (F1S(h)/2))
def F3S (h):
    return h * (Sp(b,I,S) + (F2S(h)/2))
def F4S (h):
    return h * (Sp(b,I,S) + F3S(h))

def F1E (h):
    return h * Ep(b,I,S,o,E)
def F2E (h):
    return h * (Ep(b,I,S,o,E) + (F1E(h)/2))
def F3E (h):
    return h * ((Ep(b,I,S,o,E)) + (F2E(h)/2))
def F4E (h):
    return h * (Ep(b,I,S,o,E) + F3E(h))

def F1I (h):
    return h * Ip(o,E,y,I)
def F2I (h):
    return h * (Ip(o,E,y,I) + (F1I(h)/2))
def F3I (h):
    return h * (Ip(o,E,y,I) + (F2I(h)/2))
def F4I (h):
    return h * (Ip(o,E,y,I) + F3I(h))

def F1R (h):
    return h * Rp(y,I)
def F2R (h):
    return h * (Rp(y,I) + (F1R(h)/2))
def F3R (h):
    return h * (Rp(y,I) + (F2R(h)/2))
def F4R (h):
    return h * (Rp(y,I) + F3R(h))

def Snext():
    return S + (F1S(h) + (2*F2S(h)) + (2*F3S(h)) + F4S(h))/6
def Enext():
    return E + (F1E(h) + (2*F2E(h)) + (2*F3E(h)) + F4E(h))/6
def Inext():
    return I + (F1I(h) + (2*F2I(h)) + (2*F3I(h)) + F4I(h))/6
def Rnext():
    return R + (F1R(h) + (2*F2R(h)) + (2*F3R(h)) + F4R(h))/6

out = [[S,E,I,R]]

for i in x:
    print(i,S,E,I,R)
    Snew = Snext()
    Enew = Enext()
    Inew = Inext()
    Rnew = Rnext()
    S = Snew
    E = Enew
    I = Inew
    R = Rnew
    out.append([S,E,I,R])

outS = []
for i in out:
    outS.append(i[0])
outE = []
for i in out:
    outE.append(i[1])
outI = []
for i in out:
    outI.append(i[2])
outR = []
for i in out:
    outR.append(i[3])
R0 = (b/y)*0.99
matplotlib.pyplot.title(f"R0 = {R0}")
matplotlib.pyplot.plot(outS)
matplotlib.pyplot.plot(outE)
matplotlib.pyplot.plot(outI)
matplotlib.pyplot.plot(outR)

matplotlib.pyplot.legend(["S","E","I","R"])
matplotlib.pyplot.show()
