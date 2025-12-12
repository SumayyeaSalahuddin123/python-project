def sum(a,b):
    return a + b

def difference(a,b):
    return a - b

def product(a,b):
    return a * b

def quotient(a,b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

a = 10
b = 5   
print("Sum:", sum(a, b))
print("Difference:", difference(a, b))
print("Product:", product(a, b))
print("Quotient:", quotient(a, b))
print("This is a demo script.")