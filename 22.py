#n136, p301, openstax vol3
w = [ 2.9, 2.4, 4.6, 4.1, 5]
elementna = ['ca', 'na', 'si', 'mn', 'c']
it = [1.42*10**3, 2.22*10**3,0.65*10**3,4.21*10**3,1.55*10**3]
a = [2.35*10**-4, 3.33*10**-4, 1.56*10**-4, 3.68*10**-4, 4.37*10**-4]
lamda = [330*10**-9, 250*10**-9, 130*10**-9, 220*10**-9, 160*10**-9]
ev2j = 1.602*10**-19
h = 6.626*10**-34
c = 3*10**8 
e = [ h*c/(a) for a in lamda ]
e1 = [ h*c/(2*3.14*a) for a in lamda ]
wj = [x*ev2j for x in w]
wj1 = w
ke = [ x-y for x,y in zip(e, wj)]
ke1 = [ -x+y for x,y in zip(e1, wj1)]
ke2 = [ x-y for x,y in zip(e, wj1)]


p = [x*y for x,y in zip(it,a)]
p1 = [x*y*10**4 for x,y in zip(it,a)]
n =[x/y for x,y in zip(p,e)]
n1 =[x/y for x,y in zip(p1,e)]
pout = [x*y for x,y in zip(n, ke)]
pout1=ke
pout2 = [x*y for x,y in zip(n1, ke)]
pout3 = [x*y for x,y in zip(n, ke1)]
pout4 = [x*y for x,y in zip(n1, ke)]

for i in range(len(w)):
    print( elementna[i], w[i],"eV  ", lamda[i], "m  ", a[i], "m^2   ",i,"w/m^2   ")
    print( "%.4E" %pout[i],"%.4E" %pout1[i],"%.4E" %pout2[i],"%.4E" %pout3[i],"%.4E" %pout4[i])
    
