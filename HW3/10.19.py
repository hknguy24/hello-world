class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(
            self.item_price * self.item_quantity))

    def print_item_description(self):
        print(self.item_description)

class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'none', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemsToPurchase):
        #print('ADD ITEM TO CART')
        #item_name = input('Enter the item name:\n')
        #item_description = input('Enter the item description:\n')
        #item_price = int(input('Enter the item price:\n'))
        #item_quantity = int(input('Enter the item quantity:\n'))
        #newitem = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        self.cart_items.append(ItemsToPurchase)

    def remove_item(self):
        print('REMOVE ITEM FROM CART')
        rem_item = input('Enter name of item to remove:\n')
        i = 0
        found = 1
        for item in self.cart_items:
            if (item.item_name == rem_item):
                self.cart_items.remove(item)
                return
        print('Item not found in cart. Nothing removed.')

    def output_cart(self):
        print('OUTPUT SHOPPING CART')
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print('Number of Items: ' + str(self.get_num_items_in_cart()) + '\n')
        total = 0
        for item in self.cart_items:
            print(item.item_name + " " + str(item.item_quantity) + " @ $" + str(item.item_price) + " = $" + str(
                item.item_price * item.item_quantity))
            total = total + (item.item_quantity * item.item_price)

        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
            print("\nTotal: $" + str(total))
        else:
            print("\nTotal: $" + str(total))

    def modify_item(self):
        print('CHANGE ITEM QUANTITY')
        itemname = input("Enter the item name:\n")
        itemquantity = int(input('Enter the new quantity:\n'))
        found = 1
        for item in self.cart_items:
            if (item.item_name == itemname):
                item.item_quantity = itemquantity
                break
            else:
                found = 0
        if found == 0:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        itemcount = 0
        for item in self.cart_items:
            itemcount = itemcount + item.item_quantity

        return itemcount

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            cost = (item.item_price * item.item_quantity)
            total = total + cost

        return total

    def print_total(self):
        total = self.get_cost_of_cart()
        if (total > 0):
            self.output_cart()
        else:
            print('SHOPPING CART IS EMPTY')

    def print_description(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(self.customer_name + "'s Shopping Cart - " + self.current_date, end='\n')
        print("\nItem Descriptions")

        for item in self.cart_items:
            print(item.item_name + ": " + item.item_description)

def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")
        option = input("Choose an option:\n")
        while (option != 'a' and option != 'o' and option != 'i' and option != 'r' and option != 'c' and option != 'q'):
            option = input('Choose an option:\n')
        if option == 'a':
            print('ADD ITEM TO CART')
            item_name = input('Enter the item name:\n')
            item_description = input('Enter the item description:\n')
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            newitem = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(newitem)
        elif option == 'r':
            cart.remove_item()
        elif option == 'c':
            cart.modify_item()
        elif option == 'i':
            cart.print_description()
        elif option == 'o':
            cart.output_cart()
        elif option == 'q':
            break


if __name__ == "__main__":
    customer = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print("\nCustomer name: " + customer)
    print("Today's date: " + date)
    cart = ShoppingCart(customer, date)
    print_menu(cart)