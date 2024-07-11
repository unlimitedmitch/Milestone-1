from datetime import datetime

class Payment:
    def __init__(self, id, policyholder_id, product_id, amount, due_date, date=None):
        self.id = id
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount
        self.due_date = due_date
        self.date = date
        self.paid = False
    
    def process_payment(self):
        self.paid = True
    
    def send_reminder(self):
        if not self.paid and datetime.now() > self.due_date:
            print(f"Reminder: Payment of {self.amount} for Policyholder ID: {self.policyholder_id} is overdue.")
    
    def apply_penalty(self, penalty_amount):
        if not self.paid and datetime.now() > self.due_date:
            self.amount += penalty_amount
            print(f"Penalty applied. New amount: {self.amount}")
    
    def __str__(self):
        return f"Payment [ID: {self.id}, \nPolicyholder ID: {self.policyholder_id}, \nProduct ID: {self.product_id}, \nAmount: {self.amount}, \nDue Date: {self.due_date}, \nPaid: {self.paid}]\n"