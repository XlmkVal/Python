'''301'''


class Books:
	def __init__(self, name, author, price):
		self.name = name
		self.author = author
		self.price = price
	
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, val):
		self._name = val

	@property
	def author(self):
		return self._author
	@author.setter
	def author(self, val):
		self._author = val
		
	@property
	def price(self):
		return self._price
	@price.setter
	def price(self, val):
		self._price = val
		
		
books = Books("New world", "John Doe", 12354)

print(books.author)

l = ["first", "", "second"]

for item in l:
	if item.strip():
		print(item)
		