meal_cost = float(input())
tip = int(input())
tax = int(input())
total = (meal_cost+meal_cost*(tip+tax)/100)
if total - int(total) >=0.5:
    total = int(total)+1
else:
    total = int(total)
print("The total meal cost is",total,"dollars.")