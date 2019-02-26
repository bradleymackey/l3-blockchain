import blockcypher

API_KEY = "fa36f8ddaf1446ec848398cae2010218"

# addr = blockcypher.generate_new_address(coin_symbol='btc-testnet', api_key=API_KEY)

private = "29dc9b6dde43139a38fe64733a1666d0b99cc2bb6b711e7faeb0ec6dbc530cf8"
public = "02157f9bc3d150dd52249000d3f1ec1f7e2995cee93b1a4ae58e01a125c59dd41a"
address = "mjLjznCbyKuGJ5xuz7Wo1Es3qXHoxoDXgo"

# examine our address on the testnet blockchain
details = blockcypher.get_address_details(address, coin_symbol='btc-testnet')
print(details)
sat_bal = blockcypher.get_total_balance(address, coin_symbol='btc-testnet')
btc_bal = blockcypher.from_satoshis(sat_bal, 'btc')
print(f"{address} has balance: {btc_bal}")


# sending 100 satoshi to mpamtqLA66JFVSQNDaPHZ5xMiCz6T2MeNn, from our address
# inputs = [{'address': 'mjLjznCbyKuGJ5xuz7Wo1Es3qXHoxoDXgo'}]
# outputs = [{'address': 'mpamtqLA66JFVSQNDaPHZ5xMiCz6T2MeNn', 'value': 100}]
# unsigned_tx = blockcypher.create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol='btc-testnet', api_key=API_KEY)
# private_keys=[private]
# public_keys=[public]
# # sign transactions
# tx_signatures = blockcypher.make_tx_signatures(txs_to_sign=unsigned_tx['tosign'], privkey_list=private_keys, pubkey_list=public_keys)
# # send transactions to the network
# blockcypher.broadcast_signed_transaction(unsigned_tx=unsigned_tx, signatures=tx_signatures, pubkeys=public_keys, coin_symbol='btc-testnet', api_key=API_KEY)

# writing `wbbz74` into the blockchain!
# the script we pass to the transaction should be hex encoded of a suitable script in order to create a proof-of-burn transaction with student ID in it
ID_ASCII = "wbbz74".encode('ascii').hex()
OP_RETURN = "6a" # return, so we create a NULL transaction
OP_PUSHDATA1 = "06" # the number of bytes we will push to the stack
script = OP_RETURN + OP_PUSHDATA1 + ID_ASCII # hex encoded transaction
print("script hex:",script)

inputs = [{'address': 'mjLjznCbyKuGJ5xuz7Wo1Es3qXHoxoDXgo'}]
outputs = [{'value' : 0, 'script_type':"null-data", 'script':script}]
unsigned_tx = blockcypher.create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol='btc-testnet', api_key=API_KEY)
private_keys=[private]
public_keys=[public]
# sign transactions
tx_signatures = blockcypher.make_tx_signatures(txs_to_sign=unsigned_tx['tosign'], privkey_list=private_keys, pubkey_list=public_keys)
# send transactions to the network
blockcypher.broadcast_signed_transaction(unsigned_tx=unsigned_tx, signatures=tx_signatures, pubkeys=public_keys, coin_symbol='btc-testnet', api_key=API_KEY)
