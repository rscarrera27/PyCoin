from models.Account import *


class Account:

    def __init__(self):
        pass

    @staticmethod
    def valid_transactions(transations):

        sender = transations['sender']
        requested_amount = transations['amount']
        queried_amount = Account.objects(id=sender).amount

        balance = queried_amount - requested_amount

        if balance < 0:
            return False
        else:
            Account.objects(id=sender).update_one(amount=balance)
            return True

    @staticmethod
    def update_transactions_info(sender_id, recipient_id, transaction):

        Account.objects(id=sender_id).update_one(push__transactions=transaction)
        Account.objects(id=recipient_id).update_one(push__transactions=transaction)

    @staticmethod
    def apply_acount(id):

        Account(
            id=id
        ).save()
