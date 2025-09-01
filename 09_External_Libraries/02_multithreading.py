import threading
import time

# Task function
def print_numbers():
    for i in range(1, 6):
        print(f"[{threading.current_thread().name}] Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in "ABCDE":
        print(f"[{threading.current_thread().name}] Letter: {letter}")
        time.sleep(1)

# Main code
if __name__ == "__main__":
    # Create threads
    t1 = threading.Thread(target=print_numbers, name="Thread-1")
    t2 = threading.Thread(target=print_letters, name="Thread-2")

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

    print("✅ Both threads finished execution.")