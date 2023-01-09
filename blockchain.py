import json
import hashlib


# instalize blockchain, open transactions, and temporary owner
genisis_block = {
                'previous_hash': 'None',
                'index': 0, 
                'transactions': [],
                'nonce': 190395
            }
genisis_hash = "00000868219e3eeffeb4d11f153d106980878ed4d0815b21e59cec73bbf377a7" # must be changed with difficulty change

blockchain = [genisis_block]
open_transactions = []
owner = 'Jonathan'
difficulty = 5 # must manually rehash genisis block if changed

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


def get_last_blockchain_value():
    """ returns the last blockchain value or [0] if none exists"""
    # global blockchain
    try:
        return blockchain[-1]
    except:
        # blockchain = [[None]]
        return [0]


def add_transaction(sender, recipient, amount=1.0):
    """ add a transaction to the blockchain

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }
    print(transaction)
    open_transactions.append(transaction)
    # blockchain.append([get_last_blockchain_value(), transaction_amount])


def mine_block(open_transactions, blockchain):
    leading_zeros = difficulty * "0"
    # for transaction in open_transactions:
    # insert various checks for validity of amounts
    #     pass
    if open_transactions == []:
        print("please submit a transaction first!!!")
        return blockchain
    previous_block = blockchain[-1]
    previous_block_as_hash = hash_block(previous_block)
    # previous_block_as_string = json.dumps(blockchain[-1])
    # previous_block_as_hash = hashlib.sha256(previous_block_as_string.encode()).hexdigest()
    # previous_block_as_hash = hash_block(block)
    index_of_this_Block = len(blockchain)
    nonce = 0
    passes_check = False
    block = {
        'previous_hash': previous_block_as_hash,
        'index': index_of_this_Block,
        'transactions': open_transactions,
        'nonce': nonce
    }

    while passes_check == False:
        # this_block_as_string = json.dumps(block)
        # this_block_as_hash = hashlib.sha256(this_block_as_string.encode()).hexdigest()
        this_block_as_hash = hash_block(block)
        if this_block_as_hash.startswith(leading_zeros):
            passes_check = True
        else:
            block['nonce'] += 1
            
    print(f"it took {block['nonce']} tries to complete")
    print(f"Hash: {this_block_as_hash}")
        
    # we could also hash the contents of the block now and add or increment a nonce till we get leading 0s

    blockchain.append(block)
    return blockchain
    pass


def get_user_input():
    ''' returns the user input'''
    return input('Please choose: ')


def get_recipient_and_value():
    """ gets user input recursivly until input is valid for return"""
    while True:
        transaction_recipient = input('Who are you sending to? ')
        transaction_amount = input('How much are you sending? (q to cancel): ')
        if transaction_amount == 'q' or transaction_amount.casefold() in ['q', 'done', 'quit', 'cancel']:
            return 'done'
        else:
            try:
                return transaction_recipient, float(transaction_amount)
            except:
                print(
                    "Invalid input, try again (Check the amount is a usable number... )")
                continue
            # break


def display_blockchain(blockchain):
    print(blockchain)

    print('-' * 23)
    print('this is each block using for loop with method 1:')
    for block in blockchain:
        x = locals().get('x', 0)  # I have no idea what this is doing...
        print(f'Block {x}: ', block)
        x += 1
    x = 0

    print('-' * 23)

    print('this is each block using for loop with method 2:')
    for i, block in enumerate(blockchain):
        print(f'Block {i}: {block}')

    if blockchain != [genisis_block]:
        print("Final block ", blockchain[-1])
    else:
        print('Warning: NO INPUT ADDED (yet)!')


def display_transactions(transaction):
    print('Sender: ', transaction['sender'])
    print('recipient: ', transaction['recipient'])
    print('amount: ', transaction['amount'])

def hash_block(block):
    this_block_as_string = json.dumps(block)
    return hashlib.sha256(this_block_as_string.encode()).hexdigest()


def verify_blockchain(blockchain):
    verified = False
    for i, block in enumerate(blockchain):
        print(blockchain)
        print(f'Block {i}: {block}')
        if i == 0:
            # this_block_as_string = json.dumps(block)
            # this_block_hashed = hashlib.sha256(this_block_as_string.encode()).hexdigest()
            this_block_hashed = hash_block(block)
            if this_block_hashed != genisis_hash:
                print(f'First block\'s hash: "{this_block_hashed}" does not match genisis hash {genisis_hash} and is considered CORRUPTED!')
                verified = False
                break
            else:
                verified = True
                continue
        if i > 0:
            # print(i,'/', block[0],'/',blockchain[i-1])
            
            
            previous_block_as_string = json.dumps(blockchain[i-1])
            previous_block_hashed = hashlib.sha256(previous_block_as_string.encode()).hexdigest()
            
            
            if block['previous_hash'] == previous_block_hashed:
                print(f'Block {i} = VERFIED (to contain a valid hash of Block {i-1}')
                verified = True
                continue
            else:
                print(f"Block {i}'s content's {block[0]}")
                print(f"Does NOT MATCH block {i-1}'s contents of {blockchain[i-1]} - {previous_block_hashed})")
                print(f'BLOCK {i} CORRUPTED! {previous_block_hashed} / {block["previous_hash"]}')
                verified = False
                continue

    if verified == True:
        print('ALL BLOCKS MATCH')

    print('Verification process complete')
    return (verified)


waiting_for_input = True

while waiting_for_input:
    print('\n')
    print("""Please choose one:
    1. Add transaction amount to the blockchain
    2. Print entire blockchain
    3. Print open transactions
    4. Load/Save the blockchain
    5. Verify Blockchain
    6. Mine Transaction to blockchain
    Q. (Q)uit session""")
    answer = get_user_input()
    if answer == '1':
        receipient_and_amount = get_recipient_and_value()
        recipient = receipient_and_amount[0]
        amount = receipient_and_amount[1]
        if receipient_and_amount != 'done':
            # break
            add_transaction(owner, recipient, amount)

    elif answer == '2':
        print('this is the entire blockchain:')
        display_blockchain(blockchain)

    elif answer == '3':
        print('this is the open transactions (itemized): ')
        for i, transaction in enumerate(open_transactions):
            print(f'transaction {i+1}:')
            display_transactions(transaction)
            print('\n')

        print('open transactions in raw format:')
        print(open_transactions)

    elif answer == '4':
        load_save_answer = input('Load/Save/Exit: ')
        if load_save_answer.casefold() in ['l', 'load']:
            blockchain = read_blockchain()
            print('\nVerify blockchain before continuing (Option 4)')
        elif load_save_answer.casefold() in ['s', 'save']:
            print('\nASSUMING you verified FIRST')
            write_blockchain(blockchain)
        else:
            continue

    elif answer == '5':
        verify_blockchain(blockchain)

    elif answer == '6':
        blockchain = mine_block(open_transactions, blockchain)
        open_transactions = []

    elif answer in ['q', 'Q']:
        is_sure = input('Are you sure - UNSAVED changes will be LOST (y/N): ')
        if is_sure.casefold() in ['y', 'yes']:
            waiting_for_input = False

    else:
        print('Selection not recognized')
        # restart question


print('Thank you for your visit to my blockchain, have a nice day')
