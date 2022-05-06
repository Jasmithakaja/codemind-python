a,b,c=map(int,input().split())
s=(a+b+c)/2
n=s*(s-a)*(s-b)*(s-c)
n=n**0.5
print("%.2f"%n)