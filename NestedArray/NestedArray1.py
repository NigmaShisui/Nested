#we call this array a sublist para sa tanan arrays nga sulod sa isa ka array, i mean literal gyud nga sublist na ang tawag ani saiya
#if daghan na nga array ang sulod sa isa ka array
names = [['Alice', 'Bob', 'Charlie'], #sublist 1 names[0]
         ['David', 'Eve', 'Frank'],     #sublist 2 names[1]
         ['Grace', 'Heidi', 'Ivan'],    #sublist 3 names[2]
         ['Judy', 'Ken', 'Laura']]      #sublist 4 names[3]

# the user input a name to remove
nameRemove = input("Enter the name you want to remove (if it exists): ")

nameFound = False  # chgeck if the name exists atong name nato nga variable

# Outer loop for reading sa nested array
for sublist in names:
    if nameRemove in sublist:
        sublist.remove(nameRemove)  # Remove the name
        nameFound = True
        print(f'"{nameRemove}" has been removed from the array.')
        break  # Exit the loop once the name is found and removed

# If the name was not found, add a new name
if not nameFound:
    new_name = input(f'"{nameRemove}" does not exist. Enter a new name to add to the array: ')
    names[0].append(new_name)  # Add the new name to the first sublist, kay atong nabutang is [0]

# Print the updated array
print("Updated array:", names)
