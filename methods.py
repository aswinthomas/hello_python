class Item:
    # Class attribute. Pay rate after 20% discount
    pay_rate = 0.8
    all = []

    # Constructor. passing types is not necessary here due to default assignment
    def __init__(self, name="test", price=1., quantity=1):
        # Run validations for arguments
        assert price > 0, f"Price {price} is not greater than zero"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"Constructor called with name={self.name} price={self.price} quantity={self.quantity}")

        # Execution
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):

    # Beautify return of instance
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
