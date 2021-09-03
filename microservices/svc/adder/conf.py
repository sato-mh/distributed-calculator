import os

ADDER_ADDRESS = os.environ.get('ADDER_ADDRESS', '0.0.0.0:5050')
IP_ADDRESS = ADDER_ADDRESS.split(':')[0]
PORT = int(ADDER_ADDRESS.split(':')[1])
