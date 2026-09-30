from account import Account

class Bank:
    def __init__(self):
        # Uses Module 7 Dictionaries to store all accounts in memory
        self.accounts = {} 

    def create_account(self, account_number, name, pin, initial_deposit):
        if account_number in self.accounts:
            return False, "Error: Account number already exists."
        
        new_account = Account(account_number, name, pin, initial_deposit)
        self.accounts[account_number] = new_account
        return True, "Account created successfully!"

    def get_account(self, account_number):
        # Returns the Account object if found, otherwise None
        return self.accounts.get(account_number, None)