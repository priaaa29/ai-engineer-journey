#Banking Program 

def balance():
    pass
def deposit():
    pass
def withdraw():
    pass

balance = 0 
is_running = True

while is_running:
    print('· · ─ ·✶· ─ · ·')
    print('Welcome to the Banking Program')
    print('· · ─ ·✶· ─ · ·')
    print('1. Check Balance')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Exit')
    print('· · ─ ·✶· ─ · ·')
    choice = input('Please select an option (1-4): ')
    print('· · ─ ·✶· ─ · ·')
    if choice == '1':
        print()
        print(f'Your current balance is : ${balance:.2f}')
    elif choice == '2':
        print()
        amount = float(input('Enter the amount to deposit: '))
        if amount > 0:
            balance +=amount
            print(f'${amount:.2f} has been deposited. Your new balance is: ${balance:.2f}')
        else:
            print('Invalid amount. Please enter a positive number.')
    elif choice == '3':
        print()
        amount = float(input('Enter the amount to withdraw: '))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f'${amount:.2f} has been withdrawn. Your new balance is: ${balance:.2f}')
        elif amount > balance:
            print('Insufficient funds. Please enter a smaller amount.')
        else:
            print('Invalid amount. Please enter a positive number.')
    elif choice == '4':
        print('Thank you for using the Banking Program. Goodbye!')
        is_running = False
    else:
        print('Invalid option. Please select a valid option (1-4).')
        

