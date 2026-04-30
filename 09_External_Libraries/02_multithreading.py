"""
Multithreading in Python
------------------------

Multithreading allows a program to run multiple tasks (threads) concurrently
within the same process.

Why use Multithreading?
-----------------------
- Improves responsiveness of programs
- Useful for I/O-bound tasks (downloading, file reading, waiting)
- Allows multiple functions to run seemingly at the same time

Important Concepts:
-------------------
1. Thread:
   - A lightweight unit of execution inside a process.
   - Multiple threads share the same memory space.

2. Main Thread:
   - The default thread where the program starts execution.

3. start():
   - Begins thread execution.

4. join():
   - Makes the main program wait until the thread finishes.

5. current_thread():
   - Returns the currently running thread object.

Note:
-----
Python uses the Global Interpreter Lock (GIL), so threads are best for
I/O-bound tasks rather than CPU-heavy tasks.

Example:
--------
Below program creates 3 threads:
- Number Thread → Prints numbers
- Letter Thread → Prints letters
- Symbol Thread → Prints symbols

Each thread runs independently with different delays.
"""

import threading
import time


# Task 1: Print numbers
def print_numbers(delay, repeat):
    print(f"[{threading.current_thread().name}] Starting...")
    for i in range(1, repeat + 1):
        print(f"[{threading.current_thread().name}] Number: {i}")
        time.sleep(delay)
    print(f"[{threading.current_thread().name}] Finished.\n")


# Task 2: Print letters
def print_letters(delay, letters):
    print(f"[{threading.current_thread().name}] Starting...")
    for letter in letters:
        print(f"[{threading.current_thread().name}] Letter: {letter}")
        time.sleep(delay)
    print(f"[{threading.current_thread().name}] Finished.\n")


# Task 3: Print symbols
def print_symbols(delay, symbols):
    print(f"[{threading.current_thread().name}] Starting...")
    for symbol in symbols:
        print(f"[{threading.current_thread().name}] Symbol: {symbol}")
        time.sleep(delay)
    print(f"[{threading.current_thread().name}] Finished.\n")


# Extra Task: Countdown
def countdown(delay, start):
    print(f"[{threading.current_thread().name}] Starting...")
    for i in range(start, 0, -1):
        print(f"[{threading.current_thread().name}] Countdown: {i}")
        time.sleep(delay)
    print(f"[{threading.current_thread().name}] Finished.\n")


# Main Program
if __name__ == "__main__":
    print("🚀 Multithreading Program Started...\n")

    # Creating threads
    t1 = threading.Thread(
        target=print_numbers,
        args=(1, 5),
        name="Number-Thread"
    )

    t2 = threading.Thread(
        target=print_letters,
        args=(0.8, "ABCDE"),
        name="Letter-Thread"
    )

    t3 = threading.Thread(
        target=print_symbols,
        args=(0.5, "!@#$%"),
        name="Symbol-Thread"
    )

    t4 = threading.Thread(
        target=countdown,
        args=(1.2, 5),
        name="Countdown-Thread"
    )

    # Starting all threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # Waiting for all threads to complete
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("✅ All threads finished execution.")
    print("🎯 Main Thread Exiting...")