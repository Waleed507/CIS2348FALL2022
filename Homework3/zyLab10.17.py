# Waleed Yusuf
# 2104654

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.cost = 0

    def print_item_cost(self):
        self.cost = self.item_price*self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.cost}')


if __name__ == "__main__":
    print('Item 1')
    name1 = str(input("Enter the item name:\n"))
    price1 = int(input("Enter the item price:\n"))
    quantity1 = int(input("Enter the item quantity:\n"))
    print()

    print('Item 2')
    name2 = str(input("Enter the item name:\n"))
    price2 = int(input("Enter the item price:\n"))
    quantity2 = int(input("Enter the item quantity:\n"))
    print()

    print('TOTAL COST')
    purchase_item1 = ItemToPurchase(name1, price1, quantity1)
    purchase_item2 = ItemToPurchase(name2, price2, quantity2)
    purchase_item1.print_item_cost()
    purchase_item2.print_item_cost()

    total = purchase_item1.cost + purchase_item2.cost
    print(f'\nTotal: ${total}')
