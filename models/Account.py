from mongoengine import *
import datetime

connect('BlockChain')

class Account(Document):

    id = StringField(
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


