# Policy Management System

This project implements a Policy Management System using Python classes to manage policyholders, products, payments, and their interactions.

## Features

- **Policyholder Management**: Create, suspend, and reactivate policyholders.
- **Product Management**: Create, update, suspend products.
- **Payment Management**: Process payments, send reminders, apply penalties.
- **Demonstration**: Create policyholders, assign products, process payments, and display account details.

## Files

- **policyholder.py**: Defines the `Policyholder` class for managing policyholders.
- **product.py**: Defines the `Product` class for managing products.
- **payment.py**: Defines the `Payment` class for managing payments.
- **main.py**: Showcases the functionality.

## Thought Process

The assignment required creating a robust system to manage policyholders, products, and payments with specific functionalities:

1. **Class Creation**: Separate classes (`Policyholder`, `Product`, `Payment`) were created to encapsulate related functionalities and data.
   
2. **Policyholder Management**: Methods for registering, suspending, and reactivating policyholders were implemented to manage their status dynamically.

3. **Product Management**: The `Product` class included methods for creating, updating, suspending products, ensuring flexibility in managing product offerings.

4. **Payment Management**: The `Payment` class was designed to handle payment processing, reminders, and penalties, ensuring timely management of financial transactions.

5. **Demonstration**: A demonstration script (`main.py`) was developed to showcase the system's capabilities by creating policyholders, assigning products, processing payments, and displaying account details.

### Classes Overview

- **Policyholder Class**: Manages policyholder information and product assignments.
- **Product Class**: Manages product details and status (active or suspended).
- **Payment Class**: Handles payment processing, reminders, and penalties.