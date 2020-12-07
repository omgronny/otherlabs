#task 1
s = input('Введите строку ')
w = input('Введите букву ')
s1 = ''
if w in s:  
  print(s.index(w)+1)
  k = s[-s.index(w)-1]
  for i in s:
    if i == w:
      s1 += k
    else:
      s1 += i
  print(s1)
else:
  print('Такой буквы в строке нет')
  
#task 2
s1 = [] 
n = int(input('Введите размер списка ')) 
for i in range(n): 
  p=int(input('Введите элемент списка '))
  s1.append(p)

c1=1
c2=0
for i in range(n):
  if i % 2 != 0:
    c1 *= s1[i]
  if s1[i] < 0:
    c2 += s1[i]
print(c1)
print(c2)
