s = "HELLoworld123"
# check ="1234567890"
# sum=0

# for i in s:
#     if i in check:
#         sum+=ord(i)-ord("0")
# print(sum)

# inp=input()
# sum=0
# for i in inp:
#     if(ord(i)>=48 and ord(i)<=57):
#         sum+=int(i)
inp=input()
print(inp.isalpha())
print(inp.isnumeric())
cnt=0
for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
        cnt+=1
print(cnt)
       