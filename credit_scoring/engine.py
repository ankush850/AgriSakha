import json
import numpy as np
from datetime import datetime
import hashlib

class AgriBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = {
            'index': 0,
            'timestamp': str(datetime.now()),
            'data': "Genesis Block",
            'previous_hash': "0",
            'hash': self.calculate_hash(0, "0", str(datetime.now()), "Genesis Block")
        }
        self.chain.append(genesis)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(value).hexdigest()

    def add_block(self, farmer_data):
        previous_block = self.chain[-1]
        new_block = {
            'index': len(self.chain),
            'timestamp': str(datetime.now()),
            'data': farmer_data,
            'previous_hash': previous_block['hash'],
            'hash': self.calculate_hash(
                len(self.chain),
                previous_block['hash'],
                str(datetime.now()),
                json.dumps(farmer_data)
            )
        }
        self.chain.append(new_block)
        return new_block

class CreditEngine:
    def __init__(self):
        self.blockchain = AgriBlockchain()
        self.satellite_weights = {
            'crop_health': 0.6,
            'soil_moisture': 0.2,
            'acreage': 0.2
        }

    def get_satellite_data(self, farmer_id):
        """Mock ISRO Bhuvan API"""
        return {
            'crop_health': np.random.randint(60, 95),
            'soil_moisture': np.random.randint(30, 80),
            'acreage': round(np.random.uniform(1.0, 5.0), 2)
        }

    def calculate_score(self, farmer_id):
        data = self.get_satellite_data(farmer_id)
        
        # Calculate weighted score
        score = sum(
            data[k] * v 
            for k, v in self.satellite_weights.items()
        )
        
        # Store on blockchain
        block_data = {
            'farmer_id': farmer_id,
            'score': round(score, 2),
            'details': data,
            'timestamp': str(datetime.now())
        }
        self.blockchain.add_block(block_data)
        
        return {
            'credit_score': round(score),
            'details': data,
            'voice_response': (
                f"क्रेडिट स्कोर: {round(score)}. "
                f"फसल स्वास्थ्य: {data['crop_health']}%"
            )
        }

if __name__ == "__main__":
    engine = CreditEngine()
    result = engine.calculate_score("UP_FARMER_123")
    print(json.dumps(result, indent=2, ensure_ascii=False))