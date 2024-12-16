# Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.
# Example:

# Input sentence: "I love apples."
# Replace: "apples"
# With: "oranges"
# Output: "I love oranges."

a = input("Matnni kiritin : ")
b = input("Matndan alishtiriladigan qismni kiriting : ")
c = input(" Yangi qismni kiriting : ")
  
d = a.replace(b,c)
print("Natija : " ,d)