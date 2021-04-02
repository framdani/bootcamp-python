from math import exp
t=( 0, 4, 132.42222, 10000, 12345.67)
#print("day_0"+str(t[0])+", ex_0"+str(t[1])+" : "+str(round(t[2], 2))+", "+str(exp(t[3])))
print("day_0{}, ex_0{} : {:.2f}, {:.2e}, {:.2e}".format(t[0],t[1], t[2],t[3],t[4]))

