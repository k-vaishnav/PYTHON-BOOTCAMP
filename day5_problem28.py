# write a program to print all capital letters in a given SyntaxWarning
inp=input()
for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
        print(i,end=" ")
