class Product:
    def __init__(self, id, full_name, description, price, status='active'):
        self.id = id
        self.name = full_name
        self.description = description
        self.price = price
        self.status = status
    
    def update(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price

    def suspend(self):
        self.status = 'suspended'
        
    def reactivate(self):
        self.status = 'active'
    
    def __str__(self):
        return f"Product [ID: {self.id}, \nFull Name: {self.name}, \nDescription: {self.description}, \nPrice: {self.price}, \nStatus: {self.status}]\n"
