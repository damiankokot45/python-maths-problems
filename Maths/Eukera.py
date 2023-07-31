from math import exp
#1
p=100
r=.20
t=2.0
n=12
a=p*(1+(r/n))**(n*t)
#print(a)
#2
c=p*exp(r*t)
print(c)