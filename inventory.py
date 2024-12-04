
# A program that reads from a text file and performs as instructed on the
# Provided data, to prepare for presentation to managers.

class Shoe:
    # A function that initiates some attributes.
    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Function to return the cost of the shoe.
    def get_cost(self):

        return self.cost

    # Function to return the quantity of the shoes.
    def get_quantity(self):
       
        return self.quantity

    # Function to return a string representation of a class.
    def __str__(self):
       
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

# A list to store a list of objects of shoes.

shoe_list = []

# Functions outside the class

# A function that will open and read the data from a txt file, then creates 
# A shoes object with this data and append this object into the shoes list.
def read_shoes_data():
    
    try:
        with open("inventory.txt", "r") as file:
            data = file.read()
    except:
        print("There was an error")
        return

    for line in data.split("\n")[1:]:
        info = line.split(",")

        country = info[0]
        code = info[1]
        product = info[2]
        cost = int(info[3])
        quantity = int(info[4])

        shoe_list.append(Shoe(country, code, product, cost, quantity))

    return None

# A function that allows a user to capture data about a shoe and use this
# Data to create a shoe object and append this object inside the shoe list.
def capture_shoes():
    
    data = input("Enter shoe data (country,code,product,cost,quantity):")
    info = data.split(",")

    country = info[0]
    code = info[1]
    product = info[2]
    cost = int(info[3])
    quantity = int(info[4])

    shoe_list.append(Shoe(country, code, product, cost, quantity))

    with open("inventory.txt", "a") as file:
        file.write("\n" + str(shoe_list[-1]))

# A function that iterates over the shoes list and print the details of the 
# Shoes returned from the __str__ function.
def view_all():

    for shoe in shoe_list:
        print(shoe)


def re_stock():

    # Find lowest shoe quantity 
    min_value = 10000000
    min_shoe = None

    for shoe in shoe_list:
        if shoe.quantity < min_value:
            min_value = shoe.quantity 
            min_shoe = shoe

    print()
    print("Min value", min_shoe)

    # Ask user for refill quantity
    restock_value = int(input(f"How much of the {min_shoe.product}-{min_shoe.code} do you want to restocked? "))

    min_shoe.quantity += restock_value

    data = "Country,Code,Product,Cost,Quantity"

    for shoe in shoe_list:
        data = data + "\n" + str(shoe)

    # Update shoe quantity to file
    with open("inventory.txt", "w") as file:
        file.write(data)

# A function that searches for a shoe from the list using the shoe code 
# And returns this object and prints it.
def search_shoe():

    code = input("Code:")

    for shoe in shoe_list:
        if shoe.code == code:
            return shoe

# A function that calculates the total value for each item.
def value_per_item():
    
    for shoe in shoe_list:
        print(f"{shoe.code} - {shoe.cost * shoe.quantity}")

# A function to determine the product with the highest quantity and print 
# The shoe as being for sale.
def highest_qty():
    
    max_value = -1
    max_shoe = None

    for shoe in shoe_list:
        if shoe.quantity > max_value:
            max_value = shoe.quantity
            max_shoe = shoe

    print(f"The {max_shoe.product} is on sale for only - R{max_shoe.cost}")


# Main Menu

while True:

    print("==========================")
    print("Menu Options")
    print("R - Read File Data")
    print("A - Add new shoes")
    print("V - View All")
    print("S - Re-stock")
    print("SS - Search Shoe")
    print("VA - Value Per Item")
    print("H - Highest Quantity")
    print("E - Exit")
    print("==========================")

    user_input = input("Choose an option: ").upper()
    
    if user_input == "R":
        read_shoes_data()
    if user_input == "A":
        capture_shoes()
    if user_input == "V":
        view_all()
    if user_input == "S":
        re_stock()
    if user_input == "SS":
        print(search_shoe())
    if user_input == "VA":
        value_per_item()
    if user_input == "H":
        highest_qty()
    if user_input == "E":
        print("You have chosen to exit.")
        break