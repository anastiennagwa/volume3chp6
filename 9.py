#40 in cds
lines = ["the fourth line in Lyman series",
"the fifth line in Lyman series",
"the third line in Lyman series",
"the second line in Lyman series",
"the ninth line in Lyman series"]
nf=1
ni = [5,6,4,3,10]
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
