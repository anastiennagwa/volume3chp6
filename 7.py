#n79, p298
#36 in cds
m = [4.02*10**-29, 3.65*10**-29, 5.55*10**-29,2.77*10**-29, 3.20*10**-29]
h = 6.626*10**-34
c = 3*10**8 
e = [ x*c for x in m]
e1 = [0.5* x*c for x in m]
e2 = [ 0.5*x**2*c for x in m]
e3 = [ x*c**2 for x in m]
e4 = [ (x+y)/2 for x,y in zip(e,e1)]

for i in range(len(m)):
    print("%.4E" %m[i],"  ", "%.4E" %e[i], "%.4E" %e1[i], "%.4E" %e2[i], "%.4E" %e3[i], "%.4E" %e4[i])
