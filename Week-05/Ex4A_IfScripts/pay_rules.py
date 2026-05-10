# 20 hour pay rate variables

hours_worked = 20
pay_rate = 12.50 

if hours_worked > 40: 
    overtime = hours_worked - 40 
    gross_pay = (40*pay_rate)+(pay_rate*overtime*1.5) # overtimes hours get paid 1.5 times the regular rate hours
else:
    gross_pay = pay_rate*hours_worked 

print("Gross Pay is:", gross_pay)
#Gross Pay is: 250.0


# 40 hours pay rate variables 

hours_worked2 = 40
pay_rate2 = 25.50 

if hours_worked2 > 40:
    overtime2 = hours_worked2 - 40
    overtime2 = (40*pay_rate2)+(pay_rate2*overtime2*1.5)
else:
    gross_pay2 = hours_worked2*pay_rate2

print("Gross pay is:", gross_pay2)
#Gross pay is: 1020.0


# 45 hours pay rate variable

hours_worked3 = 45
pay_rate3 = 17.30

if hours_worked3 > 40:
    overtime3 = hours_worked3 - 40
    gross_pay3 = (40*pay_rate3)+(pay_rate3*overtime3*1.5)
else:
    gross_pay3 = hours_worked3*pay_rate3

print("Gross pay is:", gross_pay3)
# Gross pay is: 821.75