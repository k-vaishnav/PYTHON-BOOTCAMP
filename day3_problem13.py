""" replace the elemnts in an array with average of maximum and minimum elemnt
TEST CASE:0
13 2 67 20 66
o/p: 35 35 35 35 35
------------------------
 """
my_list = list(map(int,input().split()))
mini=my_list[0]
maxi =my_list[0]
for i in range(1,len(my_list)):
    if mini>my_list[i]:mini=my_list[i]
    if maxi<my_list[i]:maxi =my_list[i]
ele =mini+maxi//2
for i in range(len(my_list)):
    my_list[i]=ele
print(my_list)
