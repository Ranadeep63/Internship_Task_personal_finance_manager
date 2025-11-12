import json
from collections import defaultdict

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except Exception:
    MATPLOTLIB_AVAILABLE = False

class ReportGenerator:
    def __init__(self, filename="finance_data.json"):
        with open(filename, 'r') as f:
            self.data = json.load(f)

    def generate_summary(self):
        total_income = sum(t["Amount"] for t in self.data if t["Type"] == "income")
        total_expense = sum(t["Amount"] for t in self.data if t["Type"] == "expense")
        balance = total_income - total_expense
        print("\n=== Summary Report ===")
        print(f"Total Income: ₹{total_income}")
        print(f"Total Expense: ₹{total_expense}")
        print(f"Net Balance: ₹{balance}")

    def category_report(self):
        category_summary = defaultdict(float)
        for t in self.data:
            category_summary[t["Category"]] += t["Amount"]
        print("\n=== Category-wise Report ===")
        for cat, amt in category_summary.items():
            print(f"{cat}: ₹{amt}")
        return category_summary

    def plot_category_report(self):
        if not MATPLOTLIB_AVAILABLE:
            print("Matplotlib not installed. Install it with `pip install matplotlib`.")
            return

        category_summary = self.category_report()
        if not category_summary:
            print("No data to plot.")
            return

        cats = list(category_summary.keys())
        amts = [category_summary[c] for c in cats]

        plt.figure(figsize=(8,5))
        plt.bar(cats, amts)
        plt.xticks(rotation=45, ha='right')
        plt.title("Category-wise Spending")
        plt.ylabel("Amount (₹)")
        plt.tight_layout()
        plt.show()
