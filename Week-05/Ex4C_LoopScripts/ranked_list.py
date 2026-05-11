fav_food = ["Alfredo pasta", "injera", "Tacos", "Ramen", "Lasagna"]

# using enumerate() for numbering loop
for index, item in enumerate(fav_food, start=1):  #starting at "alfredo pasta"
    if index == 1:
        print(index, ".", item, "<- top pick!") #
    else:
        print(index, ".", item) 
#OUTPUT:
#1 . Alfredo pasta <- top pick!
#2 . injera
#3 . Tacos
#4 . Ramen
#5 . Lasagna




