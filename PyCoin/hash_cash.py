from .. import CONFIG
import hashlib
import json


def block_hash(block):
    block_string = json.dumps(block, sort_keys=True)
    return hashlib.sha256(str(block_string).encode()).hexdigest()


def proof_of_work(last_proof):
    """
    :param last_proof: String
    :return: Int
    """

    proof = 0

    while valid_proof(last_proof, proof) is False:
        proof += 1

    return proof


def valid_proof(last_proof, proof):
    """
    :param last_proof: String
    :param proof: Int
    :return: Boolean
    """

    guess = str(last_proof * proof).encode()

    return hashlib.sha256(guess).hexdigest()[:6] == '0' * CONFIG.DIFFICULTY  # set difficulty


