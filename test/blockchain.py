# instalize blockchain
blockchain = []

print(blockchain)

# blockchain.append(blockchain[-1])

# print(blockchain)


def get_last_blockchain_value():
    """ returns the last blockchain value or [0] if none exists"""
    if blockchain != []:
        return blockchain[-1]
    return [0] #incase this is the first block


def add_value(transaction_amount):
    """ add a transaction to the blockchain"""
    blockchain.append([get_last_blockchain_value(), transaction_amount])
    # print("blockchain contents:",blockchain)


# add_value(3)
# add_value(5.2)
# add_value(1.4)

def get_user_input():
    ''' returns the user input'''
    return input('Please choose: ')


def get_user_amount_input():
    """ gets user input recursivly until input is valid for return"""
    transaction_amount = input('what about do you wish to add to the blockchain? (q to cancel) ')
    if transaction_amount == 'q' or transaction_amount.casefold() in ['q','done','quit','cancel']:
        return 'done'
    else:
        try:
            return float(transaction_amount)
        except:
            print("Invalid input, try again (must be a usable number.... )")
            get_user_amount_input()
            # print('your blockchain was corrupted with an unusable value')
            # return None 
            
while True:
    print(""" Choose one:
    1. Add transaction amount to the blockchain
    2. Print transaction amount          
    3. End session"""    )
    answer = get_user_input()
    if answer == '1':
        tx_amount = get_user_amount_input()
        if tx_amount != 'done':
            # break
            add_value(tx_amount)
    elif answer == '2':
        print(blockchain)
        print("Final input ",blockchain[-1][-1])
    else:
        break


# add_value(get_user_input())
# add_value(get_user_input())

# tx_amount = float(input('what about do you wish to add to the blockchain?'))
# add_value(tx_amount)

# tx_amount = float(input('what about do you wish to add to the blockchain?'))
# add_value(tx_amount)

