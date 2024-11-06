def view_balance(balance):

    print(f'Your balance is: ${balance:.2f}')
    print('#############################')

def deposit():

    amount = float(input('Enter amount to deposit: '))
    print('#############################')
    if amount <= 0:
       
        print(f'You cannot deposit {amount}')
        print('#############################')
        return 0
    else:
        return amount
    

def withdraw(balance):

    amount = float(input('Enter amount to withdraw: '))
    print('#############################')

    if amount > balance:
   
        print('Insufficient balance!')
        print('#############################')
        return 0
    if amount <=0 :
      
        print(f'You cannot withdraw {amount}')
        print('#############################')
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print('###################')
        print('     My Bank      ')
        print('###################')
        print('1.Show Balance')
        print('2.Deposit')
        print('3.Withdraw')
        print('4.Exit')
        print('###################')
       
        choice = input('Enter your choice: ')
        print('#############################')

        if choice == '1':
            view_balance(balance)

        elif choice == '2':
            balance += deposit() 

        elif choice == '3':
            balance -= withdraw(balance)

        elif choice == '4':
            is_running = False

        else:
            
            print(f'{choice} is not a valid choice!')
            print('#############################')

    print('Thank You For Visiting ):')
    print('#############################')

main()
