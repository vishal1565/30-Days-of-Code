t = int(input())
while t>0 :
    n, k = [int(i) for i in input().split()]
    print(k-1 if ((k-1) | k) <= n else k-2)
    t -= 1