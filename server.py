from flask import Flask, jsonify, request
from PyCoin.blockchain import *
from PyCoin.account import *
from PyCoin.hash_cash import *

app = Flask(__name__)

blockchain = Blockchain(Account())


@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    node_identifier = request.args.get("node_identifier")

    if type(node_identifier) != str:
        if Account.check_id("0", node_identifier) is False:
            return jsonify({'message': "Wrong argument"}), 403

    proof = HashCash.proof_of_work(last_proof)

    blockchain.new_transactions(
        sender='0',
        recipient=node_identifier,
        amount=1
    )

    previous_hash = HashCash.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'new block forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

    return jsonify(response), 200


@app.route('/id/apply', methods=['POST'])
def apply_account():

    values = request.get_json()

    account_id = values.get('id')
    print(account_id)

    if Account.apply_acount(account_id):
        response = jsonify({'message': 'ID was applied'}), 201
    else:
        response = jsonify({'message': 'requested ID is existing'}), 400

    return response


@app.route('/transactions', methods=['GET'])
def transactions():

    response = {
        'current transactions': blockchain.current_transactions,
        'length': len(blockchain.current_transactions)
    }

    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    print(values)

    check, index = blockchain.new_transactions(values['sender'], values['recipient'], values['amount'])

    if check:
        response = jsonify({'message': 'Transaction will be added to Block {0}'.format(index)}), 201
    else:
        response = jsonify({'message': 'Requested transaction is rejected'}), 403

    return response


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
    app.run(host='0.0.0.0', port=3000)
