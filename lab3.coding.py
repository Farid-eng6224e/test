import math
x=1
epsilon=0.01
n=1
a=math.sin(2*x)
sum=a
while abs(a)>=epsilon:
    n+=1
    a=math.sin(2*n*x)/(2*n-1)
    sum+=a
print(sum)