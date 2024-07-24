"""find the minimum elemnt in a given list
TEST CASE:0
12 23 36 44 45 57
o/p:12
------------------------
TEST CASE:1
56 78 -8 12 34 -99
o/p:-99
"""
my_list = list(map(int,input().split()))
mini=my_list[0]
for i in range(1,len(my_list)):
    if mini>my_list[i]:mini=my_list[i]
print(mini)