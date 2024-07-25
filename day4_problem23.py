# sort elements first half in ascending order and other half in descending order
my_list = list(map(int,input().split()))
my_list.sort()
n=len(my_list)
for i in range(n//2,(n+(n//2))//2):
    my_list[i],my_list[i+(n-i-1)] = my_list[i+(n-i-1)],my_list[i]
print(*my_list)