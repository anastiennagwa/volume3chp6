#n120, p300
lamda = [0.03*10**-9, 0.56*10**-9, 2.3*10**-9, 0.15*10**-9, 0.07*10**-9]
h = 6.626*10**-34
c = 3*10**8 
me = 9.10938356*10**-31
ev2j= 1.602*10**-19
ke = [(h/x)**2 /(2*me*ev2j) for x in lamda]# all in eV
ke1 = [h/(x*ev2j)*c for x in lamda]
ke2 = [(h/x) /(2*me) for x in lamda]
ke3 = [(h/x) /(me) for x in lamda]
ke4 = [(h/x)**2 /(me*ev2j) for x in lamda]

for i in range(len(lamda)):
    print("%.4E" %lamda[i],"  ", "%.4E" %ke[i], "%.4E" %ke1[i], "%.4E" %ke2[i], "%.4E" %ke3[i], "%.4E" %ke4[i])
