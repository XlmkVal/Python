temp =[("Sofia", 34),("Berlin", 23),("London", 14)]

'''def convertToFar(country: str, temperatureC: float):
    """ Input is in Celsius and the Output is in Fahrenheid"""
    return 9.0/5.0*float(temperatureC) + 32
x = None
y = None
'''
convertToFar = lambda data: (data[0], (9.0/5.0)*data[1] + 32)
print(list(map(convertToFar, temp)))
