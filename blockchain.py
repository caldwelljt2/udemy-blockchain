import json

# instalize blockchain
blockchain = [[0]]

# print(blockchain)
# def read_blockchain():
#     global blockchain
#     blockchain_file = open('save_blockchain.txt', 'r')
#     blockchain = blockchain_file.read()
#     blockchain_file.close()

# Open the file for reading
def read_blockchain():
    # global blockchain
    data = open('save_blockchain.txt', 'r').read()

    # Deserialize the JSON string and restore the list
    return json.loads(data)
    # data.close()

def write_blockchain(blockchain):
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
        return [0]


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

def display_blockchain(blockchain):
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

    if blockchain != [0]:
        print("Final input ",blockchain[-1][-1])
    else:
        print('Warning: NO INPUT ADDED (yet)!')
        
def verify_blockchain(blockchain):
    verified = False
    for i, block in enumerate(blockchain):
        # print(f'Block {i}: {block}')
        if i == 0:
            if block != [0]:
                print(f'First block\'s contents: "{block}" is NOT-Standard and considered CORRUPTED!')
                verified = False
                break
            else:
                verified = True
                continue
        if i > 0:
            # print(i,'/', block[0],'/',blockchain[i-1])
            if block[0] == blockchain[i-1]:
                # print(f'Block {i} = VERFIED')
                verified = True
                continue
            else:
                print(f"Block {i}'s content's {block[0]}")
                print(f"Does NOT MATCH block {i-1}'s contents of {blockchain[i-1]}")
                print(f'BLOCK {i} CORRUPTED!')
                verified = False
                continue

        # if i == 0 and block == 0:
        #     print(f'Block {i}: {block}')
        #     break
        # else:
        #     print('Not verified')
    if verified == True:
        print('ALL BLOCKS MATCH')
    
    print('Verification process complete')
    return(verified)
            
waiting_for_input = True            
            
while waiting_for_input:
    print('\n')
    print("""Please choose one:
    1. Add transaction amount to the blockchain
    2. Print entire blockchain
    3. Load/Save the blockchain
    4. Verify Blockchain
    5. End session"""    )
    answer = get_user_input()
    if answer == '1':
        tx_amount = get_user_amount_input()
        if tx_amount != 'done':
            # break
            add_value(tx_amount)

    elif answer == '2':
        print('this is the entire blockchain:')
        display_blockchain(blockchain)

    elif answer == '3':
        load_save_answer = input('Load/Save/Exit: ')
        if load_save_answer.casefold() in ['l','load']:
            blockchain = read_blockchain()
            print('\nVerify blockchain before continuing (Option 4)')
        elif load_save_answer.casefold() in ['s','save']:
            print('\nASSUMING you verified FIRST')
            write_blockchain(blockchain)
        else:
            continue
        
    elif answer == '4':
        verify_blockchain(blockchain)
        
    elif answer in ['5','q','Q']:
        is_sure = input('Are you sure - UNSAVED changes will be LOST (y/N): ')
        if is_sure.casefold() in ['y','yes']:
            waiting_for_input = False
    
    else:
        print('Selection not recognized')
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