import cowsay
import math

# Task no.1
#print("Hello Python")

# Task no.2
#cowsay.stegosaurus("Howdy?")

# Task no.3
with open("input.txt", "r") as file:	
	data = [current_line.rstrip() for current_line in file.readlines()]

def function(y):
	with open("output.txt", "w") as file:
		for x in y:
			file.write(x + "\t" + str(math.sin(int(x))) + "\n")

#function(data)

# Task no.4
class Product(object):
	def __init__(self, price, name, quantity):
		self.price = price
		self.name = name
		self.quantity = quantity

	def getPrice(self):
		return self.price

	def setPrice(self, price):
		self.price = price

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def getQuantity(self):
		return self.quantity

	def setQuantity(self, quantity):
		self.quantity = quantity

# I created some objects for testing
product_1 = Product('50', 'Shoes', '5')
product_2 = Product('25', 'T-shirt', '8')
product_3 = Product('100', 'Jacket', '3')

class Shop(object):
	def __init__(self):
		self.products = [product_1, product_2, product_3]
	
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
			part_price = int(obj.price)*int(obj.quantity)
			total_price += part_price
		return total_price

# I created 'Shop' object for testing and used it's functions to alter previous data
reorganize = Shop()
reorganize.buy(1)
reorganize.sell(2)

# Printing altered data to show that 'Shop' works
for obj in reorganize.products: 
	print( obj.price, obj.name, obj.quantity, sep =' ' )
print(reorganize.get_total_price())

