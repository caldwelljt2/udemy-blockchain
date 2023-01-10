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
participants = set()
reward = 50.0

def read_blockchain():
    """Read's blockchain from save_blockchain.txt

    Returns:
        list: The blockchain
    """
    data = open('save_blockchain.txt', 'r').read()

    # Deserialize the JSON string and return as list
    return json.loads(data)


def write_blockchain(blockchain):
    """ Writes blockchain to disk

    Arguments:
        :blockchain (list): The blockchain as list
    """
        
    # Serialize the blockchain list as a JSON string
    data = json.dumps(blockchain)
    # Open the file for writing
    with open('save_blockchain.txt', 'w') as blockchain_file:
        # Write the serialized list to the file
        blockchain_file.write(data)


def get_last_blockchain_value():
    """ returns the last blockchain value or [0] if none exists"""
    try:
        return blockchain[-1]
    except:
        return [0]


def add_transaction(open_transactions, sender, recipient, amount=0.0):
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

    open_transactions.append(transaction)
    print(open_transactions)
    return open_transactions


def mine_block(transactions, blockchain, miner = 'Jon', reward = 50.0):
    """Mines the block in transactions on to the blockchain and returns it,
    paying the miner in the next future block.

    Args:
        transactions (list): the mempool of open transactions to mine
        blockchain (list)): The blockchain
        miner (str, optional): The miner attempting to mine this block. Defaults to 'Jon'.

    Returns:
        (tuple): A tuple containing the updated blockchain and a fresh open_transaction list with a transaction for the miner being paid for his work.
    """
    
    leading_zeros = difficulty * "0"

    if transactions == []:
        print("please submit a transaction first!!!")
        return blockchain

    previous_block = blockchain[-1]
    previous_block_as_hash = hash_block(previous_block)
    index_of_this_Block = len(blockchain)
    nonce = 0
    passes_check = False

    block = {
        'previous_hash': previous_block_as_hash,
        'index': index_of_this_Block,
        'transactions': transactions,
        'nonce': nonce
    }

    while passes_check == False:
        this_block_as_hash = hash_block(block)
        if this_block_as_hash.startswith(leading_zeros):
            passes_check = True
        else:
            block['nonce'] += 1
            
    print(f"it took {block['nonce']} tries to complete")
    print(f"Hash: {this_block_as_hash}")
        
    # add block to end of chain
    blockchain.append(block)
    
    # clear transactions
    transactions = []

    # Pay the miner by adding new transaction to be mined
    print(f"paying the miner, {miner} the mining fee of {reward}")
    transactions = add_transaction(transactions, 'Mining_Rewards', miner, reward)
    
    return transactions, blockchain


def get_user_input():
    ''' returns the user input'''
    return input('Please choose: ')


def get_transaction_values():
    """ gets user input for receipient and value and returns them"""
    while True:
        transaction_sender = input('Sender: ')
        transaction_recipient = input('Recipient: ')
        transaction_amount = input('Amount / (C)ancel: ')
        if transaction_amount == 'q' or transaction_amount.casefold() in ['c', 'q', 'done', 'quit', 'cancel']:
            return 'done'
        else:
            try:
                return transaction_sender, transaction_recipient, float(transaction_amount)
            except:
                print("Invalid input, try again (Check the amount is a usable number... )")
                continue

def get_participants(blockchain):
    """Goes through entire blockchain history and returns all participants as a list of participants

    Args:
        blockchain (list): Blockchain to scourge

    Returns:
        set: A set of all participants ever
    """
    global participants
    for i, block in enumerate(blockchain):
        for transaction in block['transactions']:
            participants.add(transaction['sender'])
            participants.add(transaction['recipient'])
    return participants          

def get_balance(participant):
    """Steps through entire blockchain and gives a balance for the named participant

    Args:
        participant (string): Name or Address of participant

    Returns:
        float: A balance of transactions (also prints balance issues to terminal)
    """
    balance = 0.0
    for i, block in enumerate(blockchain):
        for transaction in block['transactions']:
            if transaction['sender'] == participant:
                balance -= transaction['amount']
            if transaction['recipient'] == participant:
                balance += transaction['amount']
                
    if balance < 0 and participant != 'Mining_Rewards':
        print(f'Block {i} shows a balance dropping below 0 for {participant}, this isn\'t possible (allowed for now')
        print(f'Full block (for debugging): {block}')
        
    if participant == 'Mining_Rewards':
        global reward
        number_of_previous_blocks = (len(blockchain) - 1)
        rewards_paid_so_far = number_of_previous_blocks * reward
        print(f'The blockchain has paid recorded {balance * -1} paid as mining rewards')
        print(f'The rules say it should have paid out {rewards_paid_so_far}')
        return 0
    return balance

def display_blockchain(blockchain):
    """Prints blockchain and each block to the terminal

    Args:
        blockchain (list): Blockchain to display
    """
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
        print('Warning: NO BLOCKS MINED (yet)!')


def display_transaction(transaction):
    """Prints a transaction's information to the terminal

    Args:
        transaction (dict): A transaction dictionary
    """
    print('Sender: ', transaction['sender'])
    print('recipient: ', transaction['recipient'])
    print('amount: ', transaction['amount'])

def hash_block(block):
    this_block_as_string = json.dumps(block)
    return hashlib.sha256(this_block_as_string.encode()).hexdigest()


def verify_blockchain(blockchain):
    """Steps through all blocks to verify they are valid (SHA256 Hashes)

    Args:
        blockchain (list): A blockchain to verify

    Returns:
        Bool: Returns True if valid (also prints errors to terminal)
    """
    verified = False
    for i, block in enumerate(blockchain):
        print(blockchain)
        print(f'Block {i}: {block}')
        if i == 0:
            this_block_hashed = hash_block(block)
            if this_block_hashed != genisis_hash:
                print(f'First block\'s hash: "{this_block_hashed}" does not match genisis hash {genisis_hash} and is considered CORRUPTED!')
                verified = False
                break
            else:
                verified = True
                continue
        if i > 0:
            this_block_hashed = hash_block(block)
            
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
    7. Get Participants
    8. Get all Balances (must load all participants first)
    Q. (Q)uit session""")
    answer = get_user_input()
    if answer == '1':
        receipient_and_amount = get_transaction_values()
        sender = receipient_and_amount[0]
        recipient = receipient_and_amount[1]
        amount = receipient_and_amount[2]
        if receipient_and_amount != 'done':
            open_transaction = add_transaction(open_transactions, sender, recipient, amount)

    elif answer == '2':
        print('this is the entire blockchain:')
        display_blockchain(blockchain)

    elif answer == '3':
        print('this is the open transactions (itemized): ')
        for i, transaction in enumerate(open_transactions):
            print(f'transaction {i+1}:')
            display_transaction(transaction)
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
        open_transactions, blockchain = mine_block(open_transactions, blockchain)
        
    elif answer == '7':
        print('was: ', participants)
        participants = get_participants(blockchain)
        print('now: ', participants)
        
    elif answer == '8':
        for participant in participants:
            print(f"{participant} has {get_balance(participant)}")

    elif answer in ['q', 'Q']:
        is_sure = input('Are you sure - UNSAVED changes will be LOST (y/N): ')
        if is_sure.casefold() in ['y', 'yes']:
            waiting_for_input = False

    else:
        print('Selection not recognized')
        # restart question


print('Thank you for your visit to my blockchain, have a nice day')
