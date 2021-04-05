#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  look [description]
''')

class Player():
    """Class for the player for re-usability """
    def __init__(self):
        self.inventory = []
        self.health = 50
        self.attack = 5

class Enemy(Player):
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
   # if "item" in rooms[currentRoom]:
    #    print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'name': 'Hall',
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Office',
        'item': 'key',
        'description': 'Dimly lit hall with wooden floors and old Knight armor.\n '
                'There is a kitchen to the South, a Dining room to the East, and Office to the West'
    },
    'Office': {
        'name': 'Office',
        'east': 'Hall',
        'item': 'shotgun',
        'description': 'This Office appears to have not been used in some time.\n '
                       'There are cobwebs all around and papers scattered on the floor.  '
    },

    'Kitchen': {
        'name': 'Kitchen',
        'north': 'Hall',
        'south': 'Basement',
        'enemy': 'monster',
        'description': 'A kitchen that looks like something has been freshly killed and possibly prepared for a meal.'
                       '\n North is the Hall'
    },
    'Dining Room': {
        'name': 'Dining Room',
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion',
        'north': 'Pantry',
        'description': ' A large table sits in the center of the room. leafless trees can be seen from the'
                       'windows\n To the West is the Hall, the Garden to the South and a pantry to the North.'
    },
    'Basement': {
        'north': 'Kitchen',
        'item': 'Large Ruby',
        'trigger': 'something',
        'description': 'A dark and damp basement you are unable to see and there is a odd moaning sound. \n '
                       'South is the kitchen',
        'description_lights': 'A damp basement with old boxes for storage'
    },
    'Garden': {
        'north': 'Dining Room',
        'text': 'A'
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': 'cookie',
    }
}
"""dictionary for weapons"""
weapons = {
    'Sword': {'damage': '10'},
    'Shotgun': {'damage': '30'}


}
"""dictionary for enemies """
enemy = {
    'Monster': {'name': 'monster', 'health': '50', 'attack': '20'},
    'Zombie': {'name': 'zombie', 'health': '15', 'attack': '10'}
}

def combat():
    global enemy,weapon, Player
    e_health = enemy['name']['health']




# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type 'look' first
    if move[0] == 'look':
        print(rooms[currentRoom]['description'])
        if "item" in rooms[currentRoom]:
            print('You see a ' + rooms[currentRoom]['item'])

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    ## If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
