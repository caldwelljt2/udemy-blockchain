import json

# instalize blockchain
blockchain = []

print(blockchain)
# def read_blockchain():
#     global blockchain
#     blockchain_file = open('save_blockchain.txt', 'r')
#     blockchain = blockchain_file.read()
#     blockchain_file.close()

# Open the file for reading
def read_blockchain():
    global blockchain
    data = open('save_blockchain.txt', 'r').read()

    # Deserialize the JSON string and restore the list
    blockchain = json.loads(data)
    # data.close()

def write_blockchain():
    # Serialize the blockchain list as a JSON string
    data = json.dumps(blockchain)
    # Open the file for writing
    with open('save_blockchain.txt', 'w') as blockchain_file:
        # Write the serialized list to the file
        blockchain_file.write(data)

# def write_blockchain():
#     # print(blockchain)
#     global blockchain
#     print(blockchain)
#     blockchain_file = open('save_blockchain.txt', 'w')
#     blockchain_file.write(blockchain)
#     blockchain_file.close()

# blockchain.append(blockchain[-1])

# print(blockchain)


def get_last_blockchain_value():
    """ returns the last blockchain value or [0] if none exists"""
    # global blockchain
    try:
        return blockchain[-1]
    except:
        # blockchain = [[None]]
        return [None]


def add_value(transaction_amount):
    """ add a transaction to the blockchain"""
    blockchain.append([get_last_blockchain_value(), transaction_amount])


def get_user_input():
    ''' returns the user input'''
    return input('Please choose: ')

def get_user_amount_input():
    """ gets user input recursivly until input is valid for return"""
    while True:
        transaction_amount = input('what about do you wish to add to the blockchain? (q to cancel): ')
        if transaction_amount == 'q' or transaction_amount.casefold() in ['q','done','quit','cancel']:
            return 'done'
        else:
            try:
                return float(transaction_amount)
            except:
                print("Invalid input, try again (must be a usable number.... )")
                # get_user_amount_input()
                # return 'done'
                continue
            # break

    

while True:
    print("""Please choose one:
    1. Add transaction amount to the blockchain
    2. Print transaction amount          
    3. Load/Save the blockchain
    4. End session"""    )
    answer = get_user_input()
    if answer == '1':
        tx_amount = get_user_amount_input()
        if tx_amount != 'done':
            # break
            add_value(tx_amount)
    elif answer == '2':
        print('this is the entire blockchain:')
        print(blockchain)

        print('-' * 23)
        print('this is each block using for loop with method 1:')
        for block in blockchain:
            x = locals().get('x', 0) # I have no idea what this is doing...
            print(f'Block {x}: ',block)
            x += 1
        x = 0

        print('-' * 23)
        
        print('this is each block using for loop with method 2:')
        for i, block in enumerate(blockchain):
           print(f'Block {i}: {block}')

        if blockchain != []:
            print("Final input ",blockchain[-1][-1])
        else:
            print('Warning: NO INPUT ADDED (yet)!')

    elif answer == '3':
        load_save_answer = input('Load/Save/Exit: ')
        if load_save_answer.casefold() in ['l','load']:
            read_blockchain()
        elif load_save_answer.casefold() in ['s','save']:
            print('in')
            write_blockchain()
        else:
            continue
    else:
        is_sure = input('Are you sure - UNSAVED changes will be LOST (y/n): ')
        if is_sure.casefold() in ['y','yes']:
            break
        # else:
            
            # restart question


# add_value(get_user_input())
# add_value(get_user_input())

# tx_amount = float(input('what about do you wish to add to the blockchain?'))
# add_value(tx_amount)

# tx_amount = float(input('what about do you wish to add to the blockchain?'))
# add_value(tx_amount)

# write_blockchain()

print('Thank you for your visit to my blockchain, have a nice day')