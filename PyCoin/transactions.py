class Transaction(object):

    def __init__(self, sender, recipient, amount):
            self.sender = sender
            self.recipient = recipient
            self.amount = amount

    @property
    def transaction_data(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }
