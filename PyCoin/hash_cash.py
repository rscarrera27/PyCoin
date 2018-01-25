import hashlib
import json


class HashCash:

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True)
        return hashlib.sha256(str(block_string).encode()).hexdigest()

    @staticmethod
    def proof_of_work(last_proof):
        """
        :param last_proof: last proof
        :return: matched proof
        """

        proof = 0

        while HashCash.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        :param last_proof:
        :param proof:
        :return:
        """

        guess = str(last_proof * proof).encode()
        return hashlib.sha256(guess).hexdigest()[:6] == '000000'  # set difficulty

