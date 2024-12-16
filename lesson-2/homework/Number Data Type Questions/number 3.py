# Kilometrlarni metr va santimetrga aylantiruvchi dastur tuzing.

S = float(input('Masofani kiriting : ')) # kilomerlarda

masofa_metr = S*1000 # metrlarda 
masofa_santimetr = S*100_000 # santimetrlarda

print(str(masofa_metr) + ' metr')
print(str(masofa_santimetr) + ' santimetr')