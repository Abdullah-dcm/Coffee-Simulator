# ☕️ Coffee Order Simulator - Session 3: Data Types and Operators ☕️
# Welcome to Code Café! Let's take your order using Python.
# This session is all about how we can talk to Python (input) and how it talks back (output).


# Print a welcome message

print("Welcome to Code Café \n")
print("Lets get started with your order!\n")

# Ask for the customer's name

customer_name=input("Enter your name? 👤: ")

print("--------------------------------------------")

# Ask for cup size

print("\nWhat cup size would you like to take? 📏")
print("Options: Small, Medium, Large")
cup_size = input("Your choice: ")

print("--------------------------------------------")

# Ask for coffee type

print("\nWhat type of coffee would you like? ☕️")
print("Options: Mocha,Cappuccino, Latte, Espresso")
coffee_type = input("Your choice: ")

print("--------------------------------------------")

# Ask for extra toppings

print("\n Would you like to add any toppings? 🍫🍦")
print("Options: None, Whipped Cream, Chocolate Syrup, Caramel Drizzle")
toppings = input("Your choice:  ")

print("--------------------------------------------")

# Ask for takeaway or dine-in

print("\n Is this order for takeaway or dine-in? 🏃‍♂️🍽️")
order_type = input("Your choice: ")

print("--------------------------------------------")

# Print a cute little receipt

print("\n\n Printing your coffee receipt...\n")
print("~" * 40)  # Decorative line

# Use sep and end for formatting fun

print("Customer:", customer_name, end=" ☕️\n")
print("Cup Size:", cup_size, sep=" ", end=" 📏\n")
print("Coffee Type:", coffee_type, end=" 🍵\n")
print("\nToppings:", toppings, sep=" ", end=" 🍬\n")
print("\nOrder Type:", order_type, end=" 🛍️\n")

print("--------------------------------------------")

print("Thank you for ordering from Code Café! 🌈💻")
print("Your coffee will be ready shortly. Enjoy! 🎉\n")

# 💡 Notes for learners:
# - input() lets Python take information from the user.
# - print() displays information back to the user.
# - You can decorate your output using escape characters like \n (new line) and special parameters like end= and sep=
# - datetime module helps you work with real-world time and date
