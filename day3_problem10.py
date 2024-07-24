""" find the kth position element from the list  
 i/p:k=38                      k=38 n=5 
 70 54 36 72 566                idx = 3 after 7 cycles remaining only 3 indexes 38/5 remainder -3
 o/p: 72 """
k=int(input())
arr = list(map(int,input().split()))
print(arr[k%len(arr)])