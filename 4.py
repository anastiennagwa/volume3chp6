#24 in cds
w = [ 2.9, 2.4, 4.6, 4.1, 5]
lamda = [300*10**-9, 350*10**-9, 250*10**-9,230*10**-9, 240*10**-9]
elementna = ['ca', 'na', 'si', 'mn', 'c']
ev2j = 1.602*10**-19
h = 6.626*10**-34
c = 3*10**8 
wj  = [ (ev2j*a) for a in w ]
wj1 = [ (a) for a in w ]

ee  = [h*c/a for a in lamda]
ee1 = [h*c/a for a in lamda]
ee2 = [h*c/a for a in lamda]
ee3 = [h*c/a for a in lamda]
ee4 = [h*c/a for a in lamda]

print(wj,ee)
dele = [ a-b for a,b in zip(ee,wj)]
for i in range(len(w)):
    print( elementna[i],"  ",w[i],"  ", "%.4E" %lamda[i],"  ", "%.4E" %dele[i])

