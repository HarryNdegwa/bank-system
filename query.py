from crud import Session

from models import Client

s=Session()

client=s.query(Client).get(1)

print(client)

# clients=s.query(Client).count()

# print(clients)

import sys

print(sys.path)
