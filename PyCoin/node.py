import requests
from models.Nodes import *
from models.Block import *
from PyCoin.blockchain import Blockchain
from urllib.parse import urlparse


def register_node(address):

    parsed_url = urlparse(address)
    Node(node_url=parsed_url.netloc).save()

    return True


def resolve_conflict():

    new_chain = None

    max_length = Block.objects.count()

    for node in Node.objects:

        response = requests.get('https://{0}/chain'.format(node.node_url))

        if response.status_code == 200:
            response = response.json()
            length = response['length']
            chain = response['chain']

            if length > max_length and Blockchain.valid_chain(chain):
                max_length = length
                new_chain = chain

    if new_chain is not None:
        Block.resolve_consensus(new_chain)

        return True

    return False
