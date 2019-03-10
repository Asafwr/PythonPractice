import getpass
import msvcrt
from math import sqrt

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


# Exercise No. 3- Check winner in a Tic Tac Toe game
# Receives matrix as an argument
# NOTE: Function is generic and can handle a board of any size
def tic_tac_toe(mat):
    dimension = len(mat)
    # Used to check diagonals
    main_diagonal_val = mat[0][0]
    main_diagonal_ok = True
    sec_diagonal_val = mat[0][dimension - 1]
    sec_diagonal_ok = True

    # Checks whether all cells in a row, a column or a diagonal are equal
    for i in range(dimension):
        # Checks diagonals
        if mat[i][i] != main_diagonal_val:  # Checks main diagonal
            main_diagonal_ok = False

        if mat[dimension - i][i] != sec_diagonal_val:
            main_diagonal_ok = False

        # Checks rows and columns
        row_val = mat[i][0]  # Used to check row
        row_ok = True
        col_val = mat[0][i]  # Used to check column
        col_ok = True
        # Goes through row / col
        for j in range(dimension):
            if mat[i][j] != row_val:
                row_ok = False
            if mat[j][i] != col_val:
                col_ok = False
        if row_ok:
            return row_val
        if col_ok:
            return col_val

    if main_diagonal_ok:
        return main_diagonal_val
    if sec_diagonal_ok:
        return sec_diagonal_val
    return -1


# Exercise No. 4- String compression
# Receives a string and returns a compressed string, where every character that repeats
# itself more than 3 times is compressed into: @[CHAR][COUNT] (ex: aaaa -> @4a)
# NOTE: Supports compression of string containing both letters and digits
def compress_str(string):
    new_str = ''
    count = 0
    prev = chr(0)  # Always contains previous character
    for ch in string:  # Iterates through all chars in string
        if ch == prev:  # If character is the same as before updates count
            count += 1
        else:
            if count > 3:
                new_str += '@' + prev + count
            else:
                new_str += count * prev
            prev = ch  # Updates prev
    return new_str


# Exercise No. 5- Checking the validation digit of an Israeli ID
# Returns True is check digit is valid or False otherwise
def valid_digit(id_num):
    # If ID number is not 9 chars long or no a number
    if len(id_num) != 9 or not id_num.isdigit() :
        return False

    num = 0
    # First part - sums up all digits as in: d1 * 1 + d2 * 2 + d3 * 1 + d4 * 2 +...
    for i in range(8):
        temp = int(id_num[i]) * (1 + i % 2)
        temp = int(temp / 10) + temp % 10 if temp > 9 else temp
        num += temp

    # Seconds part- finds the difference from the closest product of ten
    return (num + int(id_num[8])) % 10 == 0


# Exercise No. 6- Map function
# Calls a received method for each element in a received list
def map_func(ls, func):
    return [func(element) for element in ls]


# Auxiliary method for Ex. 6
# Used to check the function in exercise 6
def useless_func(x):
    return (x**2 - sqrt(x)) / x


# Exercise No. 7- Decorator Cache
# Receives a function, and returns a memoized decorator which saves results
# in a cache memory to avoid repetition of previous calculations.
def decorator(func):
    cache = dict()

    def memoize(*args):  # Decorator for function
        if args in cache:  # If function was already called with these parameters
            return cache[args]
        result = func(*args)  # Calculating result
        cache[args] = result
        return result

    return memoize