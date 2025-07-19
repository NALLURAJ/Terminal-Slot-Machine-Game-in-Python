import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    'A' : 2, 'B': 4, 'C':6, 'D':8 
}
symbol_values = {
    'A' : 5, 'B': 4, 'C':3, 'D':2 
}
def check_winnings(columns,lines,bet,values):
    winnings =0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_ckeck = column[line]
            if symbol != symbol_ckeck:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings,winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols =[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Enter the deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Not Enough Amount to deposit!!")
        else:
            print("Enter the numeric value")
    return amount

def getting_the_bet_lines():
    while True:
        lines = input("Enter the number of lines you wanna bet(1-" + str(MAX_LINES) + ") : ")
        if lines.isdigit():
            lines =int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Not Valid Lines")
        else:
            print("Enter numeric values")
    return lines

def get_bet():
    while True:
        bet = input("Enter the bet amount that you would like to bet on each line: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} AND ${ MAX_BET}')
        else:
            print("Enter numeric value")
    return bet
def spin(balance):
    lines = getting_the_bet_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You are not having enough amount to bet !')
        else:
            break
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_values)
    print(f'You won ${winnings} !!')
    print(f'You won on line:', *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Your current balance : ${balance}')
        x = input("Press enter to play ( q to quit )")
        if x == 'q':
            break
        else:
            balance += spin(balance)
    print(f"You left with ${balance}")

    
main()
