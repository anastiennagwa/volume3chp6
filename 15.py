#n116, p300
v = [3.4*10**-2, 5*10**-2, 7.9*10**-2, 9*10**-2, 2*10**-2]
h = 6.626*10**-34
c = 3*10**8 
mp = 1.67262*10**-27

lamda = [h/(mp*x*c) for x in v]
lamda1 = [h/(mp*2*3.14*x*c) for x in v]
lamda2 = [h/(0.5*mp*x*c) for x in v]
lamda3 = [(x+y)/2 for x,y in zip(lamda2,lamda1)]
lamda4 = [(x+y)/2 for x,y in zip(lamda,lamda1)]

for i in range(len(v)):
    print("%.4E" %v[i],"  ", "%.4E" %lamda[i], "%.4E" %lamda1[i], "%.4E" %lamda2[i], "%.4E" %lamda3[i], "%.4E" %lamda4[i])
