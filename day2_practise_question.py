# write a program to find perimeter of a cicle
# write a program to find area of a circle
#  write a program to find area of a triangle
# write a program to find perimeter of a triangle

# # 1.Area of a circle
# radius =int(input())
# print(3.14*(radius**2))

# # 2.perimeter of a circle
# radius =int(input())
# print(2*3.14*radius)

# # 3.area of a triangle
# base =int(input())
# height =int(input())
# print(0.5*base*height)

# 4.perimeter of a triangle

# prime numbers
n=int(input())
flag=True
if n==2 : print("prime")
elif n==1: print("prime")
else :
    for i in range (2,int((n**0.5))+1):
        if(n%i==0):
            flag=False
            break
    if flag==True:print("prime")
    else: print("not prime")