# password verifier
"""Mr. X is trying to create a new password for his instagram account these are the required conditions for creating a new password
1. minimum length is 8 maximum length is 15
2.only @,/ is allowed in a password
3.no spaces are allowed
4.only alphaNumerics are allowed
you are supposed to print 'weak' if length is exact 8 'medium' length is between 8-12 'strong' if length is between 12-15"""

check="1234567890@/abcdefghijklmnopqrstuvwxyz"
pwd =input()
n=len(pwd)
cnt=0
flag=True
str='@/'
if n<8 or n>15:
    print("password must have atleast 8 characters and atmost 15 characters")
else:
    for i in pwd:
        if i in str:
            cnt+=1
        if i not in check :
            flag =False
            break
    if(cnt>0 and flag==True):
        if n==8:print("weak")
        elif n>8 and n<=12:print("medium")
        else:print("strong")
    else :print("follow the condition")


