"""
CampusCart - Command-line inventory and checkout tool.

This program allows campus vendors to view product inventory, add items to cart, and check out with an automatically calculated receipt.

Author: Nahim Abdulkabir
"""
#main.py
#program scope: Handles CLI menu, inventory management.
#cart operations, and checkout logic for CampusCart.
#Inventory
inventory = {
    "100":{"name":"Backpack", "condition":"New", "price":20, "stock":37},
    "101":{"name":"Notebook", "condition":"New", "price":4, "stock":68},
    "102":{"name":"Pen", "condition":"New", "price":2, "stock":100},
    "103":{"name":"Bottled Water", "condition":"New", "price":5, "stock":157}
            }
cart = []
def display_inventory():
    for item_id in inventory:
        print("ID:", item_id, "| name:", inventory[item_id]["name"], "| Price:", inventory[item_id]["price"], "| stock:", inventory[item_id]["stock"], "| Condition:", inventory[item_id]["condition"])
# To add items to cart
def add_items():
    item_id = input("Enter item ID: ").strip()
    if not item_id in inventory:
        print("ID not found")
        return

    requested_qty = input("Enter item quantity: ").strip()
    
    if requested_qty.isdigit():
        requested_qty = int(requested_qty)
    
    else:
        print("Enter a valid number")
        return
    if requested_qty <= inventory[item_id]["stock"]:
       print("Quantity available")
    else:
        print("Requested quantity not available.", "We have", inventory[item_id]["stock"], "of this item in stock")
        
    sub_total = requested_qty * inventory[item_id]["price"]
    if requested_qty <= inventory[item_id]["stock"]:
        cart.append({"id": item_id, "qty": requested_qty, "subtotal": sub_total})       
# To view what has been added to cart    
def view_cart():
    if not cart:
        print("No items in cart")
    for item in cart:
        print("ID:", item["id"], "qty:", item["qty"], "subtotal:", item["subtotal"],"dollars")
        

# To generate recipt       
def checkout():
    if not cart:
        print("Your cart is empty. Add items before checking out")
        return
    total = 0
    discount = 0
    for amount in cart:
        total += amount["subtotal"]
        inventory[amount["id"]]["stock"] -= amount["qty"]
    if total > 20:
        discount = total * 0.10
        updated_total = total - discount
        print("You have received a discount of 10%")
        print("Deducting discount from total")
        print("Here is updated your total: ", updated_total, "dollars")
    else:
        print("Add items up to 20 dollars to recieve a discount of 10%")
    print("====== Receipt ======")
    print("---------------------------")
    for item in cart:
        print("ID:", item["id"], "| qty:", item["qty"], "| subtotal:", item["subtotal"],"| dollars")
    print("---------------------------")
    print("Discount Applied:", "$" + str(discount))
    print("---------------------------")
    print("TOTAL:", "$" + str(updated_total))
    print("===========================")
    print("Thank you for shopping with CampusCart!")
        
    
while True:
#option
    print("=== CampusCart ===")         
    print("1.View Catalogue")
    print("2. Add Items")
    print("3. View Cart")
    print("4. Checkout ")
    print("5. Exit")
#Choose an option
    choose_option =input("Choose an option: ")
    choose_option = choose_option.strip().lower()
    if choose_option.isdigit():
        choose_option = int(choose_option)
    
    if choose_option == 1 or choose_option == "view catalogue":
        display_inventory()
        
    if choose_option == 2 or choose_option == "add items":
        add_items()
    if choose_option == 3 or choose_option == "view cart":
        view_cart()
    if choose_option == 4 or choose_option == "checkout":
        checkout()
    if choose_option == 5 or choose_option == "Exit":
        print("Session ended. Goodbye!")
        break




