#45 in cds
lines = ["second excited state", "fourth excited state", "fifth excited state","seventh excited state","twelfth excited state "]
n = [3,5,6,8,12]
h = 6.626*10**-34
c = 3*10**8 
me = 9.10938356*10**-31
a = [5.29177*10**-11*x**2 for x in n]
a1 = [5.29177*10**-11*x for x in n]
a2 = [5.29177*10**-11/x**2 for x in n]
a3= [(x+y)/2 for x,y in zip(a,a1)]
a4 = [(x+y)/2 for x,y in zip(a1,a2)]

for i in range(len(a)):
    print(lines[i],"  ", "%.4E" %a[i], "%.4E" %a1[i], "%.4E" %a2[i], "%.4E" %a3[i], "%.4E" %a4[i])

