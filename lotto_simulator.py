
def main():  
    print("Welcome to the Lotto Simulator!")
    valid_numbers = False
    while not valid_numbers:
        spielzahlen = input("Choose 5 numbers from 1 to 50 to play: ")
        spielzahlen = spielzahlen.split()
        counter_valid_numners = 0
        for n in spielzahlen:
                try:
                    int(n)
                except ValueError:
                    print(f"All entries must be numbers. Try again. '{n}' is not valid.")
                    continue
                if int(n) >= 1 and int(n) <= 50:
                    counter_valid_numners += 1
                else:
                    print(f"All numbers must be between 1 and 50. Try again. '{n}' is not valid.")
        if counter_valid_numners != 5:
            print("You must choose exactly 5 valid numbers. Try again.")        
        else:
            valid_numbers = True
    
    print(f"You have chosen the numbers: {spielzahlen}")
if __name__ == "__main__":
    main()
