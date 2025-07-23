# String slicing - this works same as range function - in this we have a starting point and a colon (:) and an ending point which will run till (ending point-1)

# Syntax :- variable_name[starting_point : ending_point[n-1]]
# variable_name[starting_point : n-1]


name="Shourya0123456789"
print(name[0:2])  # it will run till 1 , it will go from 0 to 1
print(len(name))
print(name[2:-1])  

#  -1+17=16 which is index 16 
#  Same as [2:16]
#  goes from index 2 to 15 
#  according to string slicing it will go from 2 to -2 (-1-1=-2)  






# [starting_point : ending_point : n] - this n will skip n-1 character
# Example : - 

print(name[0:10:1]) # it will skip (1-1=0) character i.e it will not skip anything
print(name[0:10:3]) # it will skip 2 character 






# What will happen if we dont give a starting or an ending point

print(name[:4])  # Replace first empty number with 0
print(name[1:])  # Replace second empty number with length 


# To reverse a string 
print(name[::-1])