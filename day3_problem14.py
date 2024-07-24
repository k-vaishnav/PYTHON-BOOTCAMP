my_list = list(map(int,input().split()))
fmax=my_list[0]
smax=my_list[1]
for i in range(1,len(my_list)):
    if fmax<my_list[i]:
        smax=fmax
        fmax =my_list[i]
print(smax)