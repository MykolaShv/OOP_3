class Product:
    def __init__(self, name: str, price: int, unit: float, _purchased):
        self.name = name
        self.price = price
        self.unit = unit
        self._purchased = True

    def __str__(self) -> str:
        return self.name

    def __float__(self) -> float:
        return self.get_total() / 100

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.price == other.price and self.unit == other.unit

    def get_total(self, quantity: int | float = None) -> int:
        if quantity:
            return int(round(quantity * self.price / self.unit, 0))
        else:
            return self.price


class ShoppingCart:
    def __init__(self):
        self.products = []
        self.quantities = []
        self.index = 0

    def __float__(self) -> float:
        return self.get_total() / 100

    def __eq__(self, other) -> bool:
        return self.products == other.products and self.quantities == other.quantities

    def add_product(self, product: Product, quantity: int | float = None) -> None:
        quantity = quantity or product.unit
        if product not in self.products:
            self.products.append(product)
            self.quantities.append(quantity)
        else:
            index_product = self.products.index(product)
            self.quantities[index_product] += quantity

    def __getitem__(self, key) -> tuple:
        return self.products[key].__str__(), self.quantities[key]

    def __len__(self) -> int:
        return len(self.products)

    def __iter__(self):
        return zip(self.products, self.quantities)

    def remove_product(self, product: Product) -> None:
        if product in self.products:
            index_product = self.products.index(product)
            self.products.remove(product)
            del self.quantities[index_product]
        else:
            print('Sorry, we have not such product')

    def sub_product(self, product: Product, quantity: int | float = None):
        index_product = self.products.index(product)
        self.quantities[index_product] -= quantity
        if self.quantities[index_product] <= 0:
            self.remove_product(product)
        else:
            print('Зменшили суму')

    def get_total(self) -> float:
        return sum([self.products[i].price*self.quantities[i]/self.products[i].unit\
                    for i in range(self.__len__())])


class PaymentValidator:
    def is_valid(self):
        return True if self.is_valid else False


class PaymentProcessor:
    def purchase(self):
        'XXXXXX'


class CashPaymentValidator(PaymentValidator):
    def is_valid(self):
        return True


class CodeValidator(PaymentValidator):
    def __init__(self, security_code):
        self.security_code = security_code

    def is_valid(self):
        client_code = input('Please, input your code')
        return client_code == self.security_code


class CashPaymentProcessor(CashPaymentValidator, PaymentProcessor):
    def purchase(self, _purchased):
        self.is_valid()
        print('Обробка готівкового платежу')
        print('Загальна сума оплати становить :', ShoppingCart.__float__(_purchased))


class CardPaymentProcessor(CodeValidator, PaymentProcessor):
    def purchase(self, _purchased):
        self.is_valid()
        print('Обробка платежу карткою')
        print('Код безпеки :', self.security_code)


if __name__ == '__main__':
    candy = Product("candy", 1059, 0.1, 1)
    sweet = Product("candy", 1059, 0.1, 1)
    juice = Product("juice", 3655, 1, 1)
    cart = ShoppingCart()
    cart.add_product(candy, 0.75)
    cart.add_product(sweet, 0.75)
    cart.add_product(juice, 3)
    print(len(cart))
    print(cart[0])
    for cart_item, purchase in zip(cart, ((candy, 1.5), (juice, 3))):
         print('cart_item == purchase', cart_item == purchase)
    cart.remove_product(candy)
    print(len(cart))
    cart.sub_product(juice, 2)
    print(cart[0][1])
    cart.sub_product(juice, 2)
    print(not cart)

    # cart = ShoppingCart()
    # cart.add_product(Product("juice", 3655, 1, 1))
    # cash_processor = CashPaymentProcessor()
    # cash_processor.purchase(cart)
    # card_processor = CardPaymentProcessor("1234")
    # card_processor.purchase(cart)
    # print(ShoppingCart.__float__(cart))
    # candy = Product("candy", 1059, 0.1)
    # sweet = Product("candy", 1059, 0.1)
    # juice = Product("juice", 3655, 1)
    # cart_1 = ShoppingCart()
    # cart_2 = ShoppingCart()
    # cart_3 = ShoppingCart()
    # cart_1.add_product(candy, 1)
    # cart_1.add_product(sweet, 0.5)
    # cart_2.add_product(juice)
    # print(cart_1.get_total())
    # print(cart_2.get_total())
    # print(str(candy))
    # print(float(candy))
    # print(float(cart_2))
    # print('candy == sweet', candy == sweet)
    # print('sweet != juice', sweet != juice)
    # print('cart_1 == cart_2', cart_1 == cart_2)
    # print('cart_2 has products: ', bool(cart_2))
    # print('cart_3 has products: ', bool(cart_3))




