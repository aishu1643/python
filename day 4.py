#Puzzle Game
a=[]
n=int(input())
for i in range(0,n):
    e=int(input())
    a.append(e)
print(a)
sum1=0
sum2=0
for i in a:
    if(i%2==0):
        sum1+=i
    else:
        sum2+=i
print(sum1)
print(sum2)

#Puzzle Game method -2
n=int(input())
if (n<15):
    arr=list(map(int(input().split())))
    esum=0
    osum=0
    for i in range(n):
        if (arr[i]%2==0):
            esum=esum+arr[i]
        else:
            osum=osum+arr[i]
    print("even sum is",esum)
    print("odd sum is",osum)

#Distinct Numbers
n=int(input())
l=[(int(input().strip())) for i in range(n)]
el=[]
for i in range(n):
    if l[i] not in el:
        el.append(l[i])
print("there are",len(el),"distinct elements are present in the list")

#Ascending order
n=int(input())
l=[(int(input().strip())) for i in range(n)]
temp=0
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)

#Array Insertion
n=int(input())
arr=list(map(int,input().split()))
p=int(input())
e=int(input())
if p<=n:
    for i in range(e):
        if i==p:
            arr.insert(p-1,e)
else:
    print("Game Over")
print(arr)

#Factorial
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))

#Code and decoding
s=(input())
l=[*s]
l2=[]
for i in range(len(l)):
    l2.append(ord(l[i])-1)
for i in range(len(l)):
    print(chr(l2[i]),end="")

#a^n using Recursion
def exp(s,n):
    if (s==0 or s==1):
        return 1
    else:
        return s**n
s=int(input())
n=int(input())
print(exp(s,n))

#a^n using Recursion method - 2
def power(a,n):
    if(n==0):
        return 1
    elif(n==1):
        return a
    elif(a%2==1):
        return a*power(a,n-1)
    else:
        return (a*a,n//2)
a=int(input())
n=int(input())
print(power(a,n))

#fibonacci series using recurison
def fab(n):
    if (n==1):
        return 0
    if (n==2):
        return 1
    return fab(n-1)+fab(n-2)
n=int(input())
print(fab(n))

#Chocolate Jam
arr=list(map(int,input().split()))
j=int(input())
c=0
for i in arr:
    if i==0:
        continue
    elif i<=3:
        c=c+1
    else:
        if i%3==0:
            c=c+(i//3)
        else:
            c=c+(i//3)+1
print(c)
