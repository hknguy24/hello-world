# Huy Kevin Nguyen
# PSID: 1346435

class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
            print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(
                self.item_price * self.item_quantity))

if __name__ == "__main__":
    print("Item 1")
    name1 = input("Enter the item name:\n")
    price1 = int(input("Enter the item price:\n"))
    quantity1 = int(input("Enter the item quantity:\n"))
    item1 = ItemToPurchase()
    item1.item_name = name1
    item1.item_price = price1
    item1.item_quantity = quantity1
    print("\nItem 2")
    name2 = input("Enter the item name:\n")
    price2 = int(input("Enter the item price:\n"))
    quantity2 = int(input("Enter the item quantity:\n"))
    item2 = ItemToPurchase()
    item2.item_name = name2
    item2.item_price = price2
    item2.item_quantity = quantity2
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print("\nTotal: $" + str(total))
