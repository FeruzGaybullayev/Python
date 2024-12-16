x = float(input('Birinchi raqamni kiriting: '))
y = float(input('Ikkinchi raqamni kiriting: '))
z = float(input('Uchinchi raqamni kiriting: '))

if  0 <= x <= 9 and 0 <= y <= 9 and 0 <= z <= 9: 

    m = str(min(x, y, z))
    n = str(max(x, y, z))

    print("Eng kichik son: " + m)
    print("Eng katta son: " + n)

else:
    print('Error: Raqamlar (0, 9) oralig\'ida bo\'ladi')