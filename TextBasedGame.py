# Alfonso Sanchez Gallegos


# A function to display the main menu and the commands
def show_instructions():
   print("Super Mario Text Adventure Game")
   print("Collect 6 items to win the game and save Princess Peach, or be defeated by Bowser!")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")
   print("-" * 30)


# A function that shows the player's status
def show_status(current_room, inventory, rooms):
    # Print the player's current room
    print('You are in the {}'.format(current_room))

    # Print the current inventory
    print('Inventory:', inventory)

    # Print an item in the room if there is one
    if rooms[current_room].get('item') is None:
        pass
    else:
        print('You see a', rooms[current_room]['item'])


# A function that changes current room or gets item in room
def command(user_input, current_room, inventory, rooms):
    for word in range(len(user_input)):

        # Checks if proper command is in the input
        if user_input[word] == 'go':
            for key in rooms[current_room].keys():
                if user_input[word + 1] == key:
                    current_room = rooms[current_room][key]
                    print('-' * 30)
                    return current_room, inventory

            # Prints invalid direction
            print('You cannot go that way!')
            print('-' * 30)
            return current_room, inventory

        # Grabs item in room
        elif user_input[word] == 'get':
            for value in rooms[current_room].values():
                if user_input[word + 1] == value:
                    print('{} retrieved!'.format(value))
                    inventory.append(value)
                    del rooms[current_room]['item']
                    return current_room, inventory

            # Prints invalid action
            print('Cannot {}'.format(' '.join(user_input)))
            print('-' * 30)
            return current_room, inventory

        # Prints invalid command
        else:
            print('Invalid move!')
            print('-' * 30)
            return current_room, inventory


def main():
    # Initial inventory where items will be kept
    inventory = []

    # A dictionary for the Super Mario Adventure text game
    # The dictionary links a room to other rooms.
    rooms = {
        'Ground': {'South': 'Forest', 'North': 'Underwater', 'East': 'Desert', 'West': 'Underground'},
        'Forest': {'North': 'Ground', 'East': 'Ghost House', 'item': 'Mushroom'},
        'Ghost House': {'West': 'Forest', 'item': 'Key'},
        'Underground': {'East': 'Ground', 'item': 'Cappy'},
        'Underwater': {'South': 'Ground', 'East': 'Snow', 'item': 'Gloves'},
        'Snow': {'West': 'Underwater', 'item': 'Shoes'},
        'Desert': {'West': 'Ground', 'North': 'Castle', 'item': 'Yoshi'},
        'Castle': {'South': 'Desert', 'item': 'Bowser'}  # villain
    }

    # Starts the player in the Ground
    current_room = 'Ground'

    # Shows the player the game instructions
    show_instructions()

    # Loop forever until the end of the game
    while True:

        show_status(current_room, inventory, rooms)

        # Conditional to exit while loop if item in room is Bowser and items in inventory != 6
        if current_room == 'Castle' and len(inventory) != 6:
            print('You have lost to Bowser!...GAME OVER!')
            print('Thanks for playing the game. Hope you enjoyed it.')
            return False
        # Conditional to exit while loop if player collects all items
        elif current_room == 'Castle' and len(inventory) == 6:
            print('Congratulations! You have collected all the items, defeated Bowser, and saved Princess Peach!')
            print('Thanks for playing the game. Hope you enjoyed it.')
            return False

        # get the player's next 'move'
        print('Enter your move:')
        user_input = input().split()

        current_room, inventory = command(user_input, current_room, inventory, rooms)


if __name__ == '__main__':
    main()