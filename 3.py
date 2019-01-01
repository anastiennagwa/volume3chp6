#n64, p298, openstax vol3
#13 in cds
w = [ 2.9, 2.4, 4.6, 4.1, 5]
elementna = ['ca', 'na', 'si', 'mn', 'c']
ev2j = 1.602*10**-19
h = 6.626*10**-34
c = 3*10**8 
lamda = [ h*c/(ev2j*a) for a in w ]
lamda1 = [ h*c*a/(ev2j) for a in w ]
lamda2 = [ c*ev2j/a for a in w ]
lamda3 = [ h*c/(ev2j) for a in w ]
lamda4 = [ 2*3.14*h*c/(a*ev2j) for a in w ]

for i in range(len(w)):
    print( elementna[i], w[i])
    print( "%.4E" %lamda[i])
    print( "%.4E" %lamda1[i])
    print( "%.4E" %lamda2[i])
    print( "%.4E" %lamda3[i])
    print( "%.4E" %lamda4[i])
