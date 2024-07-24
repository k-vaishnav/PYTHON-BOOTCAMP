# 1.find even or odd
# 2.find greatest of 3
# 3.find the sum of all elemnts in array
# 4.find peak element in an array
# 5.find second max elemnt in array
# 6.reverse an array with out using built in functions
# 7.find max ele from array
# 8.find the sum of squares of given number
# 9.find sum of squares of even and odd digits
# 10.check whether given number is palindrome or not
# 11.write a proram to print first n fibonacii series

# 1 even or odd
# n=int(input())
# if(n%2 == 0):
#     print("even")
# else:
#     print("odd")

# # 2.greatest of 3
# a,b,c =map(int,input().split())
# if a>b and a>c:
#      print(f"greatest is {a}")
# elif b>c and b<a : print(f"greatest is {b}")
# else:print(f"greatest is c")


# # 8.sum of squares of given number
# n=int(input())
# sum=0
# while n>0:
#     rem=n%10
#     sum+=rem**2
#     n=n//10
# print(sum)
   
# # peak elemnt done in java

# # 5.second max elemnt
# my_list = list(map(int,input().split()))
# fmax=my_list[0]
# smax=my_list[1]
# for i in range(1,len(my_list)):
#     if fmax<my_list[i]:
#         smax=fmax
#         fmax =my_list[i]
# print(smax)
# """ 6.Reverse the list with out using built in functions"""
# my_list = list(map(int,input().split()))
# n=len(my_list)
# for i in range(0,n//2+1):
#     my_list[i],my_list[n-i-1]=my_list[n-i-1],my_list[i]
# print(*my_list)


# first n fibobacci series
fnum=0
snum=1
tnum=fnum+snum
n=int(input())
while n!=0:
    print(tnum,end="-")
    fnum=snum
    snum=tnum
    tnum=fnum+snum
    n-=1
print()
