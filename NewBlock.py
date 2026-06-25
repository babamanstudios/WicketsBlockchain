import hashlib
import time
import json
from CURSOR import *
from NewWicket import wicket_ID

def data_pickout(id):
    cursor = define_cursor(start())
    cursor.execute(""" SELECT * 
    FROM WICKETS
    WHERE ID = ?
    """,(id,))
    record = cursor.fetchone()
    stop(start())
    return record
class Block:
    def __init__(self, num, wicket_data, previous_hash):
        self.num = wicket_ID
        self.timestamp = time.time()
        self.wicket_data = data_pickout(wicket_ID)
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "ID": self.num,
            "timestamp": self.timestamp,
            "wicket_data": self.wicket_data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)

        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.chain.append(self.nya_block())

    def nya_block(self):
        genesis_data = {
            "ID": "GENESIS",
            "Date": None,
            "Bowler": None,
            "Batsman": None,
            "Batsman_team": None,
            "Bowler_team": None,
            "runs": None,
            "wickets": None,
            "venue_country": None,
            "Vid": None
        }
        return Block(genesis_data, "0")

    def block_load(self):
        return self.chain[-1]

    def add_block(self, wicket_data):
        previous_block = self.block_load()
        new_block = Block(
            wicket_data=wicket_data,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)
        return new_block

def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i - 1]
        if current.hash != current.calculate_hash():
            return False
        if current.previous_hash != previous.hash:
            return False
    return True