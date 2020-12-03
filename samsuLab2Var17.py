

#task 1
a=2.44
b=1.39
c=6.21
x=float(input("Введите значение х "))

y=a*x + (b*x**2 - 1)/(c*x**2 + 3)

print('y = ', y)


#task 2

n = input("Введите строку ")

print(len(n))

for i in range(5):
  print(n[-3])


#task 3
s1 = list(input())
s2 = [1, 2]
s3 = s1 + s1
print(s1)
print(s2)
print(s3)

for i in range(4,12,2):
  print(s1[i])
print(s2[0]/s2[1] - s2[0]//s2[1])
