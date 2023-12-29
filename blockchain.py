import hashlib
import time

class Block:
    def __init__(self, index, previous_block_hash, timestamp, transaction_data, hash):
        self.index = index
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp
        self.transaction_data = transaction_data
        self.hash = hash

def calculate_hash(index, previous_block_hash, timestamp, transaction_data):
    return hashlib.sha256(f"{index}{previous_block_hash}{timestamp}{transaction_data}".encode()).hexdigest()

def create_genesis_block():
    # Let's start this amazing blockchain journey with a bang!
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

def create_new_block(previous_block, transaction_data):
    # Ready to forge a new block and add it to the chain!
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, previous_block.hash, timestamp, transaction_data)
    return Block(index, previous_block.hash, timestamp, transaction_data, hash)

# Blockchain creation and adding blocks!
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# The number of blocks we'll be adding to the chain
num_blocks_to_add = 5

for i in range(num_blocks_to_add):
    new_block_transaction_data = f"Block #{i+1}: Transactions data"
    new_block = create_new_block(previous_block, new_block_transaction_data)
    blockchain.append(new_block)
    previous_block = new_block
    print(f"🔗 Block #{new_block.index} added to blockchain!")
    print(f"🔒 Hash: {new_block.hash}\n")

print("🎉 Congratulations! We've built our first blockchain!\n")
print("📜 Blockchain details:")
for block in blockchain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_block_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transaction_data: {block.transaction_data}")
    print(f"Hash: {block.hash}\n")

#tempering with the data and verifying if blockchain is valid
# Tamper with the data in Block #3 (index 3)
blockchain[3].transaction_data = "Block #3 (modified)"

# Check if the blockchain is still valid
def is_blockchain_valid(chain):
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i - 1]

        # Check if the hash of the previous block matches the 'previous_block_hash' field of the current block
        if current_block.previous_block_hash != calculate_hash(previous_block.index, previous_block.previous_block_hash,
 previous_block.timestamp, previous_block.transaction_data):
            return False

        # Check if the hash of the current block is valid (meets certain criteria)
        if current_block.hash != calculate_hash(current_block.index, current_block.previous_block_hash,
                                                current_block.timestamp, current_block.transaction_data):
            return False

    return True

# Check if the blockchain is valid
print("Is the blockchain valid?", is_blockchain_valid(blockchain))
