from models.Transactions import *
from mongoengine import *
import datetime


class Block(Document):

    index = LongField(
        required=True
    )

    timestamp = DateTimeField(
        default=datetime.datetime.now,
        required=True
    )

    transactions = ListField(
        EmbeddedDocumentField(
            document_type=Transactions
        )
    )

    proof = LongField(
        required=True
    )

    previous_hash = StringField(
        required=True
    )
