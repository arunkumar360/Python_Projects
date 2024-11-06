foods = []
prices = []
total = 0


while True: 
    food = input("Enter food to buy (Press q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price for {food}: $"))
        prices.append(price)
        foods.append(food)

print("-----Your Cart-----")

for i in foods:
    print(i,end = " ")

for price in prices:
    total += price
print()
print(f"Your total is ${total}")