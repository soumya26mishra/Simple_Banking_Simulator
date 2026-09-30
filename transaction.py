def transfer_funds(sender_account, receiver_account, amount, sender_pin):
    # First, attempt to withdraw from sender
    success, message = sender_account.withdraw(amount, sender_pin)
    if not success:
        return False, f"Transfer failed: {message}"
    
    # If successful, deposit to receiver
    receiver_account.deposit(amount)
    
    # Update the transaction logs to reflect it was a transfer, not a standard deposit/withdrawal
    receiver_account.transactions[-1]["type"] = f"Transfer from {sender_account.account_number}"
    sender_account.transactions[-1]["type"] = f"Transfer to {receiver_account.account_number}"
    
    return True, "Transfer complete."