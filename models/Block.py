from models.Transactions import *
from mongoengine import *
import datetime


connect('BlockChain')

class Block(Document):

    index = LongField(
        required=True
    )

    timestamp = DateTimeField(
        default=datetime.datetime.now,
        required=True
    )

    transactions = ListField(
    )

    proof = LongField(
        required=True
    )

    previous_hash = StringField(
        required=True
    )
