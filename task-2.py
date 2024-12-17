class productPriceManagement:

    def __init__(self):
        
        self.product_list = {'product_1':242}

    def newEntry(self):

        product_name = input("Enter product name: ")

        if product_name in self.product_list:
            print("Product already exists!")
            new_price = input("Enter new price...")
            self.product_list[product_name] = new_price

        else:
            product_price = input("Enter price: ")
            self.product_list[product_name] = product_price

        print(self.product_list)

product = productPriceManagement()
product.newEntry()

