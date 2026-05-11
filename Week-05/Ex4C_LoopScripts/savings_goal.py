# creating "while" loop to reach savings goal

# calculating values (can change whenever)
balance = 222
savings_goal = 550
weekly_save = 221

# using "while" loop saving half way to goal
while balance < savings_goal:
    if balance >= savings_goal * 0.50 and balance < savings_goal * 0.75:  #more than halfway
        balance += weekly_save 
        print("Almost there! This week my balance is up to", balance)
    else:  
        balance += weekly_save
        print("This week my balance increased to", balance)

# final print for loop completion
print("Goal met! My current balance is", balance)


#OUTPUT 
#This week my balance increased to 443
#This week my balance increased to 664
#Goal met! My current balance is 664