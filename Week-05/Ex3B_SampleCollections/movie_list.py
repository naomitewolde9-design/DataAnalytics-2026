movies = ["Everything, Everywhere, All at Once", "Soul_Pixar", "Alice in Wonderland", "Onward_Pixar"]

print(f'This list includes a list of my top {len(movies)} favorite movies {movies}')
# This list includes a list of my top 4 favorite movies ['Everything, Everywhere, All at Once', 'Soul_Pixar', 'Alice in Wonderland', 'Onward_Pixar']
print()
print(sorted(movies))
# ['Alice in Wonderland', 'Everything, Everywhere, All at Once', 'Onward_Pixar', 'Soul_Pixar']
print(movies) # ['Everything, Everywhere, All at Once', 'Soul_Pixar', 'Alice in Wonderland', 'Onward_Pixar']
print()
# The difference between the two out put is that the secound print has the list in aphabetical order 

movies.sort()
print(movies)
# ['Alice in Wonderland', 'Everything, Everywhere, All at Once', 'Onward_Pixar', 'Soul_Pixar']

movies.append("Hereditary")
print(movies)
movies.sort()
print(movies)
#['Alice in Wonderland', 'Everything, Everywhere, All at Once', 'Hereditary', 'Onward_Pixar', 'Soul_Pixar']