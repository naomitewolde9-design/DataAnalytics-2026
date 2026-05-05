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
