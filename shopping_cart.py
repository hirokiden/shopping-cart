# shopping_cart.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output


####ENVIRONMENT SETUP####


'''
# Make sure to install the following to set up the terminal and script

conda create -n shopping-env python=3.7 # (first time only)

conda activate shopping-env

pip install pytest

PYTHON comamand --> 

python shopping_cart.py'''


####NOW THE SCRIPT FOLLOWS BELOW:

# SECTION INPUT


from datetime import datetime #Taken from stackoverflow

total_price = 0
selected_ids = []

while True:
    selected_id = input("Please input a product identifier, if you're finished enter 'DONE':" ) # the data input will always be a str
#     if selected_id != "DONE": #works initially but breaks with subsequent non-"DONE" input entries
#         selected_id = input("Please enter a valid product identifier, if you're finished enter 'DONE':" )
    if selected_id == "DONE":
        break
#     if int(selected_id) > 20 or int(selected_id) <1:
#         selected_id = input("Please enter a valid product identifier, if you're finished enter 'DONE':" )
    if int(selected_id) >0 or int(selected_id) <21:
        selected_ids.append(selected_id) # remember, this will be in string format
        # print(selected_ids) --> designed to check that "id"s are being picked up via selected_ids list
    else:
        selected_id = input("Please enter a valid product identifier, if you're finished enter 'DONE':" )
    
# CART CONTENTS WITH ASSOCIATED PRICE
        
print("-------------------------------------------------------------------------------------------------------------------------")        
print("GREEN FOODS GROCERY")
print("WWW.GREEN-FOODS-GROCERY.COM")
print("-------------------------------------------------------------------------------------------------------------------------") 

# WEB, PHONE, ACTUAL TODAY'S DATE AND TIME

print("CHECKOUT AT:", datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # This section is derived from stackoverflow date function
print("-------------------------------------------------------------------------------------------------------------------------")
print("SELECTED PRODUCTS:")

for selected_id in selected_ids: # basic tutorials derived from Prof. Rossetti's youtube video
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)] 
        # each item for each item in products list is matched via "id" with input(ed) selected_id
        # in order for the match to happen ensure that both values p["id"] and selected_id are converted to str
    matching_product = matching_products[0]
        # Taking the first item in the matching_products list which is [0]
    total_price = total_price + matching_product["price"]
        # Ensuring that each total price value is added to prior matching price
        # Must be part of loop to keep this continuous
        # print(matching_product)
    product_name = str(matching_product["name"])
    product_price = matching_product["price"]
    print(product_name + " " + "$(" + str("{0:.2f}".format(product_price)) + ")" )
        # Make sure to pring the display component with product name and associated price



# SUBTOTAL, SALES TAX, GRAND TOTAL

print("-------------------------------------------------------------------------------------------------------------------------")
print("SUBTOTAL: $","{0:.2f}".format(total_price))
ny_sales_tax = 0.0876 #8.875% is the NYC combined rate
tax = "{0:.2f}".format(total_price * ny_sales_tax) #Make sure to format with digits to avoid additional decimals
print("NYC TAX $:", tax)
grand_total = "{0:.2f}".format(total_price + (total_price * ny_sales_tax))
print("TOTAL $:", grand_total)

# "{0:.2f}".format(i["price"])

print("-------------------------------------------------------------------------------------------------------------------------")
print("THANK YOU FOR SHOPPING WITH US, PLEASE COME AGAIN!")
print("-------------------------------------------------------------------------------------------------------------------------")

# MESSAGE WITH CUSTOMER EMAIL SO THAT RECEIPT IS EMAILED BACK TO CUSTOMER