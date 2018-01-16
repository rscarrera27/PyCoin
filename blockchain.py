import hashlib
import json
from time import time

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(previous_hash=1, proof=100) #Make Genesis block

    def new_block(self, proof, previous_hash=None):

        """
        :param proof: proof of work
        :param previous_hash: previous hash
        :return: created block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transactions(self, sender, recipient, amount):

        """
        :param sender: address of sender
        :param recipient: address for receive
        :param amount: amount of cryptocurrency
        :return: next block of last block

        method for make new transactions
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        print(block)
        block_string = json.dumps(block, sort_keys=True)
        print(type(block_string))
        return hashlib.sha256(str(block_string).encode()).hexdigest()

    @property
    def last_block(self):

        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        :param last_proof: last proof
        :return: matched proof
        """

        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        :param last_proof:
        :param proof:
        :return:
        """

        guess = str(last_proof * proof).encode()
        return hashlib.sha256(guess).hexdigest()[:4] == '0000' #set difficulty

