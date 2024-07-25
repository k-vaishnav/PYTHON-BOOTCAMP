"""print leap years in a range"""
n1=int(input())
n2=int(input())
for n in range(n1,n2+1):
    if n%400==0:
        print(n,end=" ")
    elif n%4==0 and n%100!=0:
        print(n,end=" ")
        