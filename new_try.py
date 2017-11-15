
cart_items = []
def print_menu():       
    print  ("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print('q - Quit')

class ItemToPurchase:
    
    def __init__(self, item_name, item_price, item_quanity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quanity
        
    def print_item_cost(self):
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity,
        self.item_price, (self.item_quantity * self.item_price)))

    def print_description(self):
        print('%s: %s'% (self.item_name, self.item_description))

if __name__ == "__main__":
    
    name = input('enter name:')
    date = input('enter date:')
    
    print('Item 1')
    item1 = ItemToPurchase(input('Enter the item name:\n'),float(input('Enter the item price:\n')),int(input('Enter the item quantity:\n')))
    
    print('\nItem 2')
    item2 = ItemToPurchase(input('Enter the item name:\n'),float(input('Enter the item price:\n')),int(input('Enter the item quantity:\n')))
    
    print('\nTOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    
    print('\nTotal: $%d' % ((item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)))


class ShoppingCart:
   def __init__(self, date, name):
       self.date = date
       self.name = name
       self.total = 0
       self.items = []

   def add_item(self, item_name, quantity, price):
       self.total += price*quantity
       cart_items.append(self.total)

   
#PRINTS MENU#
while True:          
    print_menu()    
    choice = input("Choose an option: ")
     
    if choice=='a':
        newitem = ShoppingCart(date,name)
        newitem.add_item(input('New item name:'),int(input('Quanity:')),int(input('Price')))
    
        print(cart_items)
        
    elif choice=='r':
        print("r - Remove item from cart")
        
    elif choice=='c':
        print("c - Change item quantity")
       
    elif choice=='i':
        print("Output items' descriptions")
       
    elif choice=='o':
        print("Output shopping cart")
        ##For TESTING
        print(cart_items)
        
    elif choice=='q':
        break
    else:
        input("Wrong option selection. Enter any key to try again..")


