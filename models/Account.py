from mongoengine import *
import datetime

connect('PyCoin')


class Accounts(Document):

    account_id = StringField(
        required=True
    )

    timestamp = DateTimeField(
        default=datetime.datetime.now,
        required=True
    )

    transactions = ListField(
    )

    amount = LongField(
        default=0,
        required=True
    )


