""" 
Python dasturini quyidagiga yozing:
 
Foydalanuvchidan string kiritishni oling.
Ip uzunligini chop eting.
Satrni katta va kichik harflarga aylantiring. 

"""
# Foydalanuvchidan string kiritishni so'rang.
user_input =  input("Biror matn kiriting: ")

# Matnning uzunligini toping.
length_of_string = len(user_input)
print("Matnning uzunligi: ", length_of_string )

# Satrni katta va kichik harflarga aylantiring. 
uppecase_string = user_input.upper()
lowercase_string = user_input.lower()

print("Katta harflarda : ", uppecase_string)
print("kichik harflardda : ", lowercase_string)