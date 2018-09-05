n = int(input())
if n%2 == 1:
    print("Weird")
else:
    if n<6 and n>1:
        print("Not Weird")
    elif n>5 and n<21:
        print("Weird")
    elif n>20:
        print("Not Weird")