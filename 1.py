f = [2490 * 10 ** 6, 2450 * 10 ** 6, 2400 * 10 ** 6, 2470 * 10 ** 6, 2420 * 10 ** 6] 
p = [850, 820, 870, 890, 770] 
h = 6.626 * 10 ** -34
e = [h*i for i in f]
e1 = [h/i for i in f]
e2 = [h*i*2*3.14 for i in f]
n = [(x*1.0)/y for x,y in zip(p,e)] #number of photon quantas
n1 = [(x*1.0)/y for x,y in zip(p,e1)]
n2 = [(x*1.0)/y for x,y in zip(p,e2)]
n3 = [(x+y)/2 for x,y in zip( n,n1)]
n4 = [(x+y)/2 for x,y in zip(n2,n1)]
m = 0.63
c = 0.890
delat=[36, 35, 34, 37, 32]
q = [m*c*x for x in delat]# in kcal
q1 = [m*c*1000*x for x in delat]# in kcal
q2 = [m*c for x in delat]# in kcal
q3 = [-m*c*(x-273) for x in delat]# in kcal
q4 = [m/c*x for x in delat]# in kcal
C2j = 4181
t= [(x*1.0*C2j)/y for x,y in zip(q,p)]#time
t1= [(x)/y for x,y in zip(q,p)]#time
t2= [(x*1.0*C2j/1000)/y for x,y in zip(q,p)]#time
t3= [(x*1.0*C2j)/y for x,y in zip(q1,p)]#time
t4= [(x*1.0*C2j)/y for x,y in zip(q3,p)]#time


for i in range(len(f)):
    print (i)
    print(p[i],"watt     ", f[i],"Hz     ", delat[i],"K")
    print (n[i],"photon     ",q[i]," kcal     ",t[i],"seconds")
    print (n1[i],"photon     ",q1[i]," kcal     ",t1[i],"seconds")
    print (n2[i],"photon     ",q2[i]," kcal     ",t2[i],"seconds")
    print (n3[i],"photon     ",q3[i]," kcal     ",t3[i],"seconds")
    print (n4[i],"photon     ",q4[i]," kcal     ",t4[i],"seconds")

