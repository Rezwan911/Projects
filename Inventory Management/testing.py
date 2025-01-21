import tkinter as tk
from tkinter import messagebox, simpledialog

inventory = {}

def add_item():
    name = simpledialog.askstring("Input", "Enter item name:")
    if name:
        quantity = simpledialog.askinteger("Input", f"Enter quantity for {name}:")
        price = simpledialog.askfloat("Input", f"Enter price for {name}:")
        inventory[name] = {'quantity': quantity, 'price': price}
        update_listbox()

def remove_item():
    name = listbox.get(tk.ACTIVE)
    if name in inventory:
        del inventory[name]
        update_listbox()

def update_item():
    name = listbox.get(tk.ACTIVE)
    if name in inventory:
        quantity = simpledialog.askinteger("Input", f"Enter new quantity for {name}:", initialvalue=inventory[name]['quantity'])
        price = simpledialog.askfloat("Input", f"Enter new price for {name}:", initialvalue=inventory[name]['price'])
        inventory[name] = {'quantity': quantity, 'price': price}
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for name, details in inventory.items():
        listbox.insert(tk.END, f"{name}: Quantity={details['quantity']}, Price=${details['price']:.2f}")

def save_inventory():
    with open('inventory.txt', 'w') as file:
        for name, details in inventory.items():
            file.write(f"{name},{details['quantity']},{details['price']:.2f}\n")
    messagebox.showinfo("Info", "Inventory saved successfully.")

def load_inventory():
    try:
        with open('inventory.txt', 'r') as file:
            for line in file:
                name, quantity, price = line.strip().split(',')
                inventory[name] = {'quantity': int(quantity), 'price': float(price)}
        update_listbox()
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No inventory file found. Starting with an empty inventory.")

# GUI Setup
root = tk.Tk()
root.title("Inventory Management System")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Item", command=add_item)
add_button.grid(row=0, column=0, padx=5)

remove_button = tk.Button(button_frame, text="Remove Item", command=remove_item)
remove_button.grid(row=0, column=1, padx=5)

update_button = tk.Button(button_frame, text="Update Item", command=update_item)
update_button.grid(row=0, column=2, padx=5)

save_button = tk.Button(button_frame, text="Save Inventory", command=save_inventory)
save_button.grid(row=0, column=3, padx=5)

load_inventory()  # Load existing inventory when the program starts

root.mainloop()
