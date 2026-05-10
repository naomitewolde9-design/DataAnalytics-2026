# calc taxes based on annual income and how you fill taxes(if/else/elif)

#varibles from overtime pay_rules.py hw
hours_worked = 40
pay_rate = 25.50
filing = "Single"

# Weekly pay calculation for gross pay using if and else 
if hours_worked > 40:
    overtime = hours_worked - 40
    gross_pay = (40*pay_rate)+(overtime*pay_rate*1.5) 
else:
    gross_pay = hours_worked*pay_rate

#Now calculating year gross pay by multiplying 52 
annual_income = gross_pay*52

#Now filing for single tax rate 
if filing == "Single":
    if annual_income < 12000: #5% tax rate under "single"
        tax_rate = 0.05
    elif annual_income < 25000: #round the 10% income (24999)
        tax_rate = 0.10
    elif annual_income < 75000:
        tax_rate = 0.15
    else: 
        tax_rate = 0.20

#Now filing for joint tax rate 
if filing == "Joint":
    if annual_income < 12000:
        tax_rate = 0.00
    elif annual_income < 25000:
        tax_rate = 0.06
    elif annual_income < 75000:
        tax_rate = 0.11
    else: 
        tax_rate = 0.20

# weekly tax 
weekly_tax = gross_pay*tax_rate

#annual tax 
net_pay = gross_pay-weekly_tax

print("You worked", hours_worked, "hours this period")
print("Because you earn $", pay_rate, "per hour, your gross weekly pay is $", round(gross_pay, 2))
print("Your filing status is:", filing)
print("Your tax withholding for the week it $", round(weekly_tax, 2))
print("your net pay is $", round(net_pay, 2))

#You worked 40 hours this period
#Because you earn $ 25.5 per hour, your gross weekly pay is $ 1020.0
#Your filing status is: Single
#Your tax withholding for the week it $ 153.0
#your net pay is $ 867.0