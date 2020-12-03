
#task 1

s=input('Введите строку ')                       
p=int(input('Введите целое число '))       

summ=0  
for i in s:
  if i == s[p]:  
    summ = summ + 1
print('Буква "',s[p], '" встречается в строке ', summ, ' раз') 


#task 2
s = [] 
n = int(input('Введите размер списка ')) 
for i in range(n): 
  p=int(input('Введите элемент списка '))
  s.append(p) 

k = 1  
p=int(input('Введите целое число '))
for i in range(n):
  if s[i] > p:
    k*=s[i]
print(k)

