import json
import hashlib

def hash_block(block):
    this_block_as_string = json.dumps(block)
    return hashlib.sha256(this_block_as_string.encode()).hexdigest()

blockchain = [{"previous_hash": "None", "index": 0, "transactions": [], "nonce": 190395}, {"previous_hash": "00000868219e3eeffeb4d11f153d106980878ed4d0815b21e59cec73bbf377a7", "index": 1, "transactions": [{"sender": "Jon", "recipient": "Italy", "amount": 5.0}], "nonce": 1707570}, {"previous_hash": "00000608878c88a3c02bc19c3dd8f106ed24fe49867cde0f4508394406af1801", "index": 2, "transactions": [{"sender": "Mining_Rewards", "recipient": "Jon", "amount": 50.0}, {"sender": "Italy", "recipient": "Pickle", "amount": 1.0}], "nonce": 1229733}]

open_transactions = [{'sender': 'Italy', 'recipient': 'Winter', 'amount': 4.0}, {'sender': 'Italy', 'recipient': 'Winter', 'amount': 2.0}, {'sender': 'Italy', 'recipient': 
'Winter', 'amount': 2.0}]

# def verify_blockchain(blockchain, open_transactions):
#     """
#     Verify the integrity of the blockchain and update the balances of each person
#     based on the transactions in the open_transactions list and the blockchain.

#     Args:
#         blockchain (list): The blockchain to be verified
#         open_transactions (list): The list of open transactions to be included in the verification process

#     Returns:
#         bool: True if the blockchain is valid, False otherwise
#         dict: A dictionary containing the current balances of each person
#         list: A list of valid transactions that have been added to the blockchain
#     """
#     current_balances = {}
#     valid_transactions = []
#     for block in blockchain:
#         for transaction in block['transactions']:
#             if transaction['sender'] not in current_balances:
#                 current_balances[transaction['sender']] = 0
#             if transaction['recipient'] not in current_balances:
#                 current_balances[transaction['recipient']] = 0

#             current_balances[transaction['sender']] -= transaction['amount']
#             current_balances[transaction['recipient']] += transaction['amount']
#             valid_transactions.append(transaction)

#     for transaction in open_transactions:
#         if transaction['sender'] not in current_balances:
#             current_balances[transaction['sender']] = 0
#         if transaction['recipient'] not in current_balances:
#             current_balances[transaction['recipient']] = 0

#         if current_balances[transaction['sender']] - transaction['amount'] >= 0:
#             current_balances[transaction['sender']] -= transaction['amount']
#             current_balances[transaction['recipient']] += transaction['amount']
#             valid_transactions.append(transaction)
#         else:
#             print(f"Transaction dropped: {transaction['sender']} has insufficient funds to send {transaction['amount']} to {transaction['recipient']}")

#     for person in current_balances:
#         if current_balances[person] < 0:
#             print(f"{person} has overspent their balance!")
#             return False, current_balances, valid_transactions

#     for i in range(1, len(blockchain)):
#         if blockchain[i]['previous_hash'] != hash_block(blockchain[i-1]):
#             print("The blockchain is compromised!")
#             return False, current_balances, valid_transactions

#     print("The blockchain is valid.")
#     return True, current_balances, valid_transactions


def commit_transactions(blockchain, open_transactions, current_balances):
    """
    Commit the valid transactions to the blockchain and update the current_balances dictionary.

    Args:
        blockchain (list): The blockchain to be updated
        open_transactions (list): The list of open transactions to be included
        current_balances (dict): A dictionary containing the current balances of each person

    Returns:
        list: A list of valid transactions that have been added to the blockchain
    """
    valid_transactions = []
    for transaction in open_transactions:
        if current_balances[transaction['sender']] - transaction['amount'] >= 0:
            current_balances[transaction['sender']] -= transaction['amount']
            current_balances.setdefault(transaction['recipient'], 0)
            current_balances[transaction['recipient']] += transaction['amount']

            valid_transactions.append(transaction)
        else:
            print(f"Transaction dropped: {transaction['sender']} has insufficient funds to send {transaction['amount']} to {transaction['recipient']}")
    return valid_transactions

def create_balances(blockchain):
    """
    Create a dictionary containing the current balances of each person based on the transactions in the blockchain.

    Args:
        blockchain (list): The blockchain to be verified

    Returns:
        dict: A dictionary containing the current balances of each person
    """
    current_balances = {}
    for block in blockchain:
        for transaction in block['transactions']:
            if transaction['sender'] not in current_balances:
                current_balances[transaction['sender']] = 0
            if transaction['recipient'] not in current_balances:
                current_balances[transaction['recipient']] = 0

            current_balances[transaction['sender']] -= transaction['amount']
            current_balances[transaction['recipient']] += transaction['amount']
    return current_balances

def verify_blockchain(blockchain):
    """
    Verify the integrity of the blockchain.

    Args:
        blockchain (list): The blockchain to be verified

    Returns:
        bool: True if the blockchain is valid, False otherwise
    """
    for i in range(1, len(blockchain)):
        if blockchain[i]['previous_hash'] != hash_block(blockchain[i-1]):
            print("The blockchain is compromised!")
            return False
    print("The blockchain is valid.")
    return True


current_balances = create_balances(blockchain)

if verify_blockchain(blockchain):
    valid_transactions = commit_transactions(blockchain, open_transactions, current_balances)
    print(valid_transactions)