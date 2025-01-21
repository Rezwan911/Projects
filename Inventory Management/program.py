import os

def save_inventory(inventory, filename):  #This is used to save data in the inventory after the program has ended.
    with open(filename, 'w') as file:
        for name, details in inventory.items():
            file.write("{},{},{:.2f}\n".format(name, details['quantity'], details['price']))

def load_inventory(filename):  #This is used to load up the inventory.
    inventory = {}
    if file_exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        name = parts[0]
                        quantity = int(parts[1])
                        price = float(parts[2])
                        inventory[name] = {'quantity': quantity, 'price': price}
    return inventory

def file_exists(filename):  #This checks if their is a file that we are looking for. 
    return os.path.isfile(filename)

def display_inventory(inventory): #This is used to display data from a specific file.
    if not inventory:
        print("Inventory is empty.")
    else:
        for name, details in inventory.items():
            if details['quantity'] <= 10:
                print(f"{name}: {details['quantity']} units @ ${details['price']:.2f} (Low Stock)")
            else:
                print(f"{name}: {details['quantity']} units @ ${details['price']:.2f}")


filename = 'inventory.txt'
inventory = load_inventory(filename)
while True: # Everything occurs inside this.
    print("="* 48)
    print("               Inventory Manager             ")
    print("="* 48)
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item")
    print("4. View Inventory")
    print("5. Save and Exit")
         
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Item Name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
        inventory[name] = {"quantity": quantity, "price": price}
        print(name, "has been added to the list. ")
        
    elif choice == '2':
        name = input("Item Name to Remove: ")
        if name in inventory:
              del inventory[name]
        else:
            print("Item not found.")
        
    elif choice == '3':
            name = input("Item Name to Update: ")
            if name in inventory:
                quantity = input("New Quantity (leave blank if no change): ")
                price = input("New Price (leave blank if no change): ")
                if quantity:
                    inventory[name]['quantity'] = int(quantity)
                if price:
                    inventory[name]['price'] = float(price)
                print("Now there's ", quantity, "", name, "at the price of", price, "$")
            else:
                print("Item not found.")
        
    elif choice == '4':
        print("Current Inventory:")
        display_inventory(inventory)
        
    elif choice == '5':
        x = input("Are you sure you want to exit? y/n")
        if x == 'y':
            save_inventory(inventory, filename)
            print("Inventory saved. Byeee...")
            break
        else:
            continue

    else:
         print("Invalid option. Please try again.")
  
