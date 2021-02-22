class Book:
	def __init__(self, name): 
		self.name=name
		self.orders=[]

	def insert_buy(self, quantities, prices):
		self.orders.append(Order(True, quantities, prices))
	def insert_sell(self, quantities, prices):
		self.orders.append(Order(False, quantities, prices))

class Order:
	def __init__(self, buy, quantities, prices):
		self.buy=buy
		self.quantities=quantities
		self.prices=prices
