#How many vans do you need? How 
#much will it cost to rent vans? What is the cost if you split it per person?

import math

ppl_tour = 38
van_seats = 15 
#per day van cost, included with drivers pay 
van_cost = 250
#math.ceil since it's people, can't round up a person

#how many vans needed based on people(38)
vans_needed = math.ceil(ppl_tour/van_seats)

#total cost for all the vans considering the people 
vans_total = vans_needed*van_cost

# How much per person
per_person = vans_total/ppl_tour

print(f'Total vans needed: {vans_needed}')
print(f'Total rental van cost: {vans_total}')
print(f"Cost total per person: {per_person: .2f}")

#There was a leftover amount becuase we had to round up for seating in the vans using math.ceil, no tourist left behind!