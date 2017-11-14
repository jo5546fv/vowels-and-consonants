def print_menu():       
    print  ("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print('q - Quit')
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
        self.name = name
        self.date = date
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
            pass#TODO:

    def get_num_items_in_cart(self):
        return len(cart_items + 1)

    def get_cost_of_cart(self):
       pass #TODO:

    def print_total(self):
        pass#TODO:

    def print_descriptions(self):
        pass#TODO:
    

if __name__ == "__main__":
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")

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

    ShoppingCart(name, date)
   
#PRINTS MENU#
while True:          
    print_menu()    
    choice = input("Choose an option: ")
     
    if choice=='a':     
        print("a - Add item to cart")
        
    elif choice=='r':
        print("r - Remove item from cart")
        
    elif choice=='c':
        print("c - Change item quantity")
       
    elif choice=='i':
        print("Output items' descriptions")
       
    elif choice=='o':
        print("Output shopping cart")
        
    elif choice=='q':
        break
    else:
        
        input("Wrong option selection. Enter any key to try again..")

  
