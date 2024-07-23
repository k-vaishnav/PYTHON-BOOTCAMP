# # you are given with a comma seperated natural numbers 1 to 100 print only even numbers
# my_list = list(map(int,input().split(",")))
# for i in range(1,len(my_list),2):
#     print(my_list[i],end=" ")
# print()


# # 7.2 How many even numbers are there in the above
# countEven=0
# for i in range(1,len(my_list),2):
#     countEven+=1
# print(countEven)


# 7.3 you are given with a space seperated integer list find no. of odd elemnts and no .of even elemnts in a given list
my_list = list(map(int,input().split()))
countEven=0
countOdd=0
for i in my_list:
    if i%2==0:
        countEven+=1

    else :
        countOdd+=1
print(f"No. of odd numbers are:{countOdd}\nNo. of even numbers are:{countEven}")


