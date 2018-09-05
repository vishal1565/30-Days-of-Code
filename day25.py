import math
t = int(input())
for _ in range(t):
    n = int(input())
    root = math.sqrt(n)
    limit = math.floor(root) + 1
    if n == 1:
        print("Not prime")
    elif n == 2:
        print("Prime")
    else:
        if n%2 == 0:
            print("Not prime")
        else:
            flag = True
            for i in range(3, limit, 2):
                if n%i == 0:
                    print("Not prime")
                    flag = False
                    break
            if flag:
                print("Prime")