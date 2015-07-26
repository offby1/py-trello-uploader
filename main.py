# 3rd-party
from trello import TrelloClient

# Local
from auth import py_trello_auth_dict

client = TrelloClient(
    **py_trello_auth_dict
)

print(client.list_boards())
