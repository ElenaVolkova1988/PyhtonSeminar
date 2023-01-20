# Создайте словарь, по формуле 3*n+1, где n это ключ, а формула значение
# my_dict ={}
# number = int(input('Введите целое число '))
# for n in range (1,number+1):
#     my_dict[n]= 3*n+1    
# print(my_dict)    
# Если нужно вывести отдельно какой то ключ, то
# print(my_dict.get(7))  
# Работа со строками 
# my_string= " Питон самый лучший язык в мире" 
# split- распиливает строку по по заданному элементу
# my_string=my_string.split('и')
# print(my_string)
# replace заменяет символ, на тот который укажем
# my_string=my_string.replace('и', '$')
# print(my_string)
# startswith не нужно переприсваивать, можно сразу через печать
# либо правдаБлибо ложь
# Спрашиваем есть ли строки, начинающие с ПИТ
# print(my_string.startswith(" Пит"))
# склейка только строчных элементов  join
# my_list =['1','2', '34', '5', '6', '7', '8']
# # print(' '.join(my_list))
# # либо для склейки в принте не ковычки пустые ставить, а объявить переменную и ее в принт
# glue = ''
# print(glue.join(my_list))
# Найдите корни квадратного уравнения Ax**2+Bx+C=0
# equation = '3*x**2 + 5*x - 6=0'
# a=3
# b=5
# c= -6
# equation=equation.replace('*x**2','')
# equation=equation.replace('*', '')
# equation=equation.replace('x', '')
# equation=equation.replace('=0', '')
# equation=equation.rstrip()
# equation= equation.split(' ')
# print(equation)
# a = int(equation[0])
# b = int(equation[2])
# c = int(equation[4])
# if equation [2]== '-':
#     b*=-1
# if equation [3]== '-':
#     c*=-1    
# print(a,b,c)

# dis = b**2-4*a*c 

# if dis < 0 :
#     print ('решения нет')
# elif dis == 0:
#     print (-(b/(2*a)))
# else:
#     x1 = round( (-b+(dis)**0.5)/(2*a) )     
#     x2 = round((-b-(dis)**0.5)/(2*a))
#     print (f'x1 = {x1}, x1 = {x2}')  
equation = '3*x**2 + 5*x - 6 = 0'
def create_koef(equation: str): # передаем в строковый формат
    new_equation=equation.replace(' ', "").replace('=0', '').replace( '+', ' ').replace('-', ' -') # убрали пробелы, убрали 0.Дальше  + меняем на пробел, а - на пробел минус
    new_equation= new_equation.split()
    new_list=[]
    for item in new_equation:
        if item.startswith('x'):
            new_list.append(1)
        elif item.startswith('-x'):
            new_list.append(-1)  
        else:
            new_list.append(item.split('*x')[0])    
    print(new_list) 
create_koef(equation)