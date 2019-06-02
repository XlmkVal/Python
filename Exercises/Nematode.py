class Nematode:
    def __init__(self, length, gender, age):
        self.length = length
        self.gender = gender 
        self.age = age
    def __repr__(self):
        return "{0}{1}{2}".format(self.length.__repr__, self.gender.__repr__, self.age.__repr__)
    def __str__(self):
        return "{0}{1}{2}".format(self.length, self.gender, self.age)

nem = Nematode(1, "male", 25)

print(repr(nem))