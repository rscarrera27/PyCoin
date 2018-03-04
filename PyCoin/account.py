from models.Account import *
from PyCoin.exceptions import *


def valid_transactions(transaction):

    sender = transaction.sender
    recipient = transaction.recipient
    requested_amount = transaction.amount

    queried_amount = Accounts.objects(account_id=sender)[0].amount

    balance = queried_amount - requested_amount

    if balance < 0:
        raise ValueError("requested amount {0} coin is not valid: \
        Your account balance is insufficient.".format(requested_amount))

    else:
        Accounts.objects(account_id=sender).update_one(set__amount=balance)
        Accounts.objects(account_id=recipient).update_one(inc__amount=requested_amount)

        return True


def update_transaction_info(transaction):

    sender = transaction.sender
    recipient = transaction.recipient

    Accounts.objects(account_id=sender).update_one(push__transactions=transaction)
    Accounts.objects(account_id=recipient).update_one(push__transactions=transaction)

    return True


def apply_account(apply):

    if len(Accounts.objects(account_id=apply)) is 0:

        Accounts(
            account_id=apply
        ).save()

        return True

    else:
        raise ValueError('Already Exists')


def check_id(account_id):

    check_id = not (len(Accounts.objects(account_id=account_id)) is 0)

    if not (check_recipient_id and check_sender_id):
        raise
    else:
        return True
