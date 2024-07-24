

# li=[]
# my_list = list(map(int,input().split()))
# for i in my_list:
#     if i not in li:
#         li.append(i)
# print(*li)

"""Find the duplicates in an array
i/p:8 7 7 8 5 4 4 8 9
o/p:8,7,4
"""
li=[]
du=[]
my_list = list(map(int,input().split()))
for i in my_list:
    if i not in li:
        li.append(i)
    elif i not in du:
        du.append(i)
print(*du)

