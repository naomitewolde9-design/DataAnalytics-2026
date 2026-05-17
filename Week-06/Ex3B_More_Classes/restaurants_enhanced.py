
class Restaurant:
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def add_num_served(self):
        while True:
            try:
                num = int(input("How many customers served today? "))
                if num >= 0:
                    self.number_served += num
                    break
                else:
                    print("Please enter a non-negative number.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")
    
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            rating = input("Rate your experience (1-5): ")

            if rating.isdigit() and 1 <= int(rating) <= 5:
                rating = int(rating)
                self.customer_ratings.append(rating)
                avg = sum(self.customer_ratings) / len(self.customer_ratings)
                print(f"Your rating was {rating}. The average rating is {avg:.2f}")
                break
            else:
                print("Enter a whole number between 1 and 5.")


# Create restaurants
rest1 = Restaurant("Mr.Tokyo", "Japanese")
rest2 = Restaurant("Cheesecake Factory", "American")
rest3 = Restaurant("Taco Bell", "Mexican")


# TEST number served
print("\n--- Testing number served ---")
rest1.print_num_served()
rest1.add_num_served()
rest1.add_num_served()
rest1.print_num_served()


# TEST ratings
print("\n--- Testing ratings ---")
rest1.customer_rating()
rest1.customer_rating()
rest1.customer_rating()


