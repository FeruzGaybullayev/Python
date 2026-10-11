# Case sensitive vs Case insensetive

fruit = "apple banana"
user = "Feruz gaybullayev"
print("Original:", fruit)

print(fruit.lower())
print(fruit.upper())
print(fruit.capitalize())
print(fruit.title())
print(user.title())

print(fruit.endswith('b'))
print(fruit.startswith('A'))
print(fruit.startswith('a'))

print('-'*50)
word = '     Hello World     '
print(word)
print(word.strip())

fruits = 'apple banana cherry'
print(fruits.split(" "))

print('-'*50)

file_name = "numeric.py"
base_name = file_name.split('.')[0]
extension = file_name.split('.')[1]

print(f"{file_name =}")