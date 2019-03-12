import ecdsa

# put the hex of your public key in the line below
vk_string="14afbb92502c9294f19be099ac3fe51f8ea1c943e36a06c43b096864d887145b55e87f1a01b1b9275bcc9d528a2829a774ec6de06dfaed72933ced851105f3ba"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string),ecdsa.SECP256k1)

message = b'Hello world'

sk_string = "f3fdb06bc3e08e4d97849c7a599d78d5991a629cd446ecef25f8ec7a80adc657"
sk = ecdsa.SigningKey.from_string(bytes.fromhex(sk_string), ecdsa.SECP256k1)

sig = sk.sign(message)
print("Real signature:", sig.hex())

# put your signature for "Hello world" in the line below
sig_hex = "01a2d320d74c20dd7642ec39ed1643da3b9a72fb951accc50bf0ff00187c8d2cd34eb673b934985ae980631154ec21a15be94ac47bbfcd5cda77537927a3a5c5"
sig = bytes.fromhex(sig_hex)

print("Checking signature")
print("Message: "+str(message))

print("Signature: "+sig_hex)
print("Public key: "+vk_string)
try:
    vk.verify(sig, message)# True
    print('Verification passed')
except ecdsa.keys.BadSignatureError:
    print('Verification failed')