n = int(input())
a = list(map(int,input().split()))
cnt = int(0)
for i in range(0,n-1):
    if a[i] != a[i+1] :
        cnt += 1
print(cnt)