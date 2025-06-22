import datetime

class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance, account_type, interest_rate, overdraft_limit):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
        self.account_type = account_type
        self.interest_rate = interest_rate
        self.overdraft_limit = overdraft_limit
        self.account_status = "Active"  # Initialize account as active
        self.transactions = []  # Initialize empty transactions list

    # Methods to get customer details
    def get_full_name(self):
        """Get the full name of the customer."""
        return f"{self.fname} {self.lname}"

    def get_first_name(self):
        """Get the first name."""
        return self.fname

    def get_last_name(self):
        """Get the last name."""
        return self.lname

    def get_address(self):
        """Get the address."""
        return self.address

    def get_account_no(self):
        """Get the account number."""
        return self.account_no

    def get_balance(self):
        """Get the account balance."""
        return self.balance

    def get_account_type(self):
        """Get the type of account."""
        return self.account_type

    def get_interest_rate(self):
        """Get the interest rate."""
        return self.interest_rate

    def get_overdraft_limit(self):
        """Get the overdraft limit."""
        return self.overdraft_limit

    def get_customer_details(self):
        """Return a dictionary of customer details."""
        return {
            "Full Name": self.get_full_name(),
            "Account Number": self.account_no,
            "Balance": self.balance,
            "Account Type": self.account_type,
            "Interest Rate": self.interest_rate,
            "Overdraft Limit": self.overdraft_limit,
            "Address": self.address
        }

    # Methods to update customer details
    def update_first_name(self, fname):
        """Update first name."""
        self.fname = fname
    
    def update_last_name(self, lname):
        """Update last name."""
        self.lname = lname

    def update_address(self, addr):
        """Update address."""
        self.address = addr
    
    def update_customer_name(self, new_first_name, new_last_name):
        """Update the customer's full name."""
        self.update_first_name(new_first_name)
        self.update_last_name(new_last_name)

    def update_customer_address(self, new_address):
        """Update the customer's address."""
        self.update_address(new_address)

    # Methods for account transactions
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraws the specified amount from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
    
    def print_balance(self):
        """Print account balance."""
        print(f"Account Balance: {self.balance:.2f}")
    
    def print_details(self):
        """Display all customer details."""
        print(f"Account Number: {self.account_no}")
        print(f"Full Name: {self.get_full_name()}")
        print(f"Address: {self.address}")
        print(f"Balance: {self.balance:.2f}")

    # Account menu and operations
    def account_menu(self):
        """Display available options for the account holder."""
        print("\nYour Transaction Options Are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Deposit money")
        print("2) Withdraw money")
        print("3) Check balance")
        print("4) Update customer name")
        print("5) Update customer address")
        print("6) Show customer details")
        print("7) Back")
        option = int(input("Choose your option: "))
        return option
    
    def run_account_options(self):
        """Run the account menu loop."""
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                amount = float(input("\nEnter deposit amount: "))
                try:
                    self.deposit(amount)
                    print(f"Deposited {amount}. New balance: {self.get_balance():.2f}")
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == 2:
                amount = float(input("\nEnter withdrawal amount: "))
                try:
                    self.withdraw(amount)
                    print(f"Withdrew {amount}. New balance: {self.get_balance():.2f}")
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == 3:
                self.print_balance()
            elif choice == 4:
                new_first_name = input("Enter new first name: ")
                new_last_name = input("Enter new last name: ")
                self.update_customer_name(new_first_name, new_last_name)
                print(f"Updated name: {self.get_full_name()}")
            elif choice == 5:
                new_address = input("Enter new address: ")
                self.update_customer_address(new_address)
                print(f"Updated address: {self.address}")
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
        print("\nExiting account operations")

    def close_account(self):
        """Mark account as closed"""
        self.account_status = "Closed"
        return True

    def is_active(self):
        """Check if account is active"""
        return self.account_status == "Active"

    def get_transaction_history(self):
        """Return list of recent transactions"""
        return self.transactions

    def record_transaction(self, transaction_type, amount):
        """Record a transaction"""
        transaction = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": amount,
            "balance": self.balance
        }
        self.transactions.append(transaction)

    # Enhanced deposit and withdraw methods
    def deposit(self, amount):
        """Deposit money into account with validation"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        if not self.is_active():
            raise ValueError("Cannot deposit to closed account")
        self.balance += amount
        self.record_transaction("Deposit", amount)
        return self.balance

    def withdraw(self, amount):
        """Withdraw money from account with validation"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if not self.is_active():
            raise ValueError("Cannot withdraw from closed account")
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit")
        self.balance -= amount
        self.record_transaction("Withdrawal", -amount)
        return self.balance