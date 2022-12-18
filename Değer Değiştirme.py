print("Değer Değiştirci")

a =int(input("sayı 1:"))
b =int(input("sayı 2:"))

temp = a
a = b
b = temp

print("sayı 1: {} \nsayı 2: {}\n".format(a,b))
