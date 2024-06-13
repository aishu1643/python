#Trendy Number
n=int(input())
m=(n%100)
m=m//10
if (n>99 and n<1000):
    if (m%3==0):
        print("Trendy Number")
    else:
        print("Not a Trendy number")
else:
    print("Invalid")

#Programming Trainer Salary
sun=int(input())
mon=int(input())
tue=int(input())
wed=int(input())
thu=int(input())
fri=int(input())
sat=int(input())
r1=sun*150
if (mon<=8):
    r2=mon*100
else:
    r2=(mon-8)*115+800
if (tue<=8):
    r3=tue*100
else:
    r3=(tue-8)*115+800
if (wed<=8):
    r4=wed*100
else:
    r4=(wed-8)*115+800
if (thu<=8):
    r5=thu*100
else:
    r5=(thu-8)*115+800
if (fri<=8):
    r6=fri*100
else:
    r6=(fri-8)*115+800
r7=125*sat
ttl=r1+r2+r3+r4+r5+r6+r7
print(ttl)

#Doremon Mango tree
rs=int(input())
cs=int(input())
tn=int(input())
if (tn<=cs or tn%cs==1 or tn%cs==0):
    print("Yes its a mango tree")
else:
    print("Not a mango tree")

#Multiplication Table
print("enter m:")
print("enter n:")
m=int(input())
n=int(input())
print("The multiplication of table no",m,"is")
for i in range(1,n+1):
    print(i,"*",m,"=",i*m)

#Prime or not
n=int(input())
c=0
for i in range(1,n+1):
    if (n%i==0):
        c=c+1
if (c==2):
    print("Prime")
else:
    print("Not prime")

#Prime numbers in Range
n=int(input())
for i in range(2,n+1):
    p=1
    for j in range(2,int(i/2)+1):
        if(i%j==0):
            p=0
    if (p==1):
        print(i,end=" ")

#Special Number
s=int(input())
e=int(input())
for i in range(s,e+1):
    sum=0
    sum=((i//10)+(i%10)+((i//10)*(i%10)))
    if sum==i:
        print(i)

#Ameoba Size
p=int(input())
a=0
b=1
sum=0
if (p==1):
    print(a)
if (p==2):
    print(b)
for i in range(3,p+1):
    sum=a+b
    a=b
    b=sum
print(sum)

#Number Series 1
n=int(input())
for i in range(1,n+1):
    if  (i%2==0):
        print((i*i)-2)
    else:
        print((i*i)-1)

#Number Series 2
n=int(input())
c=0
while(n>1):
    c=c+1
    if (n%2==0):
        n=n//2
        print(n,end=" ")
    else:
        n=n*3+1
        print(n,end=" ")
print(c)
