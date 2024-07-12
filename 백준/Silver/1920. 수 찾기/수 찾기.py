n= int(input())
a= sorted(list(map(int,input().split())))
m= int(input())
num= list(map(int, input().split()))

def func(i, start_idx, last_idx):
    mid_idx= (start_idx+last_idx)//2
    if last_idx < start_idx:
        return 0
    elif a[mid_idx] == i:
        return 1
    elif a[mid_idx]< i:
        start_idx= mid_idx + 1
    else:
        last_idx= mid_idx - 1
    return func(i, start_idx, last_idx)

for i in num:
    if a[0] <= i <= a[n-1]:
        print(func(i, 0, n-1))
    else:
        print(0)