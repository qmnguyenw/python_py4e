Create simple Blockchain using Python



 **A blockchain** is a time-stamped decentralized series of fixed records that
contains data of any size is controlled by a large network of computers which
are scattered around the globe and not owned by a single organization. Every
block is secured and connected with each other using hashing technology which
protects it from being tempered by an unauthorized person.

**Creating Blockchain using Python, mining new block, and display the whole
blockchain:**

  * The data will be stored in JSON format which is very easy to implement and easy to read. The data is stored in a block and the block contains multiple data. Each and every minute multiple block are added and to differentiate one from other we will use fingerprinting.
  * The fingerprinting is done by using hash and to be particular we will use the SHA256 hashing algorithm. Every block will contain its own hash and also the hash of the previous function so that it cannot get tampered.
  * This fingerprinting will be used to chain the blocks together. Every block will be attached to the previous block having its hash and to the next block by giving its hash.
  * The mining of the new block is done by giving the successfully finding the answer to the proof of work. To make mining hard the proof of work must be hard enough to get exploited.
  * After mining the block successfully the block will then be added to the chain.
  * After mining several blocks the validity of the chain must be checked in order to prevent any kind of tampering with the blockchain.
  * Then the web app will be made by using **Flask** and deployed locally or publicly as per the need of the user.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python programm to create Blockchain

 

# For timestamp

import datetime

 

# Calculating the hash

# in order to add digital

# fingerprints to the blocks

import hashlib

 

# To store data

# in our blockchain

import json

 

# Flask is for creating the web

# app and jsonify is for

# displaying the blockchain

from flask import Flask, jsonify

 

 

class Blockchain:

 

 # This function is created

 # to create the very first

 # block and set it's hash to "0"

 def __init__(self):

 self.chain = []

 self.create_block(proof=1, previous_hash='0')

 

 # This function is created

 # to add further blocks

 # into the chain

 def create_block(self, proof, previous_hash):

 block = {'index': len(self.chain) + 1,

 'timestamp': str(datetime.datetime.now()),

 'proof': proof,

 'previous_hash': previous_hash}

 self.chain.append(block)

 return block

 

 # This function is created

 # to display the previous block

 def print_previous_block(self):

 return self.chain[-1]

 

 # This is the function for proof of work

 # and used to successfully mine the block

 def proof_of_work(self, previous_proof):

 new_proof = 1

 check_proof = False

 

 while check_proof is False:

 hash_operation = hashlib.sha256(

 str(new_proof**2 -
previous_proof**2).encode()).hexdigest()

 if hash_operation[:4] == '00000':

 check_proof = True

 else:

 new_proof += 1

 

 return new_proof

 

 def hash(self, block):

 encoded_block = json.dumps(block, sort_keys=True).encode()

 return hashlib.sha256(encoded_block).hexdigest()

 

 def chain_valid(self, chain):

 previous_block = chain[0]

 block_index = 1

 

 while block_index < len(chain):

 block = chain[block_index]

 if block['previous_hash'] != self.hash(previous_block):

 return False

 

 previous_proof = previous_block['proof']

 proof = block['proof']

 hash_operation = hashlib.sha256(

 str(proof**2 -
previous_proof**2).encode()).hexdigest()

 

 if hash_operation[:4] != '00000':

 return False

 previous_block = block

 block_index += 1

 

 return True

 

 

# Creating the Web

# App using flask

app = Flask(__name__)

 

# Create the object

# of the class blockchain

blockchain = Blockchain()

 

# Mining a new block

@app.route('/mine_block', methods=['GET'])

def mine_block():

 previous_block = blockchain.print_previous_block()

 previous_proof = previous_block['proof']

 proof = blockchain.proof_of_work(previous_proof)

 previous_hash = blockchain.hash(previous_block)

 block = blockchain.create_block(proof, previous_hash)

 

 response = {'message': 'A block is MINED',

 'index': block['index'],

 'timestamp': block['timestamp'],

 'proof': block['proof'],

 'previous_hash': block['previous_hash']}

 

 return jsonify(response), 200

 

# Display blockchain in json format

@app.route('/get_chain', methods=['GET'])

def display_chain():

 response = {'chain': blockchain.chain,

 'length': len(blockchain.chain)}

 return jsonify(response), 200

 

# Check validity of blockchain

@app.route('/valid', methods=['GET'])

def valid():

 valid = blockchain.chain_valid(blockchain.chain)

 

 if valid:

 response = {'message': 'The Blockchain is valid.'}

 else:

 response = {'message': 'The Blockchain is not valid.'}

 return jsonify(response), 200

 

 

# Run the flask server locally

app.run(host='127.0.0.1', port=5000)  
  
---  
  
 __

 __

 **Output (mine_block):**

    
    
    {
    "index":2,
    "message":"A block is MINED",
    "previous_hash":"2d83a826f87415edb31b7e12b35949b9dbf702aee7e383cbab119456847b957c",
    "proof":533,
    "timestamp":"2020-06-01 22:47:59.309000"
    }
    
    
    

**Output (get_chain):**

  

  

    
    
    {
    "chain":[{"index":1,
    "previous_hash":"0",
    "proof":1,
    "timestamp":"2020-06-01 22:47:05.915000"},{"index":2,
    "previous_hash":"2d83a826f87415edb31b7e12b35949b9dbf702aee7e383cbab119456847b957c",
    "proof":533,
    "timestamp":"2020-06-01 22:47:59.309000"}],
    "length":2
    }
    

**Output(valid):**

    
    
    {"message":"The Blockchain is valid."}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

