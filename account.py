from models.Account import *


class Account:

    def __init__(self):
        check = self.apply_acount("0")
        if check is True:
            print("Genesis account spawned")
            Accounts.objects(account_id="0").update_one(set__amount=210000000)
        else:
            pass

    @staticmethod
    def valid_transactions(transations):

        sender = transations['sender']
        recipient = transations['recipient']
        requested_amount = transations['amount']
        queried_amount = Accounts.objects(account_id=sender)[0]
        queried_amount = queried_amount.amount

        balance = queried_amount - requested_amount

        if balance < 0:
            return False
        else:
            Accounts.objects(account_id=sender).update_one(set__amount=balance)
            Accounts.objects(account_id=recipient).update_one(inc__amount=requested_amount)
            return True

    @staticmethod
    def check_id(sender_id, recipient_id):

        check_sender_id = not (len(Accounts.objects(account_id=sender_id)) is 0)
        check_recipient_id = not (len(Accounts.objects(account_id=recipient_id)) is 0)

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
