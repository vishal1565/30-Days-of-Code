#!/bin/python3
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swap1, swap2 = 0, 0
for i in range(n):    
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swap1 += 1
    if swap1-swap2 == 0:
        break
    swap2 = swap1
print("Array is sorted in",swap1,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])