from scipy import *
from numpy import *
from pylab import *
from random import *
import random
import matplotlib.pyplot as plt

a = -2.0
b = 2.0
c = 1.5

N = 75000

xv1 = []
yv1 = []
n = 0
xv2 = []
yv2 = []

for i in range(N):
    x = random.uniform(a, b)
    y = random.uniform(0, c)

    if y <= 1 / (1 + pow(x / 2, 2)):
        n += 1
        xv1.append(x)
        yv1.append(y)

    else:

        xv2.append(x)
        yv2.append(y)


#================== funcao ============
def f(x):
    return 1 / (1 + pow(x / 2, 2))


fv = vectorize(f)

d = arange(-4.0, 4.0, 0.01)
#======================================

Pi = (b - a) * c * float(n) / N

print Pi


#======================= cores definidas ===============================
OrangeLine = "#d07000"
YellowLine = "#d0b000"
BlueLine = "#90a0c0"
BlueLine2 = "#483D8B"
GreyLine = "black"
RedLine = "#cd5c5c"
RedLine2 = "#DC143C"
PinkLine = "#C71585"
Graycolor = "#F5F5F5"
Seagreen = "#20B2AA"
Turquesa = "#40E0D0"
Roxo = "#800080"
GreenLine = "#008080"
#==========================================================================
figure(0)
rc('text', usetex=True)

plot(d, fv(d), color=OrangeLine, lw=2.0)
plot(xv1, yv1, 'o', markersize=2.5, color=Turquesa)
plot(xv2, yv2, 'o', markersize=2.5, color=RedLine2)
plt.show()

xlim([-2.1, 2.1])
ylim([0, 1.6])

title(r'Estimativa do $\pi$', fontsize=15)

ylabel('$f(x)$', fontsize=15)
xlabel('$x$', fontsize=15)

# savefig('pontos-aleatorios.pdf')
