#How do you calculate the distance between coordinates (x1, y1) and (x2, y2)?

import math 

#in feet
length = 20 
width = 10 

tiles_needed = length * width 

#tiles per box
per_box = 5 

#math.ceil is rounding up for example 7.1 would be 7, or 4.2 would be 5
boxes_needed = math.ceil(tiles_needed/per_box)

print(boxes_needed)
#40

#10% more
more_tiles = tiles_needed*0.10
#added the calc tiles needed already plus the 10% more tiles 
total_tiles = tiles_needed + more_tiles

total_boxes = math.ceil(total_tiles/per_box)

print(f'The amount of boxes need: {boxes_needed}')
#With the additional 10% tiles
print(f'The amount of extra boxes for the tiles would be a total of {total_boxes} boxes')

#OUTPUT 
#40
#The amount of boxes need: 40
#The amount of extra boxes for the tiles would be a total of 44 boxes