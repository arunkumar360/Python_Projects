foods = {'pizza':3,
         'nachos':4.5,
         'popcorn':6,
         'fries':2.5,
         'chips':1,
         'pretzel':3.5,
         'soda':3.5,
         'lemonade':3.5}

cart = []
total = 0

print("---------MENU--------------")

for key,value in foods.items():
    print(f'{key:10}: ${value:.2f}')

print("-----------------------------")
while True:
    food = input("Enter food to buy (Press q to quit):").lower()
    if food == 'q':
        break
    elif foods.get(food) is not None:
        cart.append(food)
print("---------Your Order--------------")
for food in cart:
    total += foods.get(food)
    print(food,end=" ")
print()

print(f'Total price is ${total}')
print("------------------------------")