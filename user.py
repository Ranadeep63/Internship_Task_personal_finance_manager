from transaction import Transaction
from data_manager import DataManager
from datetime import datetime

class FinanceManager:
    def __init__(self, username):
        self.username = username
        self.data_manager = DataManager(f"finance_{self.username}.json")
        self.transactions = self.data_manager.load_data()

    def add_transaction(self, category, amount, type, description=""):
        if type not in ("income", "expense"):
            print("Type must be 'income' or 'expense'. Transaction not added.")
            return
        try:
            amount = float(amount)
        except ValueError:
            print("Amount must be a number. Transaction not added.")
            return

        t_id = 1
        if self.transactions:
            existing_ids = [t.get("Transaction ID", 0) for t in self.transactions]
            t_id = max(existing_ids) + 1

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = Transaction(t_id, date, category, amount, type, description)
        self.transactions.append(transaction.to_dict())
        self.data_manager.save_data(self.transactions)
        print("✅ Transaction added successfully!")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return
        for t in self.transactions:
            print(f"{t['Transaction ID']}. {t['Date']} | {t['Type']} | {t['Category']} | ₹{t['Amount']} | {t['Description']}")

    def delete_transaction(self, t_id):
        try:
            t_id = int(t_id)
        except ValueError:
            print("Please provide a valid integer Transaction ID.")
            return
        before = len(self.transactions)
        self.transactions = [t for t in self.transactions if t.get('Transaction ID') != t_id]
        if len(self.transactions) < before:
            self.data_manager.save_data(self.transactions)
            print("🗑️ Transaction deleted successfully!")
        else:
            print("Transaction ID not found.")
