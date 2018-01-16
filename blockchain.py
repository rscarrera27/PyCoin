class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        pass

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
    def hash(self):
        pass

    @property
    def last_block(self):
        pass

