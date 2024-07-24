# sum of digits
n=123
sum =0
while n>0:
    rem=n%10
    sum+=rem
    n=n//10
print(sum)


# reverse numbers
n=123
num=0
while n>0:
    rem=n%10
    num=num*10+rem
    n=n//10
print(num)

# palindrome number
n=t=1225
num=0
while n>0:
    rem=n%10
    num=num*10+rem
    n=n//10
print(num==t)