from mongoengine import *
import datetime

connect('PyCoin')


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

    @staticmethod
    def resolve_consensus(new_chain):

        Block.drop_collection()

        for block in new_chain:
            Block(index=block["index"],
                  timestamp=block["timestamp"],
                  transactions=block['transactions'],
                  proof=block["proof"],
                  previous_hash=block["previous_hash"]
                  ).save()

            return True
