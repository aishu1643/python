#Hallow square
n=int(input())
for i in range (0,n):
    for j in range (0,n):
        if (i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
    else:
        print(" ",end=" ")
    print()

#Treasure box
a=4
b=2
c=6
if (a>b and a<c) or (a<b and a>c):
    print("Treasure is in the box which has number",a)
elif ((b>a and b<c) or (b<a and b>c)):
    print("Treasure is in the box which has number",b)
else :
    print("Treasure is in the box which has number",c)
for i in range(1,9+1):
    if (a%i==0 and b%i==0 and c%i==0):
        key=i
print("The code to open the box is ",key)

#Strong Number
a=int(input())
temp=a
sum=0
while(a>0):
    d=a%10
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact
    a=a//10
if (sum==temp):
    print("Strong Number")
else:
    print("Not a Strong Number")

#Right Angle Triangle
n=int(input())
m=n
for i in range(0,n):
    for j in range(0,m):
        print("*",end=" ")
    m=m-1
    print()

#Sum of Digits
n=int(input())
sum=0
while(n>10):
    sum=sum+(n%10)
    n=n//10
    if (n==0 and sum>9):
        n=sum
        sum=0
print(sum)

#
n=int(input())
sq=n*n
temp=n
c=0
while(n>0):
    c=c+1
    n=n//10
p=10**c
q=sq//p
rem=sq%p
if ((q+rem)==temp):
    print("kaprekar")
else:
    print("kaprekar")
