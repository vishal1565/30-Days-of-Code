n = int(input())
d = {}
for _ in range(n):
    temp = input().split()
    d.update({temp[0]:temp[1]})
while True:
    tmp = input()
    if tmp in d:
        print(tmp+"="+d[tmp])
    else:
        print("Not found")