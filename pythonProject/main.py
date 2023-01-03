a = [1]
n=int(input('Введите n для формулы бинома ньютона (a+b)^n : '))

for i in range(n):
    b = [1]
    b += [a[k]+a[k+1] for k in range(len(a)-1)] + [1]
    a = b

for i in range(len(a)-1):
    a[i] = str(a[i]) + "a^" + str(n-i)

for i in range(len(a)-1):
    a[i+1] = str(a[i+1]) + "b^" + str(i+1)

s=''
for i in range(len(a)):
    s = s +a[i] + " + "
print(s[:-2])

