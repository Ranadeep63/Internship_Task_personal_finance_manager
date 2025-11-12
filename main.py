from user_auth import UserAuth
from user import FinanceManager
from report import ReportGenerator

def main():
    auth = UserAuth()

    print("=== Welcome to Personal Finance Manager ===")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()
            auth.register(username, password)

        elif choice == "2":
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            if auth.login(username, password):
                fm = FinanceManager(username)
                while True:
                    print(f"\n=== {username}'s Dashboard ===")
                    print("1. Add Transaction")
                    print("2. View Transactions")
                    print("3. Delete Transaction")
                    print("4. Generate Report")
                    print("5. Plot Category Report")
                    print("6. Logout")

                    option = input("Enter choice: ").strip()

                    if option == "1":
                        category = input("Category: ").strip()
                        amount = input("Amount: ").strip()
                        ttype = input("Type (income/expense): ").lower().strip()
                        desc = input("Description: ").strip()
                        fm.add_transaction(category, amount, ttype, desc)

                    elif option == "2":
                        fm.view_transactions()

                    elif option == "3":
                        t_id = input("Enter Transaction ID to delete: ").strip()
                        fm.delete_transaction(t_id)

                    elif option == "4":
                        report = ReportGenerator(f"finance_{username}.json")
                        report.generate_summary()
                        report.category_report()

                    elif option == "5":
                        report = ReportGenerator(f"finance_{username}.json")
                        report.plot_category_report()

                    elif option == "6":
                        print("🚪 Logged out successfully.")
                        break
                    else:
                        print("Invalid option. Try again.")

        elif choice == "3":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
