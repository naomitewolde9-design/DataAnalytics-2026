# tuples and lists: examples of unpacking 
# tuples ()
# lists []
a, b, c = [1,2,3]
print(a)

veg_t = ("carrot", "broccoli", "carrot")
veg1, veg2, veg3 = veg_t
print(veg1)
print(veg2)
print(veg3)
print()

_, b, c = veg_t
# to skip a value veg_1 carrot

lots_vegs = ("carrot", "broccoli","carrot", "carrot", "raddish")
car, bro, _, _, rad = lots_vegs
print(car)
print(bro)
print(rad)
print()

#alt version of unpacking 

car2 = lots_vegs[0]
bro2 = lots_vegs[-1]
rad2 = lots_vegs[-2]
print(car2)
print(bro2)
print(rad2)
print()

#astric * creates a list from the values 
x, y, *z = lots_vegs
print(x)
print(y)
print(z)
print()

#Example: Convert the tuple into a list, change the list, then convert back to a tuple
tuple_b = ("apple", "banana", "cherry") #tuple
tuple_b = list(tuple_b) # turning into a list
tuple_b.append("orange") #adding orange to a list to change it because you can't change a tuple
tuple_b = tuple(tuple_b) # turning it back into a tuple 
print(tuple_b)

# look up how to add tupples 

#SETS only stores uniqye variables not duplicats and when it prints it doesn't have
# a specific order 
lots_vegs = ("carrot", "broccoli","carrot", "carrot", "raddish")
lots_vegs = set(lots_vegs)
print(lots_vegs)
print()

# guest list example using sets(sets are in curly braces)
# in is a fuction to look for if a value belongs to this set of values(conditional)
guests = {"naomi", "victoria" , "alexus", "lesley"}
#seating list
s1, s2, s3, s4 = guests
print(s1)
print(s2)
print(s3)
print(s4)
print()
# to see if this person has seating: bool (t/f)
print("victoria" in guests) # true
print('alexus' in guests) #true 
print('luis' in guests) #false
print()

#How to add to a set 
guests.add("luis")
print(guests)
print("luis" in guests)
print()

#how to add to a set to a set
alexus_add = ["hannah", "alondra", "lorah", "blake"]

guests.update(alexus_add)
print(guests)

# dictionary (dict)
#student guide example
contact_bb = {
 "name": "Bilbo Baggins",
 "birthday": "1999-03-25",
 "email": "bilbo.baggins@email.mail"
 } 
print()
print(contact_bb)
print(contact_bb["name"])
print(contact_bb["birthday"])
print(contact_bb["email"])
print()

#example using f-string, .keys(), .items(), .values()
exam_1 = {"baggins":.87, "gamgee":.92, "took":.78}
print(exam_1)
print(f'Score for SG: {exam_1["gamgee"]}')
print()
print(exam_1.keys()) # str values
print(exam_1.values()) #variables in the keys/values
print(exam_1.items()) # pairs the values and variables in a tuple?
print()

# example: using .pop() and .items()
print(f'score foe gandalf: {exam_1.get('gandalf', 'did not take the exam')}')
print()

print(exam_1.items()) # pulls up the list 
print()

exam_1.pop('took') # .pop() removes specific value from list 
print(exam_1.items()) # pulls up new dict with out the .pop(ped) value(without 'took)
print('took' in exam_1) # false because it was exam_1.pop out of dict
print(0.78 in exam_1) # we can't fetch for a stored value belonging to 'baggins' key it has to be the name 
print()

#nested collection

list_of_lists = [[1, 2, 3,'a'], [2, 3, 4], [4, 5, 6, 7, 8]]
list_of_tuples = [(2, 3), ('a', 'b'), ('alexus', 'victoria')]
print('first tuple', list_of_tuples[0]) #
print('first item from first tuple', list_of_tuples[0][0]) # first item/ first varible (2,3)(2)
print()

ut1, ut2, ut3 = list_of_tuples
print(ut1)
print()

#working with if / else

groceries = ['apple', 'mango', 'harissa']

check_groc = input("check for item in grocieries list: ")

if 'brocoli' in groceries: 
    print("yes, I remembered to add it")
else:
    print('no, not in list')

if 'harissa' in groceries:
    print('yes I remembered harissa')
else: #check_groc, adding new items to the list using if/else
    ('no not in list') 
if check_groc in groceries: # inputing item in terminal (ex: harissa = yes, added to list)
    print("yes, added to list!")
else:
    groceries.append(check_groc) # if typed in item is not in list it will add it with .append
    print(f'{check_groc} was added to the list') #prints after you type input in terminal

print(f'Grocery list include {groceries}') # prints new list 

#look up case match looks up specific unique values without conditions