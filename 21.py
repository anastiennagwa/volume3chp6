#n142 ,p301
from math import sin, cos, tan,pi
e = [4.98*10**3, 2*10**3, 3.34*10**3, 6.87*10**3,2.44*10**3 ]
thetdeg = [58, 45, 33, 21, 10]
theta = [x*pi/180 for x in thetdeg]
h = 6.626*10**-34
c = 3*10**8 
ev2j= 1.602*10**-19
me = 9.10938356*10**-31
dl = [h/(me*c)*(1-cos(x)) for x in theta]
print (dl)
dl1 = [h/(2*3.14*me*c)*(1-cos(x)) for x in theta]
dl2 = [h/(me*c)*(1-sin(x)) for x in theta]
dl3 = [h/(me*c)*(1-tan(x)) for x in theta]
dl4 = [h/(me*c)*(cos(x)) for x in theta]
lamdao = [h*c/(x*ev2j) for x in e]
lamda = [ x+y for x,y in zip(dl,lamdao)]
lamda1 = [ x+y for x,y in zip(dl1,lamdao)]
lamda2 = [x+y for x,y in zip(dl2,lamdao)]
lamda3 = [x+y for x,y in zip(dl3,lamdao)]
lamda4 = [x+y for x,y in zip(dl4,lamdao)]

de = [x - h*c/(y*ev2j)for x,y in zip(e,lamda)]
de1= [x - h*c/(y*ev2j) for x,y in zip(e,lamda)]
de2 = [x - h*c/(y*ev2j) for x,y in zip(e,lamda)]
de3 =[x - h*c/(y*ev2j) for x,y in zip(e,lamda)] 
de4 = [x - h*c/(y*ev2j) for x,y in zip(e,lamda)]
for i in range(len(e)):
    print("%.4E" %e[i])
    print("%.4E" %de[i],"  ", "%.4E" %de1[i], "%.4E" %de2[i], "%.4E" %de3[i], "%.4E" %de4[i])
