import random
import time

def spin_row():
    symbols = ['@','$','*']
    return [random.choice(symbols) for _ in range(3)]

   
def print_row(row):
    print(' | '.join(row))

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '@':
            return bet * 10
        elif row[0] == '*':
            return bet * 20
        elif row[0] == '$':
            return bet * 30
    return 0
        


def main():

    count = 0

    balance = 1000


    
    my_time = 3


    print('*************************')
    print('Welcome To Python Slots')
    print('*************************')
    print('Symbols @  $  *')
    print('*************************')
    while balance > 0:
        print(f'Current balance ${balance}')

        bet = input('Place your bet amount: ')
        if not bet.isdigit():
            print('Please Enter a valid number!')
            continue

        bet = int(bet)

        if bet > balance:
            print('Insufficient balance!')
            continue

        if bet <= 0:
            print(f'bet must be greater than {bet}')
            continue


        balance -= bet
        count += 1

        row = spin_row()
        print('Spinning....')
        for x in range(my_time,0,-1):
            time.sleep(1)
            print(x)

        
        print_row(row)

        payout = get_payout(row,bet)
        
        if payout > 0:
            print(f'You Won! : ${payout}')

        else:
            print('You lost the Spin!')
        balance += payout
        
        #if count >= 10:
         #  break

        
        #play_again = input('Dou You want to spin again?(Y/N): ').upper()
        #if play_again != 'Y':
         #   break
    print(f'Your total balance is : ${balance} ')
main()