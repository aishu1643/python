#Alice Problem
p=int(input())
r=float(input())
t=int(input())
i=(p*t*r)/100
ttl=(p+i)
d=(i*2)/100
fs=ttl-d
print("{:.2f}".format(i))
print("{:.2f}".format(ttl))
print("{:.2f}".format(d))
print("{:.2f}".format(fs))

#Each saturday
a=int(input())
b=int(input())
c=int(input())
p=(a*b)-(a*c+100)
print(p)

#Harry potter problem
n=int(input())
n=abs(n)
f=n//1000
l=n%10
print(f+l)

#Team dividing 
a=int(input())
b=int(input())
t=a//b
l=a%b
print("The friends in each team is",t,"and left is ",l)

#Rabbit hops
import math
x=3
y=4
x1=int(input())
y1=int(input())
res=math.sqrt(((x1-x)*(x1-x))+((y1-y)*(y1-y)))
print(int(res))

#Kamal currency system
d1=int(input())
c1=int(input())
d2=int(input())
c2=int(input())
td=(d1+d2)+(c1+c2)//100
tc=(c1+c2)%100
print(td)
print(tc)

#Treasure Hunt Pirates
tg=int(input())
lbs=int(input())
bbs=int(input())
lbc=(tg*lbs)//100
rg=tg-lbc
bbc=(rg*bbs)//100
rg=(rg-bbc)
rps=rg//3
print(lbc)
print(bbc)
print(rps)

#Tic Tac Toe 
n=int(input())
r=(n-1)//3
c=(n-1)%3
print(r,",",c)

#Electricity board
u=int(input())
if (u<=200):
    print("Rs.",int(u*0.5))
elif(u<=400):
    print("Rs.",int(u*0.65)+100)
elif(u<=600):
    print("Rs.",int(u*0.80)+200)
else:
    print("Rs.",int(u*1.25)+425)

#To check whether the given input is vowel is or not
ch=input()
list1=['a','e','i','o','u','A','E','I','O','U']
if ((ch<='a' and ch>='z') or (ch<='A' and ch>='Z')):
    if ch in list1:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Input")

#Online Shopping
fsp=int(input())
fd=int(input())
fsc=int(input())
ssp=int(input())
sd=int(input())
ssc=int(input())
asp=int(input())
ad=int(input())
asc=int(input())
ffp=fsp-(fsp*fd)//100+fsc
sfp=ssp-(ssp*sd)//100+ssc
afp=asp-(asp*ad)//100+asc
print("in Flipkart Rs.",ffp)
print("in SnapDeal Rs.",sfp)
print("in Amazon Rs.",afp)
if (ffp<=sfp and ffp<=afp):
    print("Choose Flipkart")
elif (sfp<=afp and sfp<ffp):
    print("Choose SnapDeal")
else:
    print("Choose Amazon")

#Hotel Time , Rent , No.of days
m=int(input())
r=int(input())
n=int(input())
pm=[4,5,6,11,12]
if (m>=1 and m<=12):
    if m in pm:
        print(r*n+((r*n)*20)//100)
    else:
        print(r*n)
else:
    print("Invalid input")

#Cricket Match SRH Vs CSK
tb=int(input())
tr=int(input())
rs=int(input())
bb=int(input())
to=tb//6
co=(bb//6)+(bb%6)*0.1
crr=rs/co
trr=tr/to
print(to)
print(co)
print("{:.1f}".format(crr))
print("{:.1f}".format(trr))
if (crr>=trr):
    print("Eligible to win")
else:
    print("Not eligible to win")