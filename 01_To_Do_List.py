import time

def show_menu():
    print("Select option:")
    print("[1] Display To Do List")
    print("[2] Add Item to List")
    print("[3] Remove Item from List")
    print("[4] Exit")

to_do = [] #start with a blank list
keep_going = True

while keep_going == True:
    show_menu()
    time.sleep(1)
    option = input("Select Option")
    
    if option == "4":
        keep_going = False
    
    if option == "1":
        print(to_do)
        time.sleep(2)

    if option == "2":
        print("Adding to list")
        item = input("Insert item to add to To Do List:")
        to_do.append(item)
        
        print(*to_do, sep="\n")
        time.sleep(2)

    if option == "3":
        print("Removing from list")
