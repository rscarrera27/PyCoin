from mongoengine import *

connect("PyCoin")

class Node(Document):
    node_url = StringField(
        required=True
    )
