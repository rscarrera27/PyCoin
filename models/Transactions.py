from mongoengine import *


class Transactions(EmbeddedDocument):

    sender = StringField(
        required=True
    )
    recipient = StringField(
        required=True
    )
    amount = LongField(
        required=True
    )
