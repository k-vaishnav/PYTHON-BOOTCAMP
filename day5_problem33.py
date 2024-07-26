# hello-------world
# op:--------hello world
s=input()
cnt=0
str=""
for i in s:
    if i =="-":
        cnt+=1
    else :str+=i
print("-"*cnt+str)
