class Country:
	def __init__(self, name, population, area):
		self.name = name
		self.population = population
		self.area = area
	def __str__(self):
		return "{0} has a population of {1} and total area of{2}".format(self.name, self.population, self.area)
	def __repr__(self):
		print("{0}[{1}, {2}, {3}]".format(Country, self.name, self.population, self.area))
		
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, val):
		self._name = val
		
	def is_larger(self, second):
		if self.area > second.area:
			return "{0} is larger".format(self.name)
		elif self.area == second.area:
			return "{0} and {1} are equal in size".format(self.name, second.name)
		else:
			return "{0} is smaller".format(self.name)
			
	def population_density(self):
		return self.population / self.area
		
# country = Country("Bulg", 120000, 123000)
# print(country.name)

# country2 = Country("canada", 123454, 123000)
# print(country.is_larger(country2))
# print(country2.population_density())
# print(country2)
# print(country2.__repr__())