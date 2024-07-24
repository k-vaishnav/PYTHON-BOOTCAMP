# find the sum of squares of digits in a given number
n=int(input())
sum=0
while n>0:
    rem=n%10
    sum+=rem**2
    n=n//10
print(sum)