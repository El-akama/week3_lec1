# 26.10.20
# лекция логические операции (условные операторы)

# a = '' and ' '              # оба условия должны быть правыми
# b = '' or ' '               # хотя бы одно условние должно быть правым

# a = not True
# a = not False

# a = 5
# c = 5
# b = c is a                      # проверяет является ли объект другим объектом
# b = c is not a
# print(id(a))
# print(id(c))
# print(bool(a))
# print(bool(b))

# list_ = (0)
# print(bool(list_))

# b = '' or (0,)
# a = 2 <= 5 or not b 
# print(bool(a))


# УСЛОВНЫЕ ОПЕРАТОРЫ 

# if condition:
#     print('dfdfdfd')
# elif condition:
#     print('sdsdsddsd')
# else:
#     printt('dededede')

# students = []
# if not students:
#     print('sdsd')
# elif 'makers':
#     print('dfdf')


# grade = input('enter your mark for today: ')

# if grade.isdigit():
#     grade = int(grade)
    
#     if grade == 5:
#         print('ay youh mate it awesome')
#     elif grade == 4:
#         print('this is oke body')
#     elif grade == 3:
#         print('you have to work hard')
#     elif grade > 0:
#         print('loooser')
#     else:
#         print('there is no such mark')
# else:
#     print('enter please number')

# print('Nurbek' == 'nurbek')

# кальк - цикл

# re = "r"
# while re.lower() == "r":
#     f = input("first number: ")
#     znach = input('operation +, -, *, /: ')
#     s = input("second number: ")
#     znach1 = ["+", "-", "*", "/"]
#     if znach not in znach1:
#         print("incorrect, please enter operation + - * /")

#     if f.isdigit() and s.isdigit():
#         f = int(f)
#         s = int(s)
        
#         if znach == "+":
#             r = f + s
#             print(r)
#         elif znach == "-":
#             r = f - s
#             print(r)
#         elif znach == "*":
#             r = f * s
#             print(r)
#         elif znach == "/":
#             r = f / s
#             print(r)
        
#     else:
#         print("incorret, please print number")
#     re = input("print 'r' to conitue, or another keyboard to quit: ")


# калькудятор

# f = input("first number: ")
# znach = input('operation +, -, *, /: ')
# s = input("second number: ")
# znach1 = ["+", "-", "*", "/"]
# if znach not in znach1:
#     print("incorrect, please enter operation + - * /")

# if f.isdigit() and s.isdigit():
#     f = int(f)
#     s = int(s)
    
#     if znach == "+":
#         r = f + s
#         print(r)
#     elif znach == "-":
#         r = f - s
#         print(r)
#     elif znach == "*":
#         r = f * s
#         print(r)
#     elif znach == "/":
#         r = f / s
#         print(r)

# else:
#     print("incorret, please print number")
