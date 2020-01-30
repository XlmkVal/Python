question = input("Hello, what is your name")
question = int(question)
print(type(question))
print(isinstance(question, str))
try:
    isinstance(question, str)
except False:
    print("This is not a string")
else:
    print("This is correct")
finally:
    print("Just adding a final comment")