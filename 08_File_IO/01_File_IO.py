"""
File I/O in Python
------------------

File I/O (Input/Output) in Python allows us to interact with files
— either by reading data from them or writing data into them.

Python provides built-in functions like `open()`, `read()`, `write()`,
and also supports context managers (`with` statement) for safe and efficient handling of files.

File Modes:
-----------
- 'r'  : Read mode (default). Raises an error if file does not exist.
- 'w'  : Write mode. Creates a new file or overwrites an existing one.
- 'a'  : Append mode. Adds data to the end of the file without overwriting.
- 'x'  : Exclusive creation. Raises an error if file already exists.
- 'b'  : Binary mode (e.g., 'rb', 'wb').
- 't'  : Text mode (default).

Common Methods:
---------------
- file.read([n])     -> Reads entire file or first n characters.
- file.readline()    -> Reads one line at a time.
- file.readlines()   -> Reads all lines and returns them as a list.
- file.write(str)    -> Writes a string into the file.
- file.writelines()  -> Writes a list of strings into the file.
- file.close()       -> Closes the file (important to free resources).

Note:
-----
It is recommended to use `with open(...) as f:` 
because it automatically closes the file after completing operations.
"""

# ------------------------------------------------
# Example 1: Writing to a file
# ------------------------------------------------
with open("example.txt", "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("This is the second line.\n")  # added newline for consistency

# ------------------------------------------------
# Example 2: Reading from a file
# ------------------------------------------------
with open("example.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)

# ------------------------------------------------
# Example 3: Appending to a file
# ------------------------------------------------
with open("example.txt", "a") as f:
    f.write("\nThis line is appended.")

# ------------------------------------------------
# Example 4: Reading file line by line
# ------------------------------------------------
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())  # removes extra newline characters