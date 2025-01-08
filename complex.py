# c=5+10j
# print(type(c))

#how to access real part of complex number
# c=5+10j
# print(c.real)               #real always returns float value
# num=c.real
# print(num)
# print(c)


#how to access imaginary part of complex numbr
# c=10+20j
# num=c.imag
# print(num)
# print(c)


# value=1010
# print(value)
# value1=0b1010
# print(value1)                     #PVM always convert the given input number into decimal number
# value2=0B1010
# print(value2)
# value3=0b1012
# print(value3)


#how to convert decimal number into binary
# num=1980
# print(bin(num))         #bin() returns the given number into binary form


#how to convert decimal number into octal
# num=137
# print(oct(num))          #oct() returns the given number into octal form


#how to convert decimal number into hexadecimal
# num=1010
# print(hex(num))



#real part must be int(binary,decimal,octal,hexadecimal) or float
# c=0b1010+5j       #binary
# print(c)        

# c=0o12+5j         #octal
# print(c)

# c=10+5j            #decimal
# print(c)

# c=0xa+5j           #hexadecimal
# print(c)

# c=10.0+5j           #float
# print(c)


#imaginary part must be decimal or float
# c=5+10j                 #decimal
# print(c)

# c=5+10.0j               #float
# print(c)

# c=5+0b1010j         # error for binary
# print(c)


# a=5+4j
# print(a.real)
# print(a.imag)