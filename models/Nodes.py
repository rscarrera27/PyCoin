from mongoengine import *


class Node(Document):
    node_url = StringField(
        required=True
    )
