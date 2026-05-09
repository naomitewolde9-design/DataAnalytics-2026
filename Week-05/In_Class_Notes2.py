# conditional logic example of a friendly greeting: 
# we want to program to great the user with user reply 
# and the program replies back 

user_reply = input('Hello! (enter "hi"): ')


#calc the unknown 

# if user_reply[0:2].lower == "hi": (if the value of user_reply, we only want the first 2 characters)
# "in" is looking for the str in the user_reply and lower converts all characters into lower case 
if "hi" in user_reply.lower():
    print("Nice to see ya")
#elif user_reply == "HI" :
#    print("NICE TO SEE U!")
#elif user_reply == "sup" :
#    print("sup bro how are ya")
else: 
    print("okay ig...")

# NOT example 
#if user_reply != "hi" : 
#    print("sorry huh??")


# example of replace to remove extra (replace) !
user_reply2 = input("how are ya? ")
pos_resp = ["fine", "good", "great", "wonderful","alright"] #list [], tuples (), dict {}
#replace needs what you want to replace COMMA make it nothing 
if user_reply2.lower().replace("!", ' ').replace(",", ' ') in pos_resp:
    print("thats cool")
else: 
    print("lovely weather were having")
print()


#boolean (bool)
# true, false, or none cannot be a value
# 
print(None == False) #False
print(bool(None) == False) # True 
print()


# Using and/ or/ not page 72 

strawb = input('Strawberry? Y/N: ')
blueb = input('Blueberry? Y/N: ')
fresh = input('Are the berries fresh? Y/N: ')
if (strawb =='Y' or blueb =='Y') and fresh == 'Y': #Blue and straw if it's true (Y) "and" if its True to "Y" with fresh then it's "buy it"
     print('Buy it!')
else:
    print("Don't buy it")
print()


# calc grade for exam using if/elif/f-string (condition (if/elif/else) goes in order,so it goes down the list of conditions)

points_possible = 85 

raw_score = int(input("student score (raw points): "))

score = raw_score/ points_possible

print(f'Percentage score is {score: .0%}')

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D' 
else:
    grade = 'F'
print(f'Student exam grade is: {score}')
print()


# using loops: examples 

for i in ['a', 'b', 'c']:
    print(f'At this step i is {i}')

#At this step i is a
#At this step i is b
#At this step i is c

for i in '123':
    print(f'at this step, the iterator calue is {i}')

#at this step, the iterator calue is 1
#at this step, the iterator calue is 2
#at this step, the iterator calue is 3


groceries = ['apples', 'peaches', 'bread']

basket = []

for i in groceries:
    if i == 'apples':
        print('how about them apples')
        basket.append(i)
    elif i == 'bread':
        print('get that bread')
        basket.append(i)
    elif i == 'peaches':
        print("peaches are nice")
        basket.append(i)
    print('end loop')

print(f'Grocery basket includes {basket}')

# while loop example 

sky = input('what color is the sky')

while sky != '':
    print(f'the sky is {sky}')
    if sky == 'blue': #prints over and over again until you do ctrl + c 
        print('sounds about right') 
        sky = '' #ends loop
    else:
        print('are you sure???')
        sky = input('what color is the sky')


# using counter 

counter = 0 

while counter < 3: #running it 3 times 
    print("still running the loop")
    counter += 1 