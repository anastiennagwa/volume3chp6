#36 in cds
m = [3.65*10**-29, 4.00*10**-29, 5.55*10**-29,2.77*10**-29, 3.20*10**-29]
h = 6.626*10**-34
c = 3*10**8 
lamda = [ h/x for x in m]
lamda1 = [2*3.14* h/x for x in m]
lamda2 = [ h/(2*3.14*x) for x in m]
lamda4 = [(x+y)/2 for x,y in zip(lamda,lamda1)]
lamda3 = [(x+y)/2 for x,y in zip(lamda2,lamda1)]

for i in range(len(m)):
    print("%.4E" %m[i],"  ", "%.4E" %lamda[i], "%.4E" %lamda1[i], "%.4E" %lamda2[i], "%.4E" %lamda3[i], "%.4E" %lamda4[i])




