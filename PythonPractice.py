import getpass
import msvcrt

# GLOBALS AND CONSTANTS
ATM_CODE = '7624'  # Secret access code to the ATM exercise
INITIAL_SUM = 1000  # Initial amount of money in the bank account

# Exercise No. 1- ATM emulation
def atm():
    atm_code = ATM_CODE  # Takes ATM code
    balance = INITIAL_SUM  # Takes inital sum
    while True:
        print('\nPlease enter the secret code')
        code = getpass.getpass('CODE: ')

        # Checks secret code
        if code != atm_code:  # If entered code is wrong
            print('WRONG CODE\nPlease try again')
            continue  # Quits loop

        # Displays menu
        print('Please select one of the following options:\n1) Display balance' +
              '\n2) Withdraw cash\n3) Change secret code\n4) Exit')

        choice = msvcrt.getch()  # Gets user's choice
        # OPTION 1
        if choice == '1': # User chose to see balance
            print('Your current balance is:\n ' + str(balance) + 'NIS')

        # OPTION 2
        elif choice == '2':  # User chose to withdraw money
            amount = int(input('What is the amount you would like to withdraw?\n'))
            if amount < balance:
                balance -= amount  # Updates balance
                print('Succeeded. Your new balance is ' + str(balance) + ' NIS')
            else:  # User does not have enough money
                print('You do not have enough money in your account to do this\n'
                      'action.')

        # OPTION 3
        elif choice == '3':  # User chose to change secret code
            code = getpass.getpass('Please re-enter your secret code')
            if code == atm_code:  # If user entered the right code
                atm_code = getpass.getpass('Enter new secret code\n')  # Updates code
                print('Code updates successfully')

        # OPTION 4
        elif choice == '4':
            print('Good bye')
            break

        # WRONG CHARACTER
        else:
            print('Wrong command, you will need to re-enter your secret code')


# Exercise No. 2- Calculates sums of numbers received from user
def list_sum():
    sum = 0  # Initializes sum
    print('Please enter a series of numbers, or "stop" to end input')
    num = input()
    while num.isdigit():  # As long as num is a number
        sum += int(num)
        num = input()
    print('The total sum of the numbers you entered is ' + str(sum))

    sum = 0
    print('\n\nNow please enter a series of numbers in this format: NUM,NUM,...')
    series = input()  # Gets series
    numbers = series.split(',')  # Splits string to numbers
    for n in numbers:
        sum += int(n)
    print('The total sum of the numbers in the serie you entered is ' + str(sum))