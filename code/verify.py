import ecdsa

# put the hex of your public key in the line below
vk_string="14afbb92502c9294f19be099ac3fe51f8ea1c943e36a06c43b096864d887145b55e87f1a01b1b9275bcc9d528a2829a774ec6de06dfaed72933ced851105f3ba"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string),ecdsa.SECP256k1)

message = b'Hello World'

# put your signature for Hello World in the line below
sig_hex = "acd855318df6ebb70e4c956caad1c7df1a3395c2ead557e6ec304ced9038037aa83e79ab1bb80ca3b912ea2806c67cc387301f1530e730834bb3213cf55b70d6"
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