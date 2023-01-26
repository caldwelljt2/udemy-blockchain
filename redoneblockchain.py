import os
import json
import hashlib

class Blockchain:
    def __init__(self):
        self.genisis_block = {
            'previous_hash': 'None',
            'index': 0, 
            'transactions': [],
            'nonce': 190395
        }
        self.genisis_hash = "00000868219e3eeffeb4d11f153d106980878ed4d0815b21e59cec73bbf377a7"
        self.blockchain = [self.genisis_block]
        self.open_transactions = []
        self.owner = 'Jonathan'
        self.difficulty = 5
        self.participants = set()
        self.reward = 50.0
    
    def display_blockchain(self):
        print(self.blockchain)
        for block in self.blockchain:
            print(block)

    def read_blockchain(self):
        while True:
            user_input = input("Please enter a filename (save_blockchain.txt or [Q]uit): ") or "save_blockchain.txt"
            if user_input.casefold() in ['q', 'quit']:
                return None
            if os.path.isfile(user_input) and not os.path.isabs(user_input):
                data = open(user_input, 'r').read()
                return json.loads(data)
            else:
                print("Invalid filename or not in local directory")
                continue

    def write_blockchain(self):
        data = json.dumps(self.blockchain)
        while True:
            user_input = input("Please enter a filename (save_blockchain.txt or [Q]uit): ") or "save_blockchain.txt"
            if user_input.casefold() in ['q', 'quit']:
                return None
            if os.path.isfile(user_input) and not os.path.isabs(user_input):
                with open(user_input, 'w') as blockchain_file:
                    blockchain_file.write(data)
                    print("Blockchain saved to disk")
                break   
            else:
                print("Invalid filename or not in local directory")
                continue

    def get_last_blockchain_value(self):
        try:
            return self.blockchain[-1]
        except:
            return [0]
    
    def add_transaction(self, sender, recipient, amount=0.0):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        self.open_transactions.append(transaction)
        print(self.open_transactions)

    def mine_block(self, miner='Jon'):
        leading_zeros = self.difficulty * "0"
        if self.open_transactions == []:
            print("please submit a transaction first!!!")
            return
        previous_block = self.blockchain[-1]
        previous_block_as_hash = hash_block(previous_block)
        index_of_this_Block = len(self.blockchain)
        nonce = 0
        passes_check = False
       
        block = {
            'previous_hash': previous_block_as_hash,
            'index': index_of_this_Block,
            'transactions': self.open_transactions,
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
        self.blockchain.append(block)
        self.open_transactions = []
        print(f"paying the miner, {miner} the mining fee of {self.reward}")
        self.add_transaction('Mining_Rewards', miner, self.reward)

class Block:
    def __init__(self, previous_hash, index, transactions, nonce):
        self.previous_hash = previous_hash
        self.index = index
        self.transactions = transactions
        self.nonce = nonce

class Transactions:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

class Participants:
    def __init__(self, owner, participants):
        self.owner = owner
        self.participants = participants

def hash_block(block):
    return hashlib.sha256(json.dumps(block).encode()).hexdigest()

def get_user_input():
    ''' returns the user input'''
    return input('Please choose: ')

def get_transaction_values():
    while True:
        transaction_sender = input('Sender: ')
        transaction_recipient = input('Recipient: ')
        transaction_amount = input('Amount / (C)ancel: ')
        if transaction_amount == 'q' or transaction_amount.casefold() in ['c', 'cancel']:
            return None
        try:
            transaction_amount = float(transaction_amount)
            return transaction_sender, transaction_recipient, transaction_amount
        except:
            print('Invalid input')
            continue
waiting_for_input = True
blockchain_obj = Blockchain()
while waiting_for_input:
    print("""Please choose one:
    1. Add transaction amount pending transactions (open_transactions)
    2. Print entire blockchain
    3. Print open transactions
    4. Load/Save the blockchain (save_blockchain.txt)
    5. Verify Blockchain
    6. Mine ALL Transactions to blockchain
    7. Get Participants
    8. Get all Balances (must load all participants first)
    9. Mine only valid transactions to blockchain (no double spending)
    Q. (Q)uit session""")
    answer = get_user_input()
    if answer == '1':
        receipient_and_amount = get_transaction_values()
        sender = receipient_and_amount[0]
        recipient = receipient_and_amount[1]
        amount = receipient_and_amount[2]
        if receipient_and_amount != 'done':
            blockchain_obj.add_transaction(sender, recipient, amount)
    elif answer == '2':
        print('this is the entire blockchain:')
        blockchain_obj.display_blockchain()
    elif answer == '3':
        print('this is the open transactions (itemized): ')
        for i, transaction in enumerate(blockchain_obj.open_transactions):
            print(f'transaction {i+1}:')
            blockchain_obj.display_transaction(transaction)
            print('\n')
        print('open transactions in raw format:')
        print(blockchain_obj.open_transactions)
    elif answer == '4':
        load_save_answer = input('Load/Save/Exit: ')
        if load_save_answer.casefold() in ['l', 'load']:
            blockchain_obj.blockchain = blockchain_obj.read_blockchain()
            print('\nVerify blockchain before continuing (Option 4)')
        elif load_save_answer.casefold() in ['s', 'save']:
            print('\nASSUMING you verified FIRST')
            blockchain_obj.write_blockchain()
        else:
            continue
    elif answer == '5':
        blockchain_obj.verify_blockchain()
    elif answer == '6':
        blockchain_obj.open_transactions, blockchain_obj.blockchain = blockchain_
        obj.mine_block()
    elif answer == '7':
        print('was: ', blockchain_obj.participants)
        blockchain_obj.participants = blockchain_obj.get_participants()
        print('now: ', blockchain_obj.participants)
    elif answer == '8':
        for participant in blockchain_obj.participants:
            print(f"{participant} has {blockchain_obj.get_balance(participant)}")
    elif answer == '9':
        current_balances = blockchain_obj.create_balances()
        if blockchain_obj.verify_blockchain():
            valid_transactions, invalid_transactions = blockchain_obj.commit_transactions(current_balances)
        blockchain_obj.open_transactions, blockchain_obj.blockchain = blockchain_obj.mine_block(valid_transactions)
        blockchain_obj.open_transactions.extend(invalid_transactions)
        print('the following transactions were invalid and have been added back to the open_transactions list:')
        print(blockchain_obj.open_transactions)
    elif answer in ['q', 'Q']:
        is_sure = input('Are you sure - UNSAVED changes will be LOST (y/N): ')
        if is_sure.casefold() in ['y', 'yes']:
            waiting_for_input = False
        else:
            print('Selection not recognized')
            # restart question
    print('Thank you for your visit to my blockchain, have a nice day')
