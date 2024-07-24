""" Reverse the list with out using built in functions"""
my_list = list(map(int,input().split()))
n=len(my_list)
for i in range(0,n//2+1):
    my_list[i],my_list[n-i-1]=my_list[n-i-1],my_list[i]
print(*my_list)

# li =my_list[::-1]
# print(*li)