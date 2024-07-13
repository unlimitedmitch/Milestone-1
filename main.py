from policy_holder import Policyholder
from product import Product
from payment import Payment
from datetime import datetime, timedelta


def main():
    # Create products
    product1 = Product(1, full_name="Hospital Insurance", description="Comprehensive hospital coverage", price=100.0)
    product2 = Product(2, full_name="Life Insurance", description="Complete life insurance coverage", price=150.0)

    # Create policyholders
    policyholders = [
        Policyholder(id=1, full_name="Mitchel Joe", email="mitchel@gmail.com"),
        Policyholder(id=2, full_name="Favour Joseph", email="josephfavour@gmail.com"),
        Policyholder(id=3, full_name="Ben Johnson", email="benjohnson@rocketmail.com"),
    ]

    # add products to policyholders
    policyholders[0].add_product(product1)
    policyholders[1].add_product(product2)
    policyholders[2].add_product(product1)
    policyholders[3].add_product(product2)
    policyholders[4].add_product(product1)

    # Process payments
    due_date = datetime.now() + timedelta(days=30)  # Due date set to 30 days from now
    payments = [
        Payment(id=1, policyholder_id=1, product_id=1, amount=100.0, due_date=due_date),
        Payment(id=2, policyholder_id=2, product_id=2, amount=150.0, due_date=due_date),
        Payment(id=3, policyholder_id=3, product_id=1, amount=100.0, due_date=due_date)
    ]

    # Process all payments
    for payment in payments:
        payment.process_payment()

    # Display account details
    for policyholder in policyholders:
        print(policyholder)

    # Display payment details
    for payment in payments:
        print(payment)
        
        
if __name__ == '__main__':
    main()