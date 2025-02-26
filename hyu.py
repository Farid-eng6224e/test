
#lab1
import math
t=(0.836**(1/3))*math.cos(7)+(2.324**(1/4))*math.sin(7)
g=math.cos(-1/(2**(1/2))*(math.atan(3)-math.atan(2)))
if max(t,g)>10:
    k=(math.log(3))*(math.log(abs(t)+abs(g)))
elif max(t,g)<=10:
    k=math.exp(t+g)
print(k)
