import hashlib
import time


class Transcation:

    def __init__(self, send_addr, rcv_addr, amount):
        self.send_addr = send_addr
        self.rcv_addr = rcv_addr
        self.amount = amount


class Block:

    def __init__(self, transactions):
        self.timestamp = time.time()
        self.transactions = transactions
        self.nonce = 0
        self.prev_hash = ""
        self.cur_hash = self.calculate_hash()

    def calculate_hash(self):
        data = list(map(str, [self.timestamp, self.transactions, self.nonce, self.prev_hash]))
        h = hashlib.sha256("".join(data).encode())
        return h.hexdigest()

    def mine_block(self, diff):
        while not self.cur_hash.startswith("0"*diff):
            self.nonce += 1
            self.cur_hash = self.calculate_hash()

    def __repr__(self):
        return str({
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "nonce": self.nonce,
            "previous_hash": self.prev_hash,
            "cur_hash": self.cur_hash
        })


class BlockChain:

    def __init__(self):
        self.chain = [Block([])]
        self.difficulty = 3
        self.pending_transactions = []
        self.miner_reward = 100

    def mine_pending_transactions(self, miner_addr):
        block = Block(self.pending_transactions)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = [
            Transcation(None, miner_addr, self.miner_reward)
            ]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance(self, addr):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.send_addr == addr:
                    balance -= transaction.amount
                if transaction.rcv_addr == addr:
                    balance += transaction.amount
        return balance

