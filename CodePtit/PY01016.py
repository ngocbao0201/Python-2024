for t in range(0,int(input())):
    s = input()
    for i in range(1,len(s),2) :
        for j in range(0,int(s[i])) :
            print(s[i-1],end='')
    print()