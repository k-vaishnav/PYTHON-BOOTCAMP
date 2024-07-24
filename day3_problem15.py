""" Find the missing number in an array"""
my_list = list(map(int,input().split()))
n= int(input())
sum=0
for i in range(len(my_list)) :
    sum+=my_list[i]
num= (n*(n+1))//2
print(num-sum)