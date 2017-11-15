class ItemToPurchase:
    
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = 'none'
    
    def print_item_cost(self):
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity,
        self.item_price, (self.item_quantity * self.item_price)))

    def print_item_description(self):
        print('%s:%s' % (self.item_name, self.item_description))

class ShoppingCart:

    def __init__(self, name, date):
        self.customer_name = 'none'
        self.current_date = 'January 1, 2016'
        cart_items = []

    def add_item(self):
        cart_items = cart_items.append(self.item_name)

    def remove_item(self):
        if self.item_name in cart_items:
            cart_items = cart_items.remove(self.item_name)
        else:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self):
        if self.item_name in cart_items:
            self.item_quantity = int(input('Enter the new quantity:'))
        else:
            print('Item not found in cart. Nothing removed.')

    def get_num_items_in_cart(self):
        return len(cart_items + 1)

    def get_cost_of_cart(self):
        total = 0
        for i in cart_items:
            total += i.item_price
        return total
        
    def print_total(self,total):
        if len(cart_items) >= 0:
            print("%s's Shopping Cart - %s" % (self.customer_name, self.current_date))
            print("Number of Items: %d\n" % self.get_num_items_in_cart())
            for i in cart_items:
                print('%s %d @ $%d = $%d' % (i.item_name, i.item_quantity,
                i.item_price, (i.item_quantity * i.item_price)))
            else:
                print('\nTotal: $%d' % self.get_cost_of_cart())
        else:
            print('SHOPPING CART IS EMPTY')

    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print("%s's Shopping Cart - %s\n" % (self.customer_name, self.current_date))
        print('Item Descriptions')
        for i in cart_items:
            print('%s: %s' % (self.item_name, self.item_description))

def print_menu:
    while True:
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print('q - Quit\n')
        option = input('Choose an option:\n')
        #this is where i am fuck this code jesus christ


if __name__ == "__main__":
    print('Item 1')
    item1 = ItemToPurchase()
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = float(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    
    print('\nItem 2')
    
    item2 = ItemToPurchase()
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = float(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))
    
    print('\nTOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    
    print('\nTotal: $%d' % ((item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)))
