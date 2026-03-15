foods = []
prices = []
total = 0

while True:
    food = input("Enter the name of the food item (or type 'done' to finish): ")
    if food.lower() == 'done':
        break
    price = float(input(f"Enter the price of {food}: "))
    
    foods.append(food)
    prices.append(price)

for food, price in zip(foods, prices) :
    print(f"{food}: ${price:.2f}")    
for price in prices:
    total += price

print()
print(f"Total: ${total}")