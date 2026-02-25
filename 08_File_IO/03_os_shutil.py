# 09_os_shutil_demo.py

import os
import shutil


def os_demo():
    print("---- OS MODULE DEMO ----")

    # Current working directory
    cwd = os.getcwd()
    print(f"Current Directory: {cwd}")

    # Create folder safely
    os.makedirs("test_folder", exist_ok=True)
    print("Ensured folder exists: test_folder")

    # Create nested directories safely
    os.makedirs("parent/child", exist_ok=True)
    print("Ensured nested directories exist: parent/child")

    # List directory contents
    print("Items in current directory:")
    for item in os.listdir():
        print(" -", item)

    # Check file existence
    print("Does sample.txt exist?", os.path.exists("sample.txt"))

    # Cross-platform path join
    joined_path = os.path.join("folder", "file.txt")
    print("Joined Path:", joined_path)


def file_creation():
    print("\n---- FILE CREATION ----")

    with open("sample.txt", "w") as f:
        f.write("Hello from sample file.\nThis file is used for OS & shutil demo.")

    size = os.path.getsize("sample.txt")
    print(f"Created 'sample.txt' ({size} bytes)")


def shutil_demo():
    print("\n---- SHUTIL MODULE DEMO ----")

    # Copy file
    shutil.copy("sample.txt", "sample_copy.txt")
    print("Copied → sample_copy.txt")

    # Copy with metadata
    shutil.copy2("sample.txt", "sample_copy_meta.txt")
    print("Copied with metadata → sample_copy_meta.txt")

    # Move file
    shutil.move("sample_copy.txt", os.path.join("test_folder", "sample_moved.txt"))
    print("Moved sample_copy.txt → test_folder/")

    # Show contents of test folder
    print("Files inside test_folder:", os.listdir("test_folder"))

    # Disk usage (convert to GB)
    total, used, free = shutil.disk_usage(".")
    gb = 1024 ** 3
    print(f"Disk Usage → Total: {total/gb:.2f} GB | Used: {used/gb:.2f} GB | Free: {free/gb:.2f} GB")


def cleanup():
    print("\n---- CLEANUP DEMO ----")

    # Delete metadata copy
    if os.path.exists("sample_copy_meta.txt"):
        os.remove("sample_copy_meta.txt")
        print("Deleted sample_copy_meta.txt")

    # Delete nested directory
    if os.path.exists("parent"):
        shutil.rmtree("parent")
        print("Deleted parent folder and its contents")


if __name__ == "__main__":
    os_demo()
    file_creation()
    shutil_demo()
    cleanup()