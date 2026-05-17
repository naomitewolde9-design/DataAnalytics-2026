
class Restaurant:
   
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
    
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    
    def rest_open(self):
        print(f"{self.rest_name} is open.")

# Create three instances
rest1 = Restaurant("Wendy's", "fast food")
rest2 = Restaurant("Dunkin Donuts", "coffee and donuts")
rest3 = Restaurant("Taco Bell", "Mexican-inspired fast food")

# Test the methods
rest1.describe_rest()
rest1.rest_open()

rest2.describe_rest()
rest2.rest_open()

rest3.describe_rest()
rest3.rest_open()

#OUTPUT:
#Wendy's serves fast food.
#Wendy's is open.
#Dunkin Donuts serves coffee and donuts.
#Dunkin Donuts is open.
#Taco Bell serves Mexican-inspired fast food.
#Taco Bell is open.