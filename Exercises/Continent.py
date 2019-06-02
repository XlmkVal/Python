import Country

class Continent:
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, val):
        self._name = val
        
    def total_population(self):
        sum = 0
        for i in self.countries:
            sum +=i.population
        print(sum)
    
canada = Country.Country('Canada', 34482779, 9984670)
usa = Country.Country('United States of America', 313914040, 9826675)
mexico = Country.Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)

north_america.name
for country in north_america.countries:
    print(country)
north_america.total_population()