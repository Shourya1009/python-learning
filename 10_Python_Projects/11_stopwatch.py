import time

def main():
    print("⏱️ Simple Stopwatch")
    print("Press ENTER to start and ENTER again to stop.")
    print("Type 'quit' to exit.\n")

    while True:
        command = input("Press ENTER to start or type 'quit' to exit: ")
        if command.lower() == 'quit':
            print("Goodbye!")
            break

        print("Started... Press ENTER to stop.")
        start_time = time.time()
        input()
        end_time = time.time()

        elapsed = end_time - start_time
        minutes = int(elapsed // 60)
        seconds = elapsed % 60
        print(f"⏲️ Elapsed Time: {minutes} min {seconds:.2f} sec\n")

if __name__ == "__main__":
    main()
