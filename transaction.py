class Transaction:
    def __init__(self, t_id, date, category, amount, type, description=""):
        self.t_id = t_id
        self.date = date
        self.category = category
        self.amount = amount
        self.type = type  # 'income' or 'expense'
        self.description = description

    def to_dict(self):
        return {
            "Transaction ID": self.t_id,
            "Date": self.date,
            "Category": self.category,
            "Amount": self.amount,
            "Type": self.type,
            "Description": self.description
        }
