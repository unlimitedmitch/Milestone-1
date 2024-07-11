class Policyholder:
    def __init__(self, id, full_name, email, status='active'):
        self.id = id
        self.name = full_name
        self.email = email
        self.status = status
        self.products = []

    def add_product(self, product):
        self.products.append(product)
    
    def suspend(self):
        self.status = 'suspended'
    
    def reactivate(self):
        self.status = 'active'

    def __str__(self):
        products_str = ', '.join([str(product) for product in self.products])
        return f"Policyholder [ID: {self.id}, \nFull Name: {self.name}, \nEmail: {self.email}, \nStatus: {self.status}, \nProducts: {products_str}]\n"
