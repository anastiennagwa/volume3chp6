#lambdamax*T=2.898*10^-3
t = [700, 650, 710, 750, 670]
lamdam = [2.898*10**-3/a for a in t]#frequency
lamdam1 = [2.898*10**-3*a for a in t]#frequency
lamdam2 = [a/2.898*10**-3 for a in t]#frequency
lamdam3 = [2.898*10**-3/(a-273) for a in t]#frequency
lamdam4 = [2.898/a for a in t]#frequency

f = [ 3*10**8/l for l in lamdam]
f1 = [ 3*10**8/l for l in lamdam1]
f2 = [ 3*10**8/l for l in lamdam2]
f3 = [ 3*10**8/l for l in lamdam3]
f4 = [ 3*10**8/l for l in lamdam4]

for i in range(len(t)):
    print( "version", i,"      " ,t[i])
    print ("%E"%f[i]  )
    print ("%E"%f1[i])
    print ("%E"%f2[i] )
    print ("%E"%f3[i] )
    print ("%E"%f4[i] )
    




