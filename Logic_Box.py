print("Welcome to Pattern Generator and Number Analyzer!!")
print("\nThis program generate patterns as pr user input.")
print("This program labeled number as odd and even number in given range.")

while True:
    print("\nSelect an option:")
    print("1. Generate a pattern.")
    print("2. Analyze a range of numbers.")
    print("3. Exit.")

    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1:
            n = int(input("\nEnter a number of rows:"))
            print("\nPatern:")
            for i in range(1,n+1):
                for j in range(1,i+1):
                    print("*", end =" ")

                print()

        case 2:
            start = int(input("Enter starting number of range: "))
            end = int(input("Enter ending number of range: "))

            if start > end:
                print("Starting value should be greater than ending value...")
                continue

            sum = 0 
            for i in range(start, end+1):
                if i%2 == 0:
                    print(f"Number {i} is Even")
                else:
                    print(f"Number {i} is Odd")
                
                sum += i
            print(f"Sum of all numbers from {start} to {end} is : {sum}")

        case 3:
            print("Exiting the program. Goodbye!!")
            break

        case _:
            print("Invalid input...")