a = []
for i in range(6):
    temp=[int(j) for j in input().split()]
    a.append(temp)
res = []
sum = 0
for i in range(4):
    for j in range(4):
        sum += a[i][j]+a[i][j+1]+a[i][j+2]
        sum += a[i+1][j+1]
        sum += a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
        res.append(sum)
        sum = 0
print(max(res))