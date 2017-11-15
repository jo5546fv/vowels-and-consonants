class cellphone:

    def __init__(self, manufact, model, retail_price):
        self.manufact = manufact
        self.model = model
        self.retail_price = retail_price

    def set_manufact(self, manufact):
        self.manufact = manufact

    def set_model(self, model):
        self.model = model

    def set_retail_price(self, retail_price):
        self.retail_price = retail_price

    def get_manufact(self):
        return self.manufact()

    def get_model(self):
        return self.model()

    def get_retail_price(self):
        return self.retail_price

phone = cellphone(
    input('Enter the manufacturer: '),
    input('Enter the model number: '),
    float(input('Enter the retail price: ')))

print('Here is the data that you entered:')
print('Manufacturer: %s' % phone.manufact)
print('Model Number: %s' % phone.model)
print('Retail Price: %.2f' % phone.retail_price)
