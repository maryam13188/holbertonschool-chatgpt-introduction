#!/usr/bin/python3
"""
checkbook.py - Simple checkbook application with error handling
Fixed version: Prevents crashes from invalid input
"""

class Checkbook:
    def __init__(self):
        """Initialize checkbook with zero balance"""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.
        
        Args:
            amount (float): Positive amount to deposit
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook.
        
        Args:
            amount (float): Positive amount to withdraw
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
        
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Display current balance"""
        print("Current Balance: ${:.2f}".format(self.balance))


def get_positive_float(prompt):
    """
    Safely get a positive float number from user input.
    
    Args:
        prompt (str): The prompt to display to user
    
    Returns:
        float or None: Valid positive float, or None if input invalid
    """
    try:
        value = float(input(prompt))
        if value <= 0:
            print("Error: Amount must be positive.")
            return None
        return value
    except ValueError:
        print("Error: Please enter a valid number.")
        return None


def main():
    """Main function to run checkbook application"""
    cb = Checkbook()
    print("Welcome to the Checkbook Application!")
    print("=" * 40)
    
    while True:
        print("\nAvailable actions: deposit, withdraw, balance, exit")
        action = input("What would you like to do? ").lower().strip()
        
        if action == 'exit':
            print("Thank you for using the checkbook. Goodbye!")
            break
        
        elif action == 'deposit':
            amount = get_positive_float("Enter the amount to deposit: $")
            if amount is not None:
                cb.deposit(amount)
        
        elif action == 'withdraw':
            amount = get_positive_float("Enter the amount to withdraw: $")
            if amount is not None:
                cb.withdraw(amount)
        
        elif action == 'balance':
            cb.get_balance()
        
        else:
            print("Invalid command. Please choose from: deposit, withdraw, balance, exit")


if __name__ == "__main__":
    main()
