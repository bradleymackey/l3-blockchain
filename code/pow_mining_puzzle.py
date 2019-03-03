import hashlib
import json
import time

# An example block header - do not change any fields except nonce and coinbase_addr
example_block_header = {'height': 1478503,
                        'prev_block': '0000000000000da6cff8a34298ddb42e80204669367b781c87c88cf00787fcf6',
                        'total': 38982714093,
                        'fees': 36351,
                        'size': 484,
                        'ver': 536870912,
                        'time': 1550603039.882228,
                        'bits': 437239872,
                        'nonce': 3856645,              #You may change this field of the block
                        'coinbase_addr': 'wbbz74',     #You should change this field of the block to your studentID
                        'n_tx': 2,
                        'mrkl_root': '69224771b7a2ed554b28857ed85a94b088dc3d89b53c2127bfc5c16ff49da229',
                        'txids': ['3f9dfc50198cf9c2b0328cd1452513e3953693708417440cd921ae18616f0bfc', '3352ead356030b335af000ed4e9030d487bf943089fc0912635f2bb020261e7f'],
                        'depth': 0}

print("VALID BLOCK:")
# Simplified conversion of block header into bytes:
block_serialised = json.dumps(example_block_header, sort_keys=True).encode()
# Double SHA256 hashing of the serialised block
block_hash = hashlib.sha256(hashlib.sha256(block_serialised).digest()).hexdigest()
print('Hash with nonce ' + str(example_block_header['nonce'])+': '+block_hash)


##### CALCULATE VALID NONCE
print()
print("RECALCULATING VALID NONCE:")

DIFFICULTY = 0.001
max_target = 0x00000000FFFF0000000000000000000000000000000000000000000000000000
current_target = int(max_target/DIFFICULTY)
print(f"current target: {current_target:x}")

start_time = time.time()

nonce = 0
while True:
    # update the nonce
    example_block_header['nonce'] = nonce
    # progress updates
    if nonce % 100000 == 0:
        print("nonce", nonce)

    # Simplified conversion of block header into bytes:
    block_serialised = json.dumps(example_block_header, sort_keys=True).encode()
    # Double SHA256 hashing of the serialised block
    block_hash = hashlib.sha256(hashlib.sha256(block_serialised).digest()).hexdigest()
    #print('Hash with nonce ' + str(example_block_header['nonce'])+': '+block_hash)

    current_hash = int(block_hash, 16)
    if current_hash<current_target:
        print("VALID BLOCK")
        print(f"nonce {nonce}")
        print(f"hash {block_hash}")
        break

    # increment the nonce for the next check
    nonce += 1

end_time = time.time() - start_time
print(f"time taken: {end_time:.2f}s")