#32 in cds
lamda = [600*10**-9, 350*10**-9, 700*10**-9,230*10**-9, 400*10**-9]
h = 6.626*10**-34
c = 3*10**8 
p = [ h/x for x in lamda]
p1 = [2*3.14* h/x for x in lamda]
p2 = [x/h for x in lamda]
p3 = [(x+y)/2 for x,y in zip(p,p1)]
p4 = [[(x+y)/2 for x,y in zip(p2,p1)]]

for i in range(len(lamda)):
    print("%.4E" %lamda[i],"  ", "%.4E" %p[i], "%.4E" %p1[i], "%.4E" %p2[i])





