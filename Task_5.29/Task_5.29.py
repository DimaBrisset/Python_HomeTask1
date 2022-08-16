#а) среднее арифметическое всех целых чисел от 1 до 1000;
#б) среднее арифметическое всех целых чисел от 100 до b (значение b вводится с клавиатуры; b 100);
#в) среднее арифметическое всех целых чисел от a до 200 (значения a и b вводятся с клавиатуры; a 200);
#г) среднее арифметическое всех целых чисел от a до b (значения a и b вводятся с клавиатуры; b a).

#a  
count=0
for x in range(1001):
   # print(x+1)
    count+=x
print(f"Среднее арифметическое: {count/1000}")



#b
b = int(input("Insert b: "))
while (b<100):
    print(f"Error b<0")
    b = int(input("Insert b: "))
c = 0
for i in range(100, b+1):
    c += i
c /= b - 100 + 1
print(c)




#v
a = int(input("Insert a: "))
while a > 200:
    print(f"Error a>200")
    a = int(input("Insert a: "))
b = 200
c = 0
for i in range(a, b + 1):
    c += i
c /= b - a + 1
print(c)





#G
a = int(input("Insert a: "))
b = int(input("Insert b: "))
while b < a:
    print(f"Error b<a")
    b = int(input("Insert b: "))
c = 0
for i in range(a, b + 1):
    c += i
c /= b - a + 1
print(c)
