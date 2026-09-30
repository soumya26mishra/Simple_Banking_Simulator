import datetime

class Account:
    def __init__(self, account_number, holder_name, pin, initial_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.pin = pin
        self.balance = float(initial_balance)
        self.transactions = []  # List of dictionaries to store history
        
        if self.balance > 0:
            self._record_transaction("Initial Deposit", self.balance)

    def _record_transaction(self, description, amount):
        # Uses Module 4 string formatting for the timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append({
            "date": timestamp, 
            "type": description, 
            "amount": amount, 
            "balance": self.balance
        })

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._record_transaction("Deposit", amount)
            return True, "Deposit successful."
        return False, "Amount must be greater than zero."

    def withdraw(self, amount, entered_pin):
        # Module 8 Control flow for validation
        if entered_pin != self.pin:
            return False, "Incorrect PIN."
        if amount <= 0:
            return False, "Amount must be greater than zero."
        if amount > self.balance:
            return False, "Insufficient funds."
        
        self.balance -= amount
        self._record_transaction("Withdrawal", amount)
        return True, "Withdrawal successful."

    def get_statement(self):
        return self.transactions