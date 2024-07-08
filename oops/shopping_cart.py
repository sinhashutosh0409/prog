class Shopping:

    items = {"apple":5, "orange":4, "papaya":9}
    price = {"apple":1000, "orange":500, "papaya":700}

    def __init__(self):
        self.cart = []

    def add_item(self,product,quantity):
        if product not in Shopping.items.keys():
            raise Exception("item not found")
        if quantity > Shopping.items[product]:
            raise Exception("out of stock")
        item = {"product":product, "quantity":quantity, "price":Shopping.price[product]}
        self.cart.append(item)
        Shopping.items[product] = Shopping.items[product] -1

cart1 = Shopping()
print(cart1.add_item("apple",1))
print(cart1.add_item("orange",1))
print(cart1.add_item("papaya",1))
print(cart1.add_item("apple",2))
print(cart1.cart)
print(Shopping.items)




