print("Welcome to the Bill Splitter App!")

while True:
    try:
        bill_amount = float(input("\nEnter total bill amount: "))
        if bill_amount < 0:
            print("Error: Bill amount cannot be negative.")
            continue

        num_people = int(input("Enter number of people: "))
        if num_people <= 0:
            print("Error: Number of people must be greater than zero.")
            continue

        tip_percent = int(input("Enter tip percentage (0,5,10,15,20): "))
        if tip_percent not in [0,5,10,15,20]:
            print("Error: Tip must be one of these values: 0,5,10,15,20")
            continue

        tip_amount = (tip_percent / 100) * bill_amount
        final_bill = bill_amount + tip_amount
        per_person = final_bill / num_people
        GST_amount = final_bill %  18
            
        print("\n----- Bill Summary -----")
        print(f"Total Bill Amount   : ${bill_amount:.2f}")
        print(f"Tip Amount ({tip_percent}%) : ${tip_amount:.2f}")
        print(f"Final Bill Amount   : ${final_bill:.2f}")
        print(f"Amount Per Person   : ${per_person:.2f}")
        print(f"GST_amount          : ${GST_amount:.2f}")

    except ValueError:
        print("Invalid input. Please enter correct number formats.")
        continue

    again = input("\nDo you want to split another bill? (y/n): ")
    if again != 'y':
        print("Thank you for using the Bill Splitter App!")
        break
