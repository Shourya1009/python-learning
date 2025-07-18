# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

i=1
while i<6:
    print(i)
    i+=1



# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
i = 1
while i < 6:
  print(i)
  i += 1
  


print("Count : ")
count=0
while count<5:
    print(count)
    count+=1



# Infinite Loop in Python :

# while True:
#     print("It will run till infinity")


# While loop with continue statement

s=5
while(s<10):
   s+=1
   if s==8:
      continue
   print(s)
