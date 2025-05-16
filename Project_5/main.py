# Cafe Management System

# Cafe Menu
menu = {
    "Margherita Pizza": 199,
    "Veg Biryani": 180,
    "Paneer Butter Masala": 220,
    "Masala Dosa": 100,
    "Chicken Curry": 250,
    "Fried Rice": 150,
    "Coffee": 120,
    "Tea": 90,
    "Vanilla Icecream": 50,
    "Gulab Jamun (2 pcs)": 60
}

print("\nWelcome to Tarbucks Cafe...")

# Printing Cafe Menu (line by line)
for key, values in menu.items():
    print(f"{key} : ₹{values}")


# First Order function
def first_order():
    order_total = 0
        
    f_Order = input("\nEnter the item you want to order from the menu: ").title()

    if f_Order in menu:
        f_Quantity = int(input("How many items do you want to order? "))
        order_total = order_total + menu[f_Order] * f_Quantity
        
        print(f"\nYour item {f_Order} has been added in your order.\n")
    
    else:
        print("Sorry, but you will definitely get this item next time!")
            
    
    return order_total


# Another order function (If they want something else)
def another_order(total):

    while True:
        s_Order = input("Do you want to order something else? (Yes/No): ").title()

        if s_Order == "No":
            print(f"\nHere is your final bill: ₹{total}")
            break

        if s_Order == "Yes":
            s_Order = input("\nEnter the item you want to order from the menu: ").title()

            if s_Order in menu:
                s_Quantity = int(input("How many items do you want to order? "))
                total = total + menu[s_Order] * s_Quantity
                
                print(f"Your item {s_Order} has been added in your order.")
                
            elif s_Order not in menu:
                print("\nThis item is not in our menu!")


another_order(first_order())