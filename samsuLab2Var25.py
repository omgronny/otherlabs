#task 1

a=1.93
b=3.48
c=0.27
x=float(input("Введите значение х ")) # Вводим значение 
y=(a*x+b*x**2)/(x+c*x**4) # Формула из варианта 
print('y = ', y) # Выводим значение 

# task 2

x=input("Введите строку ") # Вводим строку 
print('Длина строки = ', len(x)) # Выводим длину строки 
print(x[2:15:4]) # Выводим элементы согласно заданию 

#task 3

stroka=input("Введите строку ") # вводим строку 
spisok1=list(stroka) # делаем список из этой строки 
spisok2=[] 
x1=float(input('Введите первое число '))
spisok2.append(x1)
x2=float(input('Введите второе число ')) # Вводим числа и добавляем их в список
spisok2.append(x2)
spisok3=spisok1+spisok2 # объединяем списки 
print(spisok1)
print(spisok2)
print(spisok3) # выводим списки подряд 
print(spisok1[5:15:3]) # выводим первый список согласно заданию 
print(spisok2[0]//spisok2[1]) # выводим результат деления
