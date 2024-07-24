# sum of even digits in a given number
n=int(input())
sum=0
while n>0:
    rem=n%10
    if(rem%2 ==0):
        sum+=rem
    n=n//10
print(sum)