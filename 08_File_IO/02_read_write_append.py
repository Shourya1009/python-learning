"""
Read, Write, and Append in File Handling
----------------------------------------

In Python, files can be handled using the `open()` function with different modes. 
The most commonly used modes are:

1. Read Mode ('r')
   - Opens a file for reading.
   - Raises an error if the file does not exist.
   - Methods:
       - read()     -> Reads entire file or specified number of characters.
       - readline() -> Reads a single line.
       - readlines()-> Reads all lines into a list.

2. Write Mode ('w')
   - Opens a file for writing.
   - Creates a new file if it doesn’t exist.
   - Overwrites the file if it already exists.
   - Methods:
       - write(string)    -> Writes a string to the file.
       - writelines(list) -> Writes multiple strings.

3. Append Mode ('a')
   - Opens a file for appending.
   - Creates a new file if it doesn’t exist.
   - Adds data to the end of the file without overwriting existing content.

It’s recommended to use `with open(...) as f:` for file handling 
since it automatically closes the file after operations.
"""

# Writing to a file (creates the file if it does not exist)
with open("sample.txt", "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("This is the second line.\n")

print("File created and data written successfully.\n")

# Appending to the file (adds content without deleting old data)
with open("sample.txt", "a") as f:
    f.write("This line is added later.\n")

print("Data appended successfully.\n")

# Reading the file safely
try:
    with open("sample.txt", "r") as f:
        content = f.read()
        print("File Content:\n")
        print(content)
except FileNotFoundError:
    print("Error: sample.txt does not exist!")
