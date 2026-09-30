from bank import Bank
from transaction import transfer_funds
from validation import get_valid_float

def display_menu():
    print("\n--- CLI Banking Simulator ---")
    print("1. Create Account")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Transfer Funds")
    print("5. View Account Statement")
    print("6. Exit")
    print("-----------------------------")

def main():
    my_bank = Bank()

    while True:
        display_menu()
        choice = input("Select an option (1-6): ")

        if choice == '1':
            acc_num = input("Enter new account number: ")
            name = input("Enter account holder name: ")
            pin = input("Set a 4-digit PIN: ")
            initial_deposit = get_valid_float("Enter initial deposit amount: ₹")
            
            success, msg = my_bank.create_account(acc_num, name, pin, initial_deposit)
            print(msg)

        elif choice == '2':
            acc_num = input("Enter account number: ")
            account = my_bank.get_account(acc_num)
            if account:
                amount = get_valid_float("Enter deposit amount: ₹")
                success, msg = account.deposit(amount)
                print(msg)
            else:
                print("Account not found.")

        elif choice == '3':
            acc_num = input("Enter account number: ")
            account = my_bank.get_account(acc_num)
            if account:
                pin = input("Enter your PIN: ")
                amount = get_valid_float("Enter withdrawal amount: ₹")
                success, msg = account.withdraw(amount, pin)
                print(msg)
            else:
                print("Account not found.")

        elif choice == '4':
            sender_num = input("Enter your account number: ")
            sender = my_bank.get_account(sender_num)
            if sender:
                receiver_num = input("Enter receiver account number: ")
                receiver = my_bank.get_account(receiver_num)
                if receiver:
                    pin = input("Enter your PIN: ")
                    amount = get_valid_float("Enter transfer amount: ₹")
                    success, msg = transfer_funds(sender, receiver, amount, pin)
                    print(msg)
                else:
                    print("Receiver account not found.")
            else:
                print("Sender account not found.")

        elif choice == '5':
            acc_num = input("Enter account number: ")
            account = my_bank.get_account(acc_num)
            if account:
                pin = input("Enter your PIN to view statement: ")
                if account.pin == pin:
                    print(f"\n--- Statement for {account.holder_name} ---")
                    print(f"Current Balance: ₹{account.balance:.2f}")
                    print(f"{'Date':<20} | {'Type':<25} | {'Amount'}")
                    print("-" * 60)
                    for txn in account.get_statement():
                        print(f"{txn['date']:<20} | {txn['type']:<25} | ₹{txn['amount']:.2f}")
                else:
                    print("Incorrect PIN.")
            else:
                print("Account not found.")

        elif choice == '6':
            print("Thank you for using the CLI Banking Simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()