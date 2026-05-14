import random 

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp','Surge Protector']

#a) randomly selects item 
random_product = random.choice(products)
print( "Product of the Day: " + random_product)
# Output:
# Product of the Day: Headset

#b) using random.sample() to select 3 items

selected_products = random.sample(products, 3)
print(f'Brief usability survey: {selected_products}')
#OUTPUT: Brief usability survey: ['Keyboard', 'Monitor', 'Webcam']

#c) Using random.shuffle() to look at shuffled product list 

random.shuffle(products)
print(f'Updated shuffled list: {products}')
#OUTPUT:
# Updated shuffled list: ['Desk Lamp', 'USB Hub', 'Docking Station', 
#'Webcam', 'Surge Protector', 'Monitor', 'Laptop', 
# 'Keyboard', 'Headset', 'Mouse']

#d) Using random.randint() to find transaction amt between 30-500 

daily_transactions = random.randint(50, 300)
# printing the result with a label and colon for formating 
print("Daily Transaction Count:", daily_transactions)
# OUTPUT: Daily Transaction Count: 197

