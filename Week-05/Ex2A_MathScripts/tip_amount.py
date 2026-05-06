bill = 236 
tip = bill*0.20
# print(tip) # OUTPUT: 47.2
# Usually resturants automatically charge 18%-20% gratuity 

#print('The tip on a $' + str(bill) + " " + 'restaurant bill is $' + str(tip) )
#OUTPUT: The tip on a $236 restaurant bill is $47.2

# lets try this using the function "format"

print('The tip on a $' + format(bill, ".2f") + " " + 'restaurant bill is $' + format(tip, ".2f") )

#OUTPUT
# The tip on a $236.00 restaurant bill is $47.20


# LAB 3 for INPUT functions 

bill_amount = input("what was the bill for the food you got? ")
tip_amount = input("How much did you tip? ")
food_critic = input("How would you rate your food 1-10? ")
print("Your total bill was $" + bill_amount + ", you also tipped $" + tip_amount + " and you rated the food from 1-10 a: " + food_critic)

#Output:

#what was the bill for the food you got? 236
#How much did you tip? 47.20
#How would you rate your food 1-10? 10
#Your total bill was $236, you also tipped $47.20 and you rated the food from 1-10 a: 10