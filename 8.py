#n84, p 299
#37 in cds
lamda = [3.1*10**-6, 10*10**-6, 30*10**-6,0.5*10**-6, 15*10**-6]
h = 6.626*10**-34
c = 3*10**8 
me = 9.10938356*10**-31
p = [ h/x for x in lamda]
p1 = [2*3.14*h/x for x in lamda]
p2 = [ h/(x*2*3.14) for x in lamda]
p3 = [ (x+y)/2 for x,y in zip(p,p1)]
p4 = [ (x+y)/2 for x,y in zip(p2,p1)]
v = [x/me for x in p]
v1 = [x/me for x in p1]
v2 = [x/me for x in p2]
v3 = [2*x/me for x in p]
v4 = [(x+y)/2 for x,y in zip(v2,v1)]
ke = [ 0.5*me*x**2 for x in v]
ke1 = [ 0.5*me*x**2 for x in v1]
ke2 = [ 0.5*me*x**2 for x in v2]
ke3 = [ 0.5*me*x**2 for x in v4]
ke4 = [ (x+y)/2 for x,y in zip(ke2,ke1)]
for i in range(len(lamda)):
    print("%.4E" %lamda[i],"  ", "%.4E" %p[i], "%.4E" %p1[i], "%.4E" %p2[i], "%.4E" %p3[i], "%.4E" %p4[i],"  ", "%.4E" %v[i], "%.4E" %v1[i], "%.4E" %v2[i], "%.4E" %v3[i], "%.4E" %v4[i],"  ", "%.4E" %ke[i], "%.4E" %ke1[i], "%.4E" %ke2[i], "%.4E" %ke3[i], "%.4E" %ke4[i])
