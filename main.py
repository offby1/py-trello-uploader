# 3rd-party
from trello import TrelloClient

# Local
from auth import py_trello_auth_dict

client = TrelloClient(
    **py_trello_auth_dict
)

board = client.get_board ('hPK2DcxK')
print("About to munge {!r}".format(board.name))

input_data = [{'name': 'Some Test Book', 'desc': '''
This is _such_ a great book!  Here's a quote from it:
> Twas brillig, yo
> The slithey toves
> Were all like up in your shit
'''}]

lists = board.get_lists(None)
if len(lists) != 1:
    raise Exception("{!r} has {} entries, but I only know how to deal with a single entry".format(lists, len(lists)) )

l = lists[0]
print("List: {!r}".format(l))

for book in input_data:
    l.add_card(**book)
