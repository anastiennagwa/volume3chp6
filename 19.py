#n156,p302
v = [0.23, 0.5, 0.1, 0.66, 0.12]
h = 6.626*10**-34
c = 3*10**8 
mp = 940
lamda = [ h/(x*c*mp) for x in v]
lamda1 = [ h/(c*mp) for x in v]
lamda2 = [ h/(2*3.14*x*c*mp) for x in v]
lamda3 = [ h/(x*c) for x in v]
lamda4 = [ h/(x*c*mp) for x in v]
gamma = [1/(1-x**2)**0.5 for x in v]
ke = [ (y-1)*mp*(c)**2 for y in(gamma)]
ke1 = [ 0.5*mp*(x*c)**2 for x in v]
ke2 = [ h*c/(x) for x in lamda]
ke3 = [ 0.5*mp*c**2 for x in v]
ke4 = [  h*c/(x) for x in lamda1]


for i in range(len(v)):
    print("%.4E" %v[i])
    print("%.4E" %lamda[i], "%.4E" %lamda1[i], "%.4E" %lamda2[i], "%.4E" %lamda3[i], "%.4E" %lamda4[i])
    print ("%.4E" %ke[i], "%.4E" %ke1[i],"%.4E" %ke2[i],"%.4E" %ke3[i],"%.4E" %ke4[i])
