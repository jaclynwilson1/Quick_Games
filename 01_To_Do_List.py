import time

#To Do: sort by priority, date created, due date. Make as dictionary or other format. Use a pickle module to save
#and load taasks to the file
# CLI using argparse library

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
        print("You are now exiting your to do list.")
        keep_going = False
    
    if option == "1":
        print("\n")
        print(*to_do, sep="\n")
        time.sleep(2)

    if option == "2":
        print("Adding to list")
        item = input("Insert item to add to To Do List:")
        to_do.append(item)
        
        print("Your list:\n")
        print(*to_do, sep="\n")
        time.sleep(2)

    if option == "3":
        print("Removing from list. \n Here is your current todo list:")
        print(*to_do, sep="\n")
        item = input("Enter item you want to remove from list.")
        to_do.remove(item)
        print("Your list now looks like this:\n")
        print(*to_do, sep="\n")
        time.sleep(2)
