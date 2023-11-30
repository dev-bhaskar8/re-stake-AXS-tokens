from web3 import Web3
from web3.auto import w3 as w
import os
from dotenv import load_dotenv

load_dotenv()

my_ronin_address = os.getenv("PUBLIC_KEY")

private_key = os.getenv("PRIVATE_KEY")
private_key = bytearray.fromhex(private_key.replace("0x", ""))

staking_address = "0x05b0bb3c1c320b280501b86706c3551995bc8571"
staking_address = w.toChecksumAddress(staking_address)

w3 = Web3(Web3.HTTPProvider('https://proxy.roninchain.com/free-gas-rpc'))

signed_txn = w3.eth.account.sign_transaction(
  {
    'value': Web3.toWei('0', 'gwei'),
    'chainId': 2020,
    'gas': 300000,
    'gasPrice': Web3.toWei('0', 'gwei'),
    'nonce': w3.eth.get_transaction_count(w.toChecksumAddress(my_ronin_address)),
    'to': staking_address,
    'data': '0x3d8527ba'
    },
  private_key=private_key)

w3.eth.send_raw_transaction(signed_txn.rawTransaction)

txn = w3.toHex(w3.keccak(signed_txn.rawTransaction))
print(txn)