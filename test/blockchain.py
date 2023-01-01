blockchain = []

print(blockchain)

# blockchain.append(blockchain[-1])

# print(blockchain)


def get_last_blockchain_value():
    if blockchain != []:
        return blockchain[-1]
    return [0] #incase this is the first block


def add_value(transaction_amount):
    blockchain.append([get_last_blockchain_value(), transaction_amount])
    # print("blockchain contents:",blockchain)


# add_value(3)
# add_value(5.2)
# add_value(1.4)

def get_user_input():
    transaction_amount = input('what about do you wish to add to the blockchain?')
    try:
        return float(transaction_amount)
    except:
        get_user_input()
        # print('your blockchain was corrupted with an unusable value')
        # return None 
        

add_value(get_user_input())
add_value(get_user_input())
add_value(get_user_input())

# tx_amount = float(input('what about do you wish to add to the blockchain?'))
# add_value(tx_amount)

# tx_amount = float(input('what about do you wish to add to the blockchain?'))
# add_value(tx_amount)

print(blockchain)
