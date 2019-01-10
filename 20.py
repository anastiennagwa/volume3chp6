#n156,p302
v = [0.4, 0.5, 0.1, 0.66, 0.12]
h = 6.626*10**-34
c = 3*10**8 
mp = 940*10**6
qp=1.60217662 * 10**-19
lamda = [ h/(x*c*mp) for x in v]
lamda1 = [ h/(c*mp) for x in v]
lamda2 = [ h/(2*3.14*x*c*mp) for x in v]
lamda3 = [ h/(x*c) for x in v]
lamda4 = [ h/(x*c*mp) for x in v]
gamma = [1/(1-x**2)**0.5 for x in v]
gamma1 = [1/(1-x)**0.5 for x in v]
ke = [ (y-1)*mp for y in gamma]
ke1 = [(y-1) for y in gamma1]
ke2 = [ h*c/(x) for x in lamda]
ke3 = [ mp for x in v]
ke4 = [  h*c/(x) for x in lamda]
volt=[x/qp for x in ke]
volt1=[x/qp for x in ke1]
volt2=[x/qp for x in ke2]
volt3=[x/qp for x in ke3]
volt4=[x/qp for x in ke4]

for i in range(len(v)):
    print("%.4E" %v[i])
    print ("%.4E" %ke[i], "%.4E" %ke1[i],"%.4E" %ke2[i],"%.4E" %ke3[i],"%.4E" %ke4[i])
    print("%.4E" %volt[i], "%.4E" %volt1[i], "%.4E" %volt2[i], "%.4E" %volt3[i], "%.4E" %volt4[i])
