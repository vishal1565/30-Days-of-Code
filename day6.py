for _ in range(int(input())):
    a = input()
    even, odd =[], []
    for i in range(len(a)):
        if i%2 == 0:even.append(a[i])
        else:odd.append(a[i])
    print(*even," ",*odd,sep="")