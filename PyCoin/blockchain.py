import requests
from models import *
from PyCoin.hash_cash import *
from urllib.parse import urlparse


class Blockchain(object):

    def __init__(self, account):
        self.current_transactions = []
        self.Account = account

        if len(Block.objects) == 0:
            print("Chain initialized on {0}".format(datetime.datetime.now()))

            self.chain = []
            self.new_block(previous_hash=1, proof=100)

        else:
            print("Chain loaded from database on {0}".format(datetime.datetime.now()))

            self.chain = []
            for block in Block.objects:
                self.chain.append({
                    'index': block.index,
                    'timestamp': str(block.timestamp),
                    'transactions': block.transactions,
                    'proof': block.proof,
                    'previous_hash': block.previous_hash
                })

        if len(Node.objects) == 0:
            print("Node list initialized on {0}".format(datetime.datetime.now()))

            self.nodes = []

        else:
            print("Node list loaded from database on {0}".format(datetime.datetime.now()))

            self.nodes = []
            for node in Node.objects:
                self.nodes.append({
                    "node_url": node.node_url
                })

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.append(parsed_url.netloc)
        Node(node_url=parsed_url.netloc).save()
        print(parsed_url)

    def resolve_conflict(self):

        neigbours = self.nodes
        new_chain = None

        max_length = len(self.chain)

        for node in neigbours:
            response = requests.get('https://{0}/chain'.format(node))

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                if length > max_length and Blockchain.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain

            Block.resolve_consensus(self.chain)

            return True

        return False

    def new_block(self, proof, previous_hash=None):

        """
        :param proof: proof of work
        :param previous_hash: previous hash
        :return: created block
        """
        print(self.current_transactions)

        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or HashCash.hash(self.chain[-1])
        }

        self.chain.append(block)
        Block(
            index=len(self.chain),
            transactions=self.current_transactions,
            proof=proof,
            previous_hash=str(previous_hash or HashCash.hash(self.chain[-1]))
        ).save()

        self.current_transactions = []

        return block

    def new_transactions(self, sender, recipient, amount):

        """
        :param sender: address of sender
        :param recipient: address for receive
        :param amount: amount of cryptocurrency
        :return: next block of last block

        method for make new transactions
        """
        requested_transactions = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        if self.Account.check_id(sender, recipient) is False:
            return False, self.last_block['index'] + 1
        else:
            pass

        if self.Account.valid_transactions(requested_transactions) is True:
            self.current_transactions.append(requested_transactions)
            self.Account.update_transactions_info(sender, recipient, requested_transactions)

            return True, self.last_block['index'] + 1

        else:
            return False, self.last_block['index'] + 1

    @property
    def last_block(self):

        return self.chain[-1]

    @staticmethod
    def valid_chain(chain):

        last_block = chain[0]
        for current_index in chain:
            block = chain[current_index]

            print('last block : {0}\nblock : {1}\n--------------------\n'.format(last_block, block))

            if block['previous_hash'] != HashCash.hash(last_block):
                return False

            if not HashCash.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True
