inventory = []

def open_file():
    files=open("inventory",'r')
    inventory=files.readlines()
    files.close()
open_file()
        
def save_file():
    files = open("inventory",'w')
    files.write(str(inventory))
    files.close()

def total_value():
    total = 0
    for item in inventory:
        if item[1] <= 0:
            print(item[0] , "is out of stock.")
        else:
            total += item[2] + item[2] 
    return total

def update_stock():
    name = input("Enter the item name to update: ")
    found = False
    for item in inventory:
        if item[0] == name:
            found = True
            quantity = input("Enter new quantity (leave blank if no change): ")
            if quantity.isdigit():  # Check if input is a number
                item[1] = int(quantity)
                print(f"Updated {name} quantity to {item[1]}.")
            else:
                print("Quantity not changed.")
            break
    if not found:
        print("Item not found.")

def add_items():
    item=input("Enter the item's name: ")
    quantity=int(input("Enter the quantity(of the item you just put name in): "))
    price=float(input("Enter the cost of the item: "))
    x = [item,quantity,price]
    inventory.append(x)

def view_inventory():
    print(inventory)


print("\t\t==========Inventory Management=========")

while 1:
    print("1. Add items.")
    print("2. View Inventory")
    print("3. View the total value of stock.")
    print("4. Update stock")
    print("5. Search for an item.")
    print("6. View the item with the highest stock value.")
    print("7. Save and exit.")
    choice = input("Enter which funtion to run:")

    if choice=='1':#This adds new items to the stock
        add_items()

    elif choice=='2':#This lets us see our inventory
        view_inventory()

    elif choice=='3':#This calculates the value of items that are stored in the stock
        print(total_value())

    elif choice=='4':#Using this you can update the stock 
        name = input("Item Name to Update: ")
        if name in inventory:
            quantity = input("New Quantity (leave blank if no change): ")
            if inventory[1]:
                inventory[name][1] = int(quantity)
            print("Now there's ", quantity, name, ".")
        else:
            print("Item not found.")

    elif choice=='5':#this shows if a certain item is available in the stock
        name = input("Enter the name you want to search: ")
        for i in range(len(inventory)):
            if name in inventory[i][0]:
                print("Item found")
            else:
                print("Item not found")

    elif choice=='6':
        max = 0
        for i in range(len(inventory)):   
                    if inventory[i][2] > max:
                        inventory[i][2] = max
        print(inventory[i][0], max)

    elif choice=='7':
        print("Saving....")#This saves the file in a test file so that we can access it anytime we need
        save_file()
        break

    else :
        print("Invalid choice. Try again.....")
