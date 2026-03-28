def main():
    print("Welcome to the Lotto Simulator!")
    
    while True:
        spielzahlen = input("Choose 5 numbers from 1 to 50 to play (separated by spaces): ")
        spielzahlen = spielzahlen.split()
        
        # Validate input
        if len(spielzahlen) != 5:
            print("You must choose exactly 5 numbers. Try again.")
            continue
        
        valid_numbers = []
        invalid_entries = []
        
        for n in spielzahlen:
            try:
                number = int(n)
                if 1 <= number <= 50:
                    valid_numbers.append(number)
                else:
                    invalid_entries.append(n)
            except ValueError:
                invalid_entries.append(n)
        
        if len(valid_numbers) != 5:
            if invalid_entries:
                print(f"Invalid entries: {', '.join(invalid_entries)}. All numbers must be between 1 and 50.")
            else:
                print("All entries must be numbers. Try again.")
            continue
        
        print(f"You have chosen the numbers: {valid_numbers}")
        break  # Exit the loop if valid numbers are chosen

if __name__ == "__main__":
    main()
