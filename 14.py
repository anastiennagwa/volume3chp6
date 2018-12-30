n114, p300
lamda = [5.8*10**-15,4*10**-15,29*10**-15,33*10**-15,57*10**-15]
h = 6.626*10**-34
c = 3*10**8 
mp = 1.67262*10**-27

v  = [h/(mp*x*c) for x in lamda]
v1 = [h/(mp*2*3.14*x*c) for x in lamda]
v2 = [h/(0.5*mp*x*c) for x in lamda]
v3 = [(x+y)/2 for x,y in zip(v2,v1)]
v4 = [(x+y)/2 for x,y in zip(v,v1)]

for i in range(len(lamda)):
    print("%.4E" %lamda[i],"  ", "%.4E" %v[i], "%.4E" %v1[i], "%.4E" %v2[i], "%.4E" %v3[i], "%.4E" %v4[i])
