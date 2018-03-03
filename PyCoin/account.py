from models.Account import *
from PyCoin.exceptions import *


def valid_transactions(transaction):

    sender = transaction.sender
    recipient = transaction.recipient
    requested_amount = transaction.amount

    try:
        queried_amount = Accounts.objects(account_id=sender)[0].amount

    except:
        raise DBAccessError('an error raised while trying to creating the transaction ')

    balance = queried_amount - requested_amount

    if balance < 0:
        raise ValueError("requested amount {0} coin is not valid: \
        Your account balance is insufficient.".format(requested_amount))

    else:
        try:
            Accounts.objects(account_id=sender).update_one(set__amount=balance)
            Accounts.objects(account_id=recipient).update_one(inc__amount=requested_amount)

        except:
            raise DBAccessError('an error raised while trying to creating the transaction ')

        return True


def update_transaction_info(transaction):

    sender = transaction.sender
    recipient = transaction.recipient

    try:
        Accounts.objects(account_id=sender).update_one(push__transactions=transaction)
        Accounts.objects(account_id=recipient).update_one(push__transactions=transaction)

    except:
        raise DBAccessError('an error raised while trying to creating the transaction ')

    return True


def apply_account(apply):

    if len(Accounts.objects(account_id=apply)) is 0:
        try:
            Accounts(
                account_id=apply
            ).save()

        except:
            raise DBAccessError('an error raised while trying to creating the transaction ')

        return True

    else:
        raise ValueError('Already Exists')
