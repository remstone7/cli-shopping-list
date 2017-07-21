# make a list that will hold onto our items
shopping_list = []
# print out instructions
print("What should we pick up at the store?")

def show_help():
    print("Enter 'DONE' to stop adding items.")
    print("SHOW to show a list")
    print("HELP for help")

def show_list():
    # print out  the list
    print("Here is your list:")
    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("added {}.  list now has {} items.".format(new_item, len(shopping_list)))

show_help()
while True:
    # ask for new items
    new_item = input("> ")
    if new_item == "" or new_item == " ":
        print('try again you didnt enter anything')
        continue
    # quit app
    if new_item.upper() == 'DONE':
        break;
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)


show_list()
