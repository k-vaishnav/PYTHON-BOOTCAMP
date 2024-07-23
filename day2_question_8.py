# Given an space seperated integer list find the average of elemnts present at the even index
my_list = list(map(int,input().split()))
sum=0
cnt =0
n=len(my_list)
for i in range(0,len(my_list),2):
    sum+=my_list[i]
    cnt+=1
if(n%2==0): print(sum//i)
else :print(sum/i-1)