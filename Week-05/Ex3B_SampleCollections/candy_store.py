#candy
#create variables for candy and flavors within the tuples
candy = ("Gum", "gummies", "taffy")
flavors = ("strawberry", "rasberry", "watermelon")

#value name to hold the sets
pairs = set()

# use .add the keys and values from the tuples 
pairs.add(candy[0]+"-"+flavors[1])
pairs.add(candy[1]+"-"+flavors[2])
pairs.add(candy[2]+"-"+flavors[0])

print("Today's candy includes:")
print(pairs)
#{'taffy-strawberry', 'Gum-rasberry', 'gummies-watermelon'}
#{'Gum-rasberry', 'gummies-watermelon', 'taffy-strawberry'}
#{'gummies-watermelon', 'Gum-rasberry', 'taffy-strawberry'}