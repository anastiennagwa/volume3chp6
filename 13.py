#n110,p300
m = [70,25,30,4,6]
v= [6.5, 20, 3, 0.5,10]
h = 6.626*10**-34
lamda = [h/(x*y) for x,y in zip(m,v)]
lamda1 = [2*3.14*h/(x*y) for x,y in zip(m,v)]
lamda2 = [h/(x*y) for x,y in zip(m,v)]
lamda3 = [h*(x*y) for x,y in zip(m,v)]
lamda4 = [h/(2*3.14*x*y) for x,y in zip(m,v)]
for i in range(len(v)):
    print("%.4E" %v[i],"%.4E" %m[i],"  ","%.4E" %lamda[i], "%.4E" %lamda1[i], "%.4E" %lamda2[i], "%.4E" %lamda3[i], "%.4E" %lamda4[i])
