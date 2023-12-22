greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "John"

intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name) #Helps to change what we put in name

print(intrupution, formatted)
print(formatted.upper())
print(formatted.lower())
print(formatted.replace("John", "Paul"))