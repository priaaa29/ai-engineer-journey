Emenu = {"pizza": 3.00,
"nachos": 4.50,
"popcorn": 6.00,
"fries": 2.50,
"chips": 1.00,
"pretzel": 3.50,
"soda": 3.00,
"lemonade": 4.25}

cart = []
total = 0

print('----------------------------')
for key, value in Emenu.items():
    print(f'{key:10}: ${value:.2f}')
print('----------------------------')

while True:
    item = input('Enter the item you want to order (q to quit): ')
    if item.lower() == 'q':
        break
    elif item.lower() in Emenu:
        cart.append(item.lower())
    else :
        print('choose from the menu')
for item in cart :
    total += Emenu.get(item)
print('----------------------------')
print ('      your order is:       ')
print('----------------------------')
for item in cart:
    print(item)
print(f'your total is ${total:.2f}')
