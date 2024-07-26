# patterns
# solid square
row =5
col=5
for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()
# lower triangle
row =5
col=5
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
row =5
col=5
for i in range(5,0,-1):
    for j in range(1,6):
        if j>i:
            print(" ",end="")
        else:
            print("*",end="")
    print()

row =5
col=5
for i in range(5,0,-1):
    for j in range(1,6):
        if j>=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
 
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

k=0
for i in range(1,5):
    for j in range(1,i+1):
        k+=1
        print(k,end=" ")
    print()

k=7
for i in range(1,5):
    k=(2*i)+5
    for j in range(5,i,-1):
        print(k,end=" ")
        k+=1
    
    print()

row =5
col=5
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print(" ",end="")
        else:
            print("*",end="")
    print()
# upper triangular,lower triangular,rhombus,parallelogram,number pyramid

row=3
col=3
for i in range(1,4):
    for j in range(1,i+3):
        if j>=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

n=3
for i in range(n):
    spaces=n-i-1
    for j in range(0,spaces):
        print(" ",end="")
    stars = (2*i)+1
    for k in range(0,stars):
        print("*",end="")
    for j in range(0,spaces+1):
        print(" ",end="")
    print()
n=3
for i in range(n):
    spaces=i
    for j in range(0,spaces):
        print(" ",end="")
    stars = 2*(n-i)-1
    for k in range(0,stars):
        print("*",end="")
    for j in range(0,spaces):
        print(" ",end="")
    print()
n=3

for i in range(n):
    spaces=n-i-1
    for j in range(0,spaces):
        print(" ",end="")
    
    k=1
    for j in range(0,(2*i)+1):
        if(j>i):
            print(k,end="")
            k-=1
        elif (i==j):
            print(k,end="")
            k-=1
        else:
            print(k,end="")
            k+=1
    print()  
