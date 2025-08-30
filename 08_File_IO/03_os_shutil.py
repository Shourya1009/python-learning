# 09_os_shutil_demo.py

import os
import shutil

# ---------- OS MODULE ----------
print("---- OS MODULE DEMO ----")

# Get current working directory
print("Current Directory:", os.getcwd())

# Create a new folder if it doesn't exist
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("Created folder: test_folder")

# Create nested directories
if not os.path.exists("parent/child"):
    os.makedirs("parent/child")
    print("Created nested directories: parent/child")

# List all files and folders in current directory
print("List of files in current directory:", os.listdir())

# Check if a file exists
print("Does sample.txt exist?", os.path.exists("sample.txt"))

# Path join (OS independent)
print("Joined Path:", os.path.join("folder", "file.txt"))


# ---------- FILE CREATION ----------
print("\n---- FILE CREATION ----")
with open("sample.txt", "w") as f:
    f.write("Hello from sample file.")

print("Created 'sample.txt' with some text.")


# ---------- SHUTIL MODULE ----------
print("\n---- SHUTIL MODULE DEMO ----")

# Copy file
shutil.copy("sample.txt", "sample_copy.txt")
print("Copied 'sample.txt' → 'sample_copy.txt'")

# Copy with metadata
shutil.copy2("sample.txt", "sample_copy_meta.txt")
print("Copied 'sample.txt' with metadata → 'sample_copy_meta.txt'")

# Move file into test_folder
shutil.move("sample_copy.txt", "test_folder/sample_moved.txt")
print("Moved 'sample_copy.txt' → test_folder/")

# Show contents of test_folder
print("Files inside test_folder:", os.listdir("test_folder"))

# Disk usage info
total, used, free = shutil.disk_usage(".")
print("Disk Usage → Total:", total, "Used:", used, "Free:", free)

# ---------- CLEANUP DEMO ----------
print("\n---- CLEANUP DEMO ----")

# Delete files
if os.path.exists("sample_copy_meta.txt"):
    os.remove("sample_copy_meta.txt")
    print("Deleted 'sample_copy_meta.txt'")

# Delete a whole directory (CAREFUL!)
if os.path.exists("parent"):
    shutil.rmtree("parent")
    print("Deleted 'parent' folder with all subfolders")
