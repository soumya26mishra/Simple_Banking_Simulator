# Simple Banking Simulator CLI

## Overview
The Simple Banking Simulator is a purely terminal-based application designed to manage basic financial operations. It allows users to simulate core banking activities such as creating accounts, managing balances, and securely transferring funds without the need for an external database or heavy graphical interfaces. 

## Features
* **Account Management:** Register new accounts with unique account numbers and secure 4-digit PINs.
* **Core Transactions:** Process deposits and authenticated withdrawals.
* **Fund Transfers:** Securely transfer money between two existing accounts.
* **Auditing:** Generate and view formatted chronological account statements.
* **Robust Validation:** Prevents application crashes from invalid user inputs (e.g., entering text instead of numbers).

## Technologies Used
* Python 3.x (Built-in libraries only: `datetime`)

## Installation & Execution
This project requires no external dependencies or installations other than Python 3. 

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/banking-simulator.git](https://github.com/your-username/banking-simulator.git)
2. **Navigate to the project directory:**
   ```Bash
   cd banking-simulator
3. **Run the application:**
   ```Bash
    python3 main.py
    (Note: Depending on your system configuration, you may need to use python main.py)

## Instructions for Testing

To evaluate the system, follow these steps in the CLI menu:
Press 1 to create an account (e.g., Account 101, PIN 1234, Initial Deposit 5000).
Press 1 again to create a second account (e.g., Account 102, PIN 0000, Initial Deposit 0).
Press 2 to test a deposit on Account 101. Enter a non-numeric character to test the error handling.
Press 4 to transfer 1000 from Account 101 to Account 102. You will be prompted for Account 101's PIN.
Press 5 to view the statement for Account 102 to verify the transferred funds appear correctly.
Press 6 to safely exit the application.

