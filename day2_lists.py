# my_list=[1,2,4,3]
# # print(*my_list,end="@")
# # my_list.insert(5,9999)
# # print(*my_list)
# # print(len(my_list))
# # my_list.pop()
# # print(*my_list)
# # new_list = my_list.copy()
# # new_list.pop()
# # print(new_list)
# my_list.sort()
# print(*my_list)

# my_list=list(map(str,input().split(" ")))
# my_list1=list(map(str,input().split(" ")))
# my_list.append("apple")
# lst = my_list+my_list1
# cnt =lst[0].count('o')
# print(*lst)
# print(cnt)

lst = list(map(int,input().split(" ")))
print("if choice =1 -'APPEND'")
print("if choice =2 -'POP'")
print("if choice =3 -'SORT'")
print("if choice =4 -'PRINT LENGTH'")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        lst.append(15)
    elif choice == 2:
        lst.pop()
    elif choice == 3:
        lst.sort()
        print(lst)
    elif choice == 4:
        print(len(lst)) 
    else :break
