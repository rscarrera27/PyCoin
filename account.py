from models.Account import *


class Account:

    def __init__(self):
        pass

    @staticmethod
    def valid_transactions(transations):

        sender = transations['sender']
        requested_amount = transations['amount']
        queried_amount = Accounts.objects(account_id=sender)[0]
        queried_amount = queried_amount.amount

        balance = queried_amount - requested_amount

        if balance < 0:
            return False
        else:
            Accounts.objects(account_id=sender).update_one(set__amount=balance)
            return True

    @staticmethod
    def check_id(sender_id, recipient_id):
        check_sender_id = not (len(Accounts.objects(account_id=sender_id)) is 0)
        check_recipient_id = not (len(Accounts.objects(account_id=recipient_id)) is 0)

        print("account" + str(check_recipient_id and check_sender_id))
        print(Accounts.objects(account_id=sender_id))

        if not (check_recipient_id and check_sender_id):
            return False
        else:
            return True

    @staticmethod
    def update_transactions_info(sender_id, recipient_id, transaction):

        Accounts.objects(account_id=sender_id).update_one(push__transactions=transaction)
        Accounts.objects(account_id=recipient_id).update_one(push__transactions=transaction)

    @staticmethod
    def apply_acount(id):

        if len(Accounts.objects(account_id=id)) is 0:
            Accounts(
                account_id=id
            ).save()
            return True

        else:
            return False
