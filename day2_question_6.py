# take space seperated input from a user and print alternate elemnts
li = list(map(int,input().split()))
for i in range(0,len(li),2):
    print(li[i],end=" ")
print()

