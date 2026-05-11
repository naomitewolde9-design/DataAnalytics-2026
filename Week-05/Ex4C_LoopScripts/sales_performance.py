sales_data = [
 ('Marcus Webb', 'East', 4250.00),
 ('Priya Sharma', 'West', 5875.50),
 ('DeShawn Carter', 'East', 3100.75),
 ('LaTonya Rivers', 'South', 6420.00),
 ('Bob Nguyen', 'West', 4980.25),]


money_total = 0

for name,region,sales in sales_data:

    money_total += sales 

    if sales >= 5000:

        print(f'{name}: {region}: ${sales:,.2f}  ^ top performer!')
    else:
        print(f'{name}: {region}: ${sales:,.2f}')
    print(f'Running total {money_total:.2f}')

#Marcus Webb: East: $4,250.00
#Running total 4250.00

#Priya Sharma: West: $5,875.50  ^ top performer!
#Running total 10125.50

#DeShawn Carter: East: $3,100.75
#Running total 13226.25

#LaTonya Rivers: South: $6,420.00  ^ top performer!
#Running total 19646.25

#Bob Nguyen: West: $4,980.25
#Running total 24626.50
 
