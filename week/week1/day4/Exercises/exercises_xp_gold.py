#Exercise 1: Bank Account
#Part I AND Part III

class BankAccount:
    def __init__(self, username, password):
        self.balance = 0
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, entered_username, entered_password):
        if self.username == entered_username and self.password == entered_password:
            self.authenticated = True
            print("Authentication successful!")
            return True
        print("Authentication failed.")
        return False

    def _check_authenticated(self):
        if not self.authenticated:
            raise Exception("Authentication required. Please log in first.")

    def deposit(self, amount):
        self._check_authenticated()
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Deposit amount must be a positive number.")
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        self._check_authenticated()
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive number.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

#Part II : Minimum balance account

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, minimum_balance=0):
        super().__init__(username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        self._check_authenticated()
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive number.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Withdrawal failed. Minimum balance of ${self.minimum_balance} must be maintained.")
        
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

#Part IV: BONUS Create an ATM class

class ATM:
    def __init__(self, account_list, try_limit):
        if not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("Invalid account list. Must contain BankAccount or MinimumBalanceAccount instances.")
        
        try:
            try_limit = int(try_limit)
            if try_limit <= 0:
                raise ValueError
        except (ValueError, TypeError):
            print("Invalid try limit. Setting to default of 2.")
            try_limit = 2
        
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            choice = input("\n--- Main Menu ---\n1. Log In\n2. Exit\nEnter your choice: ")
            if choice == "1":
                self.log_in()
            elif choice == "2":
                print("Thank you for using our ATM. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please enter 1 or 2.")
    
    def log_in(self):
        while self.current_tries < self.try_limit:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            for account in self.account_list:
                if account.authenticate(username, password):
                    print("Login successful!")
                    self.show_account_menu(account)
                    return
            
            self.current_tries += 1
            print(f"Invalid username or password. You have {self.try_limit - self.current_tries} tries remaining.")
        
        print("Maximum number of login attempts reached. Shutting down.")
        sys.exit()

    def show_account_menu(self, account):
        while True:
            print(f"\nWelcome, {account.username}!")
            choice = input("--- Account Menu ---\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\nEnter your choice: ")

            if choice == "1":
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except Exception as e:
                    print(f"Error: {e}")
            
            elif choice == "2":
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "3":
                print(f"Your current balance is: ${account.balance}")
            
            elif choice == "4":
                account.authenticated = False  # Log out
                print("Logging out. Returning to main menu.")
                return
            
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    account1 = BankAccount("john_doe", "password123")
    account2 = MinimumBalanceAccount("jane_smith", "securepass", minimum_balance=50)

    accounts = [account1, account2]
    

    atm = ATM(accounts, 3)