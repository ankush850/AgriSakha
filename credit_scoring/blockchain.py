from dataclasses import dataclass
from datetime import datetime
import hashlib
import json

@dataclass
class Block:
    index: int
    timestamp: str
    data: dict
    previous_hash: str
    hash: str = ""

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}".encode())
        return sha.hexdigest()

class AgriBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(
            index=0,
            timestamp=str(datetime.now()),
            data={"message": "Genesis Block"},
            previous_hash="0"
        )

    def add_block(self, farmer_data: dict):
        last_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            timestamp=str(datetime.now()),
            data=farmer_data,
            previous_hash=last_block.hash
        )
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        return new_block

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True