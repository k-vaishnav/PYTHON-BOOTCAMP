# remove all the brackets from the given algebric expression
check="(){}[]"
s=input()
for i in s:
    if i not in check:
       print(i,end="")

inp=input()
for i in inp:
    if(ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125 or ord(i)==41 or ord(i)==40):
        pass
    else:
        print(i,end="")
