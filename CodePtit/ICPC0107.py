for t in range(int(input())) :
    m,n = [i for i in input().split()]
    a = input().strip()
    if a.count(' ') :
        a,b = a.split()
    else :
        b = input()
    p = min(m,n)
    q = max(m,n)
    print(int(a.replace(q,p)) + int(b.replace(q,p)),end=' ')
    print(int(a.replace(p,q)) + int(b.replace(p,q)))
    