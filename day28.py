n = int(input())
res = []
for _ in range(n):
    temp = input()
    if temp[-10:] == '@gmail.com':
        tmp = temp.split()
        res.append(tmp[0])
res.sort()
print(*res,sep='\n')