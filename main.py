import cowsay
import math

# Task no.1
#print("Hello Python")

# Task no.2
#cowsay.stegosaurus("Howdy?")

# Task no.3
def function():
	with open("input.txt", "r") as file:	
		data = [current_line.rstrip() for current_line in file.readlines()]
	with open("output.txt", "w") as file:
		for x in data:
			file.write(x + "\t" + str(math.sin(int(x))) + "\n")

#function()

# Task no.4
# Task no.5
# Added methods __str__() in both classes and __len__() in class Shop()
# iterator() not working
class Product(object):
	def __init__(self, name, price, quantity):
		self.name = name
		self.price = price
		self.quantity = quantity

	def __str__(self):
		return 'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'.format(self = self)

	def getPrice(self):
		return self.price

	def setPrice(self, price):
		if int(price) <= 0:
			print('Price cannot be <= 0')
		else:
			self.price = price

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def getQuantity(self):
		return self.quantity

	def setQuantity(self, quantity):
		if int(quantity) <= 0:
			print('Quantity cannot be <= 0')
		else:
			self.quantity = quantity

# I created some objects for testing
product_1 = Product('Shoes', '50', '5')
product_2 = Product('T-shirt', '25', '8')
product_3 = Product('Jacket', '100', '3')

class Shop(object):
	def __init__(self):
		self.products = [product_1, product_2, product_3]

	def __str__(self):
		for obj in self.products:
			X = obj.name
			Y = obj.price
			Z = obj.quantity
		return '\nName\tPrice\tQuantity\n{X}\t{Y}\t{Z}'.format(X = X, Y = Y, Z = Z)
	
	def __len__(self):
		total_amount = 0
		for obj in self.products:
			total_amount += int(obj.getQuantity())
		return print('\nTotal amount of products: ' + str(total_amount))

	def buy(self, product):
		a = int(self.products[product].getQuantity())
		a += 1
		return self.products[product].setQuantity(str(a))

	def sell(self, product):
		a = int(self.products[product].getQuantity())
		a -= 1
		return self.products[product].setQuantity(str(a))

	def get_total_price(self):
		total_price = 0
		part_price = 0

		for obj in self.products:
			part_price = int(obj.getPrice())*int(obj.getQuantity())
			total_price += part_price
		return print('\nTotal price of products: ' + str(total_price))

	# Code is not giving errors, when iterator() used nothing happens
	def __iter__(self):
		return self

	def __next__(self):
		this_elem = products[idx]
		idx = (idx + 1) % len(products)
		next_elem = products[idx]

	def iterator(self, name):
		iter_list = self.products.__iter__()
		
		if iter_list != name:
			try:
				iter_list.__next__()
			except:
				return print('Cannot find!')
		else:
			return print('Found it!')


# I created 'Shop' object for testing and used it's functions to alter previous data
# and to show that everything works

reorganize = Shop()
reorganize.buy(1)
reorganize.sell(2)
print(reorganize)
reorganize.get_total_price()
reorganize.__len__()

# Unlike __str__ method in Shop prints all products properly, worth to keep around
# for obj in reorganize.products: 
#	 print( obj.name, obj.price, obj.quantity, sep =' ' )

