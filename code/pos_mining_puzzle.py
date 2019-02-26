import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1
import time

# An the previous block header - do not change any fields
previous_block_header = {
  "previousBlockHash": "651c16a0226d2ddd961c9391dc11f703c5972f05805c4fb45ab1469dda1d4b98",
  "payloadLength": 209,
  "totalAmountNQT": "383113873926",
  "generationSignature": "9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1",
  "generator": "11551286933940986965",
  "generatorPublicKey": "feb823bac150e799fbfc124564d4c1a72b920ec26ce11a07e3efda51ca9a425f",
  "baseTarget": 1229782938247303,
  "payloadHash": "06888a0c41b43ad79c4e4991e69372ad4ee34da10d6d26f30bc93ebdf7be5be0",
  "generatorRS": "NXT-MT4P-AHG4-A4NA-CCMM2",
  "nextBlock": "6910370859487179428",
  "requestProcessingTime": 0,
  "numberOfTransactions": 1,
  "blockSignature": "0d237dadff3024928ea4e5e33613413f73191f04b25bad6b028edb97711cbd08c525c374c3e2684ce149a9abb186b784437d01e2ad13046593e0e840fd184a60",
  "transactions": ["14074549945874501524"],
  "version": 3,
  "totalFeeNQT": "200000000",
  "previousBlock": "15937514651816172645",
  "cumulativeDifficulty": "52911101533010235",
  "block": "662053617327350744",
  "height": 2254868,
  "timestamp": 165541326
}

# you should edit the effective balance to be the last two digits from your user id
effective_balance = 74

# create keys using the bitcoin curve alg
# sk = SigningKey.generate(SECP256k1)
# print(f"private: {sk.to_string().hex()}")
# vk = sk.get_verifying_key()
# print(f"public: {vk.to_string().hex()}")

# use pre-existing signing keys so we know they can't change
sk_string = "f3fdb06bc3e08e4d97849c7a599d78d5991a629cd446ecef25f8ec7a80adc657"
sk = SigningKey.from_string(bytes.fromhex(sk_string), SECP256k1)
vk_string = "14afbb92502c9294f19be099ac3fe51f8ea1c943e36a06c43b096864d887145b55e87f1a01b1b9275bcc9d528a2829a774ec6de06dfaed72933ced851105f3ba"
vk = VerifyingKey.from_string(bytes.fromhex(vk_string), SECP256k1)

# validate keypair
# signature = sk.sign(b"Hello World")
# print(f"signature: {signature.hex()}")
# assert vk.verify(signature, b"Hello World")

base_target = int(previous_block_header['baseTarget'])
block_timestamp = int(previous_block_header['timestamp'])
time_since_block = int(time.time()) - block_timestamp

target = base_target * time_since_block * effective_balance
print(f"target cal: {base_target} * {time_since_block} * {effective_balance}")
print(f"target: {target:x}")

prev_gen_signature = previous_block_header['generationSignature']
print(f"prev signature: {prev_gen_signature}")
gen_signature = sk.sign(bytes.fromhex(prev_gen_signature))
print(f"signed: {gen_signature.hex()}")
gen_hash = hashlib.sha256(gen_signature).digest()
print(f"hashed: {gen_hash.hex()}")

hit_bytes = gen_hash[:8]
print(f"hitval: {hit_bytes.hex()}")