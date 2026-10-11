# True va False

# >, <, ==, <=, >=, !=
# ==  tengmi?

a = 5
b = 10
print(a == b)  # False
print(a != b)  # True

# Truthy va Falsy

print(bool(0))
print(bool(1))
print(bool("Stringlar uchun"))
print(bool(""))
print(bool("asdf"))

print("Booleanlar uchun")
print(bool(True))
print(bool(False))

print("Container data typelar uchun")
print(bool([]))
print(bool([1, 2]))
print(bool({}))
print(bool({"key": "value"})) # Empty dictionary
print(bool({1, 2, 3}))

print("-"*50)
print(bool(" "))