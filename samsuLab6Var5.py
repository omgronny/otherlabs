
#task 1

s=input('Введите строку ')                       #вводим втроку
p=int(input('Введите целое число '))       #вводим число

summ=0  #объявили счетчик для подсчёта количества вхождений буквы в строку
for i in s:
  if i == s[p]:  # если очередная буква (элемент) строки равна нашей, то увелияиваем сумму 
    summ = summ + 1
print('Буква "',s[p], '" встречается в строке ', summ, ' раз') # просто вывод


#task 2
s = [] # заводим список
n = int(input('Введите размер списка ')) # вводим размер списка с клавиатуры 
for i in range(n): # цикл по n
  p=int(input('Введите элемент списка '))
  s.append(p) # вводим с клавиатуры элемент и сохраняем его в массив
  
print(s)
print ("длин наименьшей оси равна  ", max(s) - min(s)) # длина наименьшей оси это просто разница между минимумальным и максимумальным элементом в массиве