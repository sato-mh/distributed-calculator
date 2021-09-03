import os

DIVIDER_ADDRESS = os.environ.get('DIVIDER_ADDRESS', '0.0.0.0:5050')
IP_ADDRESS = DIVIDER_ADDRESS.split(':')[0]
PORT = int(DIVIDER_ADDRESS.split(':')[1])
