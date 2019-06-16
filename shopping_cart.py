# Instructions on running this script, go to ----> LINE 40

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

pip install sendgrid==6.0.5

conda activate shopping-env

pip install pytest

PYTHON command --> 

python shopping_cart.py'''


####NOW THE SCRIPT FOLLOWS BELOW:

# SECTION INPUT


# Professor Rossetti's suggested if else loop, (try block)


import os
import pprint
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime #Taken from stackoverflow

total_price = 0
selected_ids = []



while True:
    selected_id = input("Please input a product identifier, if you're finished enter 'DONE':" )
    
#  try converting the input (that is string) into integer
#  try: except: incorporation as a potential alternative
    
    if selected_id == "DONE":
        break # stops the loop
    if selected_id.isdigit() == False: # Attributed this line of code concept to classmate Harrison Grubb's advice, 
        # more details located from https://www.tutorialspoint.com/python/string_isdigit.htm, script concept borrowed from website after research
        print("Please enter numbers, not text. (From 1~20)")
    elif int(selected_id) > 0 and int(selected_id) < 21: # Attribute this section loop to Prof. Rossetti
        # this ensures that only integers from 1 to 20 is valid
        selected_ids.append(selected_id)
    else:
        print("Invalid Input, please enter a valid input. (From 1~20)")
        next # proceeds into the next iteration of the loop (OK to omit in this basic example because there is no more code following it inside the loop before the loop repeats)

# print(selected_ids) --> these were included for testing processes, can confirm that the loop works well
# print(len(selected_ids))

    
        
print("-------------------------------------------------------------------------------------------------------------------------")        
print("GREEN FOODS GROCERY")
print("WWW.GREEN-FOODS-GROCERY.COM")
print("-------------------------------------------------------------------------------------------------------------------------") 
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

print("-------------------------------------------------------------------------------------------------------------------------")
print("SUBTOTAL: $","{0:.2f}".format(total_price))
ny_sales_tax = 0.0876 #8.875% is the NYC combined rate
tax = "{0:.2f}".format(total_price * ny_sales_tax) 
#Make sure to format with digits to avoid additional decimals and keep hundredth value in case of 0 eg. $3.50
print("NYC TAX $:", tax)
grand_total = "{0:.2f}".format(total_price + (total_price * ny_sales_tax))
print("TOTAL $:", grand_total)

# "{0:.2f}".format(i["price"])

print("-------------------------------------------------------------------------------------------------------------------------")
print("THANK YOU FOR SHOPPING WITH US, PLEASE COME AGAIN!")
print("-------------------------------------------------------------------------------------------------------------------------")





# MESSAGE WITH CUSTOMER EMAIL SO THAT RECEIPT IS AUTO - EMAILED BACK TO CUSTOMER

# Note for professor --> was able to send email with visual, greeting and total cost including tax 
# However, faced difficulties in sending each product line with associated price 


# import os
# import pprint
# from dotenv import load_dotenv
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

# d-9fd75bfad7a740e7a1716705c95f4f0b --> example receipt template code from sendgrid


load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

#print("API KEY:", SENDGRID_API_KEY)
#print("TEMPLATE ID:", SENDGRID_TEMPLATE_ID)
#print("EMAIL ADDRESS:", MY_ADDRESS)

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

subject = "Your Receipt from the GREEN FOODS GROCERY"

template_data = {
    "total_price_usd": grand_total,
    "human_friendly_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "products": [ 
        product_name 
        ] 
    
} # or construct this dictionary dynamically based on the results of some other process :-D

client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client))

message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS, subject=subject)

print("MESSAGE:", type(message))

message.template_id = SENDGRID_TEMPLATE_ID

message.dynamic_template_data = template_data


try:
    response = client.send(message)

    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS  --> email correctly sends with no issues
    print(response.body)
    print(response.headers)

except Exception as e:
    print("OOPS", e)