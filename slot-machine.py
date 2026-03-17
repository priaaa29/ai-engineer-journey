#slot machine 
import random

def spin_row():

    symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '💎']
    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))
    return result
    
def print_row(row):

    print ('∘₊✧───────✧₊∘')
    print(' | '.join(row))
    print ('∘₊✧───────✧₊∘')

def get_payout(row, bet):

    if row[0] == row[1] == row[2]:
        return bet * 10   
    if row[0] == row[1] or row[0] == row[2] or row[1] == row[2]:
        return bet * 2
    return 0
    

def main():

    balance = 100

    print ('────────────────∘₊✧──────────────────────────────✧₊∘────────────────')
    print ('|                 Welcome to the Slot Machine Game!                |')
    print ('|                  symbols: 🍒, 🍋, 🍊, 🍉, ⭐, 💎                 |')
    print ('|                            ∘₊✧───────✧₊∘                         | ')
    print('|        You can bet any amount up to your current balance.        |')
    print('|   If you get three matching symbols, you win 10 times your bet!  |')
    print('|     If you get two matching symbols, you win 2 times your bet!   |')
    print('|        If you get no matching symbols, you lose your bet.        |')
    print('|                       ✧₊∘ Good luck! ✧₊∘                         |')
    print('────────────────∘₊✧──────────────────────────────✧₊∘────────────────')

    while balance > 0:

        print(f'Your current balance is: ${balance}')
        bet = input('Enter your bet amount: ')

        if not bet.isdigit():
            print('You must enter a valid number for your bet.')
            continue

        bet = int(bet)

        if bet > balance:
            print('You cannot bet more than your current balance.')
            continue

        if bet <= 0:
            print('You must bet a positive amount.')
            continue

        balance -= bet

        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f'Congratulations! You won ${payout}!')
            balance += payout

        else:
            print('Sorry, you did not win this time.')

        if balance <= 0:
            print('You have run out of money. Game over!')
            break
        if play_again := input('Do you want to play again? (y/n): ').lower() != 'y':
            print('Thank you for playing! Goodbye!')
            break


if __name__ == "__main__":
    main()