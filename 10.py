#41 in cds
lines = ["the fifth line in Balmer series",
"the fourth line in Balmer series",
"the third line in Balmer series",
"the seventh line in Balmer series",
"the ninth line in Balmer series"]
nf=2
ni = [7,6,5,9,11]
h = 6.626*10**-34
rh=1.09737*10**7
c = 3*10**8 
me = 9.10938356*10**-31
lamda = [(rh*(1/(nf**2)-1/(x**2)))**-1 for x in ni]
lamda1 = [(rh*(1/((nf+1)**2)-1/((x+1)**2)))**-1 for x in ni]
lamda2 = [(rh*(1/(nf**2)-1/((x-1)**2)))**-1 for x in ni]
lamda3 = [(rh*(1/(nf**2)-1/((x+1)**2)))**-1 for x in ni]
lamda4 = [(rh*(1/(nf+1)**2-1/(x**2)))**-1 for x in ni]

for i in range(len(lamda)):
    print(lines[i],"  ", "%.4E" %lamda[i], "%.4E" %lamda1[i], "%.4E" %lamda2[i], "%.4E" %lamda3[i], "%.4E" %lamda4[i])

