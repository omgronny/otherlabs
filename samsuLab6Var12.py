
#task 1
s = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

n = input("Введите строку ")
n1=''
for i in range(len(n)):
  if s.index(n[i]) != 31:
    n1 += s[s.index(n[i])+1]
  else:
    n1 += "а"
print(n1)

#task 2

s1 = [] 
s2 = []
n = int(input('Введите размер списка ')) 
for i in range(n): 
  p=int(input('Введите элемент списка 1 '))
  s1.append(p)
for i in range(n): #
  p=int(input('Введите элемент списка 2 '))
  s2.append(p)
c1=0
c2=1
for i in range(n):
  if i % 2 != 0:
    c1+=1
  if s2[i] < 0:
    c2 *= s2[i]
print(c1)
print(c2)
