#numer 106, page 299
lamda = [2.11, 5, 1, 0.05, 15]
h = 6.626*10**-34
c = 3*10**8 
me = 9.10938356*10**-31
v = [ h/(x*me) for x in lamda]
v1 = [ x*h/(me) for x in lamda]
v2 = [ x*h/(x*me) for x in lamda]
v3 = [ 2*3.14*h/(x*me) for x in lamda]
v4 = [ h/(2*3.14*x*me) for x in lamda]

for i in range(len(v)):
    print("%.4E" %lamda[i],"  ", "%.4E" %v[i], "%.4E" %v1[i], "%.4E" %v2[i], "%.4E" %v3[i], "%.4E" %v4[i])

