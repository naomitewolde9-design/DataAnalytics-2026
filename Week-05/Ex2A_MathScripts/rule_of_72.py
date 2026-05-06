savings = 12000
interest_rate = 0.08 #8%

doubled_in_years = 72/(interest_rate*100) #using the rule of 72 and creating the float into a 8% by multiplying by 100
savings_db = savings*2 # were looking for our saving to double, need this for the sentence

print("Your current savings is $" + str(savings))
print("At a " + format(interest_rate, ".0%" ) + ' ' + 'interest rate, your savings account will be' )
print("worth $" + format(savings_db, ".2f") + " in " + format(doubled_in_years, ".1f") + " years")
#OUTPUT:
#Your current savings is $12000
#At a 8% interest rate, your savings account will be
#worth $24000.00 in 9.0 years