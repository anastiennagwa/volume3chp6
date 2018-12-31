#n118, p300
e = [57*10**9, 90*10**9, 33*10**9, 45*10**9,12*10**9 ]
h = 6.626*10**-34
c = 3*10**8 
me = 9.10938356*10**-31
ev2j= 1.602*10**-19
g = [(x*ev2j/(me*c**2))-1 for x in e]
g1= [(x/(me*c**2))-1 for x in e]
g2 = [(x*ev2j/(me*c*2))-1 for x in e]
g3 =[(x*ev2j/(me*c))-1 for x in e] 
g4 = [(x*ev2j/(me**2*c)) for x in e]
lamda = [ h/(x*ev2j/c) for x in e]
lamda1 = [ h/(x*ev2j/c) for x in e]
lamda2 = [ h/(x*ev2j/c) for x in e]
lamda3 = [ h/(x*ev2j/c) for x in e]
lamda4 = [ h/(x*ev2j/c) for x in e]

for i in range(len(e)):
    print("%.4E" %e[i],"  ", "%.4E" %g[i], "%.4E" %g1[i], "%.4E" %g2[i], "%.4E" %g3[i], "%.4E" %g4[i])
    print("%.4E" %e[i],"  ", "%.4E" %lamda[i], "%.4E" %lamda1[i], "%.4E" %lamda2[i], "%.4E" %lamda3[i], "%.4E" %lamda4[i])
