# The break Statement

# With the break statement we can stop the loop even if the while condition is true:
print("Break statement : ")
for i in range(1,21):
  if i==10:
    break
  print(i)
  





# The continue Statement

# With the continue statement we can stop the current iteration, and continue with the next:
# basically it skip that iteration and continues to move further
print("Continue Statement : ")
for i in range(1,21):
  if i==15:
    continue
  print(i)






# Pass Statement

# The  pass statement is a placeholder that does nothing. It is used when syntax requires a statement but no action is needed.


# Pass keyword in a function is used when we define a function but don’t want to implement its logic immediately. It allows the function to be syntactically valid, even though it doesn’t perform any actions yet.
def fun():
    pass  # Placeholder, no functionality yet

# Call the function
fun()



print("Pass statement : ")

for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    else:
        print(i)