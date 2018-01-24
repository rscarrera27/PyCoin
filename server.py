from flask import Flask, jsonify, request
from uuid import uuid4

from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']

    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transactions(
        sender='0',
        recipient=node_identifier,
        amount=1
    )

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'new block forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    print(values)

    check, index = blockchain.new_transactions(values['sender'], values['recipient'], values['amount'])

    response = {'message': 'Transaction will be added to Block {0}'.format(index)}

    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

    return jsonify(response), 200


@app.route('/nodes/register', methods=['POST'])
def register_nodes():

    values = request.get_json()

    nodes = values.get('nodes')
    print(nodes)

    if nodes is None or type(nodes) == str:
        return "Error : unvalid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New Nodes hav been successfully added',
        'total_nodes': list(blockchain.nodes)
    }

    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflict()

    if replaced:
        response = {
            'message': 'Conflict on chain has been successfully solved',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': "There's no conflict in chain. nothing has changed",
            'chain': blockchain.chain
        }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
