"""
File I/O in Python
------------------

File I/O (Input/Output) in Python allows us to interact with files 
— reading data from them or writing data into them.

Python provides built-in functions like `open()`, `read()`, `write()`, 
and context managers (`with` statement) to handle files easily.

File Modes:
-----------
- 'r'  : Read (default). Error if file not found.
- 'w'  : Write. Creates new file or overwrites existing.
- 'a'  : Append. Adds data to the end of file without overwriting.
- 'x'  : Exclusive creation. Error if file already exists.
- 'b'  : Binary mode (e.g., 'rb', 'wb').
- 't'  : Text mode (default).

Common Methods:
---------------
- file.read([n])     -> Reads entire file or first n characters.
- file.readline()    -> Reads one line.
- file.readlines()   -> Reads all lines into a list.
- file.write(str)    -> Writes a string to the file.
- file.writelines()  -> Writes list of strings to the file.
- file.close()       -> Closes the file (important to free resources).

It’s recommended to use `with open(...) as f:` 
since it auto-closes the file after operations.
"""

# ------------------------------------------------
# Example 1: Writing to a file
# ------------------------------------------------
with open("example.txt", "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("This is the second line.")

# ------------------------------------------------
# Example 2: Reading from a file
# ------------------------------------------------
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# ------------------------------------------------
# Example 3: Appending to a file
# ------------------------------------------------
with open("example.txt", "a") as f:
    f.write("\nThis line is appended.")

# ------------------------------------------------
# Example 4: Reading line by line
# ------------------------------------------------
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
