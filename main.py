import random

#global constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value ={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def checkWins(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def getSlotmachineSpin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # the colon inside the bracket will copy the list inside it
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slotMachine(columns):
   for row in range(len(columns[0])):
       for i, column in enumerate(columns):
           if i != len(columns) - 1:
              print(column[row], end=" | ")
           else:
               print(column[row], end="")

       print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)  #converting it into 'int' bcz by default it was string {3}
            if amount>0:
                break
            else:
                print("Amount must be greater than zero (0)!")
        else:
            print("Please enter a number.")

    return amount


def getNumofLines():
    while True:
        lines= input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? " )
        if lines.isdigit():
            lines = int(lines)  # converting it into 'int' bcz by default it was string {3}
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Please enter a number.")

    return lines

def getBet():
    while True:
     amount = input("What would you like to bet on each line? $")
     if amount.isdigit():
            amount = int(amount)  # converting it into 'int' bcz by default it was string {3}
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
     else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = getNumofLines()
    while True:
        bet = getBet()
        totalBet = bet * lines

        if totalBet > balance:
            print(f"You don't have enough to bet that amount, your current account balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines}. Total bet is equal to: ${totalBet}")

    slots = getSlotmachineSpin(ROWS, COLS, symbol_count)
    print_slotMachine(slots)
    winnigs, winning_lines = checkWins(slots, lines, bet, symbol_value)
    print(f"You won ${winnigs}.")
    print(f"You won on lines:",
          *winning_lines)  # here '*' is splat or unpack operator and its going to pass every single ine from winning_lines list to print function

    return winnigs - totalBet


def main():
    balance = deposit()
    while True:
       print(f"Current balance is ${balance}")
       ans = input("Press enter to spin (q to quit).")
       if ans == "q":
           break
       balance += spin(balance)
    print(f" You left with ${balance}")
main()
