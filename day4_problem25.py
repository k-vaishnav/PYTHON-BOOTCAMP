# write a program to print all the prime numbers in a given range
# def prime(n):
#     flag =True
#     for i in range (2,int((n**0.5))+1):
#         if(n%i==0):
#             flag=False
#             break
#     if flag:
#         print(n,end=" ")
# a=int(input())
# b=int(input())
# for i in range (a,b+1):
#     prime(i)

a=int(input())
b=int(input())

for i in range(a,b+1):
    cnt=0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            cnt+=1
            break
    if cnt==0:print(i,end=" ")
    # else:print(i,end=" ")
