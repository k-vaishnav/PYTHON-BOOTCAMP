"""find the maximum elemnt in a given list
TEST CASE:0
12 23 36 44 45 57
o/p:57
------------------------
TEST CASE:1
56 78 -8 12 34 -99
o/p:78
"""
my_list = list(map(int,input().split()))
max=my_list[0]
for i in range(1,len(my_list)):
    if max<my_list[i]:max =my_list[i]
print(max)