# Write a program that counts the number of vowels and consonants in a given string.

def unli_harf_soni(matn):
    unli_harflar = "aeiouAEIOU"
    hisob = 0
    for harf in matn:
        if harf in unli_harflar:
           hisob += 1
    return hisob
matn = input("Enter a string : ")
natija = unli_harf_soni(matn)
print(natija)