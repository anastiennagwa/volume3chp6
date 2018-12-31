#n134, p301
w = [ 2.9, 2.4, 4.6, 4.1, 5]
elementn = ['ca', 'na', 'si', 'mn', 'c']
ev2j = 1.602*10**-19
h = 6.626*10**-34
c = 3*10**8 
me = 9.1093835*10**-31
lamda = [500*10**-9, 400*10**-9, 200*10**-9, 220*10**-9,100*10**-9 ]
v= [ ((-x*ev2j + h*c/y)/(0.5*me))**0.5 for x,y in zip(w,lamda)]
v1= [ (-x*ev2j + h*c/y)/me for x,y in zip(w,lamda)]
v2= [ ((-x*ev2j + h*c/y)/me)**0.5 for x,y in zip(w,lamda)]
v3= [ ((-x*ev2j + h*c/y)/me )for x,y in zip(w,lamda)]
v4= [ (( -x* ev2j + h*c/y)/0.5*me) for x,y in zip(w,lamda)]


for i in range(len(w)):
    print( elementn[i], w[i])
    print( "%.4E" %v[i],"%.4E" %v1[i],"%.4E" %v2[i],"%.4E" %v3[i],"%.4E" %v4[i])
