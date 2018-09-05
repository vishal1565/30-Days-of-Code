def binConverter(num):
    bin=[]
    while num>0:
        bin.append(num%2)
        num=num//2
    bin.reverse()
    return bin

n = int(input())
temp = binConverter(n)
count = 1
rec = [1]
for i in range(1,len(temp)):
    if temp[i-1] == temp[i]:
        count += 1
    else:
        rec.append(count)
        count = 1
rec.append(count)
print(max(rec))