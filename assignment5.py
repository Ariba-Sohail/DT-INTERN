class Customer:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def display_details(self):
        print(f"Name: {self.name}, Address: {self.address}, Phone: {self.phone_number}, Email: {self.email}")


class Account:
    def __init__(self, account_number, account_type, balance, customer):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount.")

    def display_account_info(self):
        print(f"Account Number: {self.account_number}, Type: {self.account_type}, Balance: {self.balance}")
        self.customer.display_details()


class SavingsAccount(Account):
    def display_account_info(self):
        print(f"Savings Account Number: {self.account_number}, Balance: {self.balance}")
        self.customer.display_details()


class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_account(self, account):
        self.accounts.append(account)

    def display_customers(self):
        for customer in self.customers:
            customer.display_details()

    def display_accounts(self):
        for account in self.accounts:
            account.display_account_info()


# Example usage
if __name__ == "__main__":
    bank = Bank("Example Bank")
    customer1 = Customer("John Doe", "123 Main St", "1234567890", "johndoe@example.com")
    account1 = SavingsAccount(12345, "Savings", 1000, customer1)

    bank.add_customer(customer1)
    bank.add_account(account1)

    bank.display_customers()
    bank.display_accounts()

    account1.deposit(500)
    account1.withdraw(200)
    account1.display_account_info()
