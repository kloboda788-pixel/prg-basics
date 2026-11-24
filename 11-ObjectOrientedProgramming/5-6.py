###
# Main program using the BankAccount class
#
import bank_account

def main():
    # 1. Create a bank account
    account = bank_account.BankAccount('12 3456 5555 9090 1111 0000 7722')
    # 2. Display account balance
    account.display()
    # 3. Deposit PLN 25,30
    account.deposit(25.30)
    # 4. Display account balance
    account.display()
    # 5. Withdraw PLN 31,70 - more than the balance
    account.withdraw(31.70)
    # 6. Display account balance
    account.display()
    # 7. Withdraw PLN 14
    account.withdraw(14)
    # 8. Display account balance
    account.display()

if __name__ == "__main__":
    main()