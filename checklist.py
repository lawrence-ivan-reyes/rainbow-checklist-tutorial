checklist = []

rainbow_colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def create(item):
    # splitting input into 2 words & check the first word for colour
    colour = item.split()[0].lower() # extracting first word as colour & accounting for upper/lowercase inputs to all revert to lower 

    # checking if inputted colour is valid
    if colour in rainbow_colours:
        # check if an item with the same colour already exists
        for existing_item in checklist:
            if existing_item.lower().startswith(colour): # check if item starts with same colour
                print(f"You can't wear more than one {colour} item!")
                return # exiting function if colour is already used
        
        # if item is unique and valid, append to checklist
        checklist.append(item)
    else:
        print("\nPlease choosen a valid rainbow colour. Remember, the colours of the rainbow are: \nred, orange, yellow, green, blue, indigo, & violet!")

def read(index):
    return checklist[int(index) -1] # -1 because i want the list to start at 1 instead of 0

def update(index, item):
    colour = item.split()[0] # extracting first word as colour (like in line 7)
    if colour in rainbow_colours and item not in checklist:
        checklist[int(index)] = item
    else:
        print("You can't wear the same item twice, or it's not a valid rainbow colour!")

def destroy(index):
    checklist.pop(int(index))

def list_items():
    index = 1
    for list_items in checklist:
        print("{}: {}".format(index, list_items))
        index += 1

def mark_completed(index):
    checklist[int(index) - 1] = "√" + checklist[int(index) -1]

def select(function_code):
    if function_code.upper() == "C":
        input_item = user_input("Input item (e.g., 'yellow jacket'): ")
        create(input_item)

        if len(checklist) == 7: # checking if all colours are filled
            print("All items are now asssigned a unique colour from the rainbow!")

    elif function_code.upper() == "R":
        item_index = user_input("Index Number? ")
        print(read(item_index))
    
    elif function_code.upper() == "P":
        list_items()
    
    elif function_code.upper() == "M":
        print("Here is your current checklist: \n")
        list_items() # display current list so that user can see which one they want to mark as complete
        item_index = user_input("\nWhich index number do you want to mark as complete? ")
        mark_completed(item_index)
    
    elif function_code.upper() == "Q":
        return False

    else:
        print("Invalid Option")
    
    return True

def user_input(prompt):
    return input(prompt)

running = True
while running:
    print("\nWelcome to Captain Rainbow's Colour Checklist!")
    selection = user_input("\nPress C to add to list, R to read froom list, P to display list, M to mark as complete, or Q to quit: ")
    running = select(selection)