# Initializing our (empty) blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if blockchain.__len__() < 1:
        return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        blockchain.append([transaction_amount])
    else:
        blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    while True:
        user_input = input('Your transaction amount please: ')
        try:
            user_input = float(user_input)
            break
            # return user_input (moved to parent loop)
        except: 
            print('Sorry, Invalid Entry. Please enter a VALID number.')
            continue
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_all_blockchain_elements():
    print(blockchain)

def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

# Get the first transaction input and add the value to the blockchain
# tx_amount = get_transaction_value()
# add_transaction(tx_amount)

# Main Loop
while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('3: Output ALL blockchain blocks')
    print('Q: Quit')
    user_choice = get_user_choice().strip()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == '3':
        print_all_blockchain_elements()
    elif user_choice.lower() == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')
    print('Choice registered!')


print('Done!')
print('your final ledger was:')
print(blockchain)
print('your itemized blockchain was:')
for block in blockchain:
    print(block)