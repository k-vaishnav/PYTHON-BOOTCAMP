# # peak element --------most imp
# lst=list(map(int,input().split()))
# n=len(lst)
# peak=0
# for i in range(n):
#     if i==0 and lst[i]>lst[i+1]:
#         print(lst[i],end=" ")
#     elif i== n-1 and lst[i]>lst[i-1]:
#         print(lst[i],end=" ")
#     elif lst[i]>lst[i+1] and lst[i]>lst[i-1]:
#         print(lst[i],end=" ")

lst=list(map(int,input().split()))
n=len(lst)
count=0 
for i in range(1,len(lst)-1):
    if lst[i]>lst[i+1] and lst[i]>lst[i-1]:
        count=i
if(lst[-1]>lst[-2]) and lst[-1]>count :
    count=len(lst)-1
print(lst[count])