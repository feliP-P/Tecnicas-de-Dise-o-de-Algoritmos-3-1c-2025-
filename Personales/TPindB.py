#solución del problema B con greedy/combinatoria

import math
s1 = input()
s2 = input()
sumas1 = s1.count("+") -s1.count("-")
sumas2 = s2.count("+") - s2.count("-")
dudas2 = s2.count("?")
"""
for i in s1:
    if i == "+":
        sumas1 += 1
    else:
        sumas1 -= 1
for i in s2:
    if i == "+":
        sumas2 += 1
    elif i == "-":
        sumas2 -= 1
    else:
        dudas2 += 1
"""
dif = abs(sumas1-sumas2)
if dif>dudas2 or len(s1) != len(s2) or (dif+dudas2)%2 !=0:
    print("0.000000000")
elif dif==dudas2:
    print(f"{0.5**dudas2:.11f}")
elif dif<dudas2:
    k= (dif+dudas2)//2
    print(f"{(math.comb(dudas2,k)/(2**dudas2)):.11f}")
else:
    print("0.000000000")
