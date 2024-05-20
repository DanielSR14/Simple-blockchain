import hashlib
from datetime import datetime
import json
import os


class Block:
    
    def __init__(self, index, previous_hash, datetime, data, sender, 
                 recipient, amount, custom_data):
        
        self.index = index
        self.previous_hash = previous_hash
        self.datetime = datetime
        self.data = data
        self.nonce = 0
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.custom_data = custom_data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.datetime).encode('utf-8') +
            str(self.nonce).encode('utf-8') +
            str(self.sender).encode('utf-8') +
            str(self.recipient).encode('utf-8') +
            str(self.amount).encode('utf-8') +
            str(self.custom_data).encode('utf-8') 
        )

        return sha.hexdigest()

class Blockchain:

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def load_chain(self):
        if os.path.exists("blockchain.json"):
            with open("blockchain.json", "r") as json_file:
                blockchain_data = json.load(json_file)
                chain = []
                for block_data in blockchain_data:
                    block = Block(block_data['index'], block_data['previous_hash'], 
                                  block_data['timestamp'], block_data['data'], 
                                  block_data['sender'], block_data['recipient'], 
                                  block_data['amount'], block_data['custom_data'])
                    chain.append(block)
                return chain
        else:
            return [self.create_genesis_block()]
        
    def create_genesis_block(self):
        return Block(0, datetime.now(), 'Genesis Block', '0', '', '', 0, '')

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash

        while True:
            if new_block.hash[:5] == '0' * 5:  
                break
            new_block.nonce +=1
            new_block.hash = new_block.calculate_hash()
       
        self.chain.append(new_block)


    def valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
            
            return True

    def print_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Timestamp: {block.datetime}")
            print(f"Data: {block.data}")
            print(f"Sender: {block.sender}")
            print(f"Recipient: {block.recipient}")
            print(f"Amount: {block.amount}")
            print(f"Custom Data: {block.custom_data}")
            print(f"Nonce: {block.nonce}")
            print(f"Hash: {block.hash}")
            print("-" * 50)
        

    def save_json(self, file):
        blockchain_data = []

        for block in self.chain:
            block_data = {
                'index' : block.index,
                'previous_hash' : block.previous_hash,
                'timestamp': block.datetime,
                'data' : block.data,
                'sender' : block.sender,
                'recipient' : block.recipient,
                'amount' : block.amount,
                'custom_data' : block.custom_data,
                'nonce' : block.nonce,
                'hash' : block.hash 
            }

            blockchain_data.append(block_data)
        
        with open(file, 'w') as json_file:
            json.dump(blockchain_data, json_file, indent=4, default=str)


b1 = Blockchain()

user_choice = 0

while user_choice != 3:
    print('\n- - - Menu Blockchain - - -')
    print('1. Transaction')
    print('2. Blockchain')
    print('3. Exit')

    user_choice = input('Choose an option: ')

    if user_choice == '1':
        sender = input('Enter sender: ')
        recipient = input('Enter recipient: ')
        amount = float(input('Enter amount: '))
        custom_data = input('Enter custom data for the transaction: ')

        inicial_time = datetime.now()

        b1.add_block(Block(len(b1.chain), b1.chain[-1].hash,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
        f'Transaction: {sender} to {recipient} - Amount: {amount}',
        sender, recipient, amount, custom_data))

        final_time = datetime.now()
        total_time = final_time - inicial_time
        elapsed_seconds = total_time.total_seconds()
        print(f'Transaction added successfully!, Elapsed Time (s): {elapsed_seconds} ')

        b1.save_json("blockchain.json")
    elif user_choice == '2':
        print()
        b1.print_chain()

    elif user_choice == '3':
        print('Exiting...')
        break

    else:
        print('Invalid choice, please try again.')
