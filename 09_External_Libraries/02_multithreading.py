import threading
import time

# Task function for numbers
def print_numbers(delay):
    print(f"[{threading.current_thread().name}] Starting...")
    for i in range(1, 6):
        print(f"[{threading.current_thread().name}] Number: {i}")
        time.sleep(delay)
    print(f"[{threading.current_thread().name}] Finished.")

# Task function for letters
def print_letters(delay):
    print(f"[{threading.current_thread().name}] Starting...")
    for letter in "ABCDE":
        print(f"[{threading.current_thread().name}] Letter: {letter}")
        time.sleep(delay)
    print(f"[{threading.current_thread().name}] Finished.")

# Task function for symbols
def print_symbols(delay):
    print(f"[{threading.current_thread().name}] Starting...")
    for symbol in "!@#$%":
        print(f"[{threading.current_thread().name}] Symbol: {symbol}")
        time.sleep(delay)
    print(f"[{threading.current_thread().name}] Finished.")

# Main code
if __name__ == "__main__":
    # Create threads with different delays
    t1 = threading.Thread(target=print_numbers, args=(1,), name="Number-Thread")
    t2 = threading.Thread(target=print_letters, args=(0.8,), name="Letter-Thread")
    t3 = threading.Thread(target=print_symbols, args=(0.5,), name="Symbol-Thread")

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for threads to finish
    t1.join()
    t2.join()
    t3.join()

    print("✅ All threads finished execution.")