from mongoengine import *


class Transactions(EmbeddedDocument):

    sender = StringField(
        required=True
    )
    recipent = StringField(
        required=True
    )
    amount = LongField(
        required=True
    )
