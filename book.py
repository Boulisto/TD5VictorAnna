class Book:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.id = 1

    def insert_buy(self, quantities, prices):
        order = Order(True, quantities, prices, self.id)
        self.id += 1
        res = '---insert ' + str(order) + ' on ' + self.name + '\n'
        if not self.execute(order, ''):
            self.orders.append(order)
        else:
            res += 'Execute ' + str(order.quantities) + ' at ' + str(order.prices) + ' on ' + self.name + '\n'
        print(res + str(self))

    def insert_sell(self, quantities, prices):
        order = Order(False, quantities, prices, self.id)
        self.id += 1
        res = '---insert ' + str(order) + ' on ' + self.name + '\n'
        test = self.execute(order, '')
        if not test:
            self.orders.append(order)
        else:
            res += test
        print(res + str(self))

    def execute(self, order, restr):
        quant = None
        orders = sorted(self.orders, key=lambda x: x.prices, reverse=True)
        if order.buy:
            for i in orders:
                if order.prices >= i.prices and order.buy ^ i.buy:
                    if order.quantities <= i.quantities:
                        i.quantities -= order.quantities
                        restr += 'Execute ' + str(order.quantities) + ' at ' + str(i.prices) + ' on ' + self.name + '\n'
                    else:
                        quant = min(i.quantities, order.quantities)
                        temp = i.quantities
                        i.quantities = 0
                        self.quantitynull()
                        restr += 'Execute ' + str(quant) + ' at ' + str(i.prices) + ' on ' + self.name + '\n'
                        restr = self.execute(Order(True, abs(temp - order.quantities), order.prices, self.id), restr)

                    self.quantitynull()
                    return restr
        if not order.buy:
            for i in orders:
                if order.prices <= i.prices and order.buy ^ i.buy:
                    if order.quantities <= i.quantities:
                        i.quantities -= order.quantities
                        restr += 'Execute ' + str(order.quantities) + ' at ' + str(i.prices) + ' on ' + self.name + '\n'
                    else:
                        quant = min(i.quantities, order.quantities)
                        temp = i.quantities
                        i.quantities = 0
                        self.quantitynull()
                        restr += 'Execute ' + str(quant) + ' at ' + str(i.prices) + ' on ' + self.name + '\n'
                        restr = self.execute(Order(False, abs(temp - order.quantities), order.prices, self.id), restr)
                    self.quantitynull()
                    return restr
        self.quantitynull()
        return False

    def quantitynull(self):
        tab = []
        for i in range(len(self.orders)):
            if self.orders[i].quantities == 0:
                tab.append(i)
        for i in range(len(tab) - 1, -1, -1):
            self.orders.pop(tab[i])

    def __str__(self):
        res = 'Book on ' + self.name + '\n'
        orders = sorted(self.orders, key=lambda x: x.prices, reverse=True)
        for i in orders:
            res += '    ' + str(i) + '\n'

        return res


class Order:
    def __init__(self, buy, quantities, prices, identifier):
        self.buy = buy
        self.quantities = quantities
        self.prices = prices
        self.id = identifier

    def __str__(self):
        return str('BUY ' + str(self.quantities) + "@" + str(self.prices) + ' id=' + str(
            self.id) if self.buy else 'SELL ' + str(self.quantities) + "@" + str(self.prices) + ' id=' + str(self.id))

