# ABC,4------EFG
# inp =input()
# n=int(input())
# skip=(ord(inp[0])+(n%26))
# if skip>122:
#     skip=skip-26
# print(skip)
# for i in range(skip,skip+len(inp)):
#     print(chr(i),end="")

inp =input()
n=int(input())
for i in inp:
    if ord(i)>=65 and ord(i)<=90:
        skip=ord(i)+(n%26)
        if skip>90:
            skip=skip-26
        print(chr(skip),end="")
    elif ord(i)>=97 and ord(i)<=122:
        skip=ord(i)+(n%26)
        if skip>122:
            skip=skip-26
        print(chr(skip),end="")
print()