#5.30. �����:
#�) ����� ����� ���� ����� ����� �� 20 �� 40;
#�) ����� ��������� ���� ����� ����� �� a �� 50 (�������� a �������� � ����������; 0 a 50);
#�) ����� ��������� ���� ����� ����� �� 1 �� n (�������� n �������� � ����������; 1 n 100);
#�) ����� ��������� ���� ����� ����� �� a �� b (�������� a � b �������� � ����������; b a).


# A
count = 0
for i in range(40):
    count = count + i ** 3
print(f'����� ���� ����� �� 20 �� 40 = {count}')


# B
a = int(input("������� �: "))
while 0>a or a>50:
    print(f"Error. Correct Input 50 >= a >= 0:")
    a = int(input("Insert a: "))

count = 0
while a <= 50:
    count = count + i ** 2
    a = a + 1
print(f'C���� ��������� ���� ����� ����� �� a �� 50= {count}')



#V
n = int(input('������� n:'))
while n<1 or n>100:
    print(f"Error. Correct Input 1<=n<=100:")
    n = int(input("Insert n: "))


j = 0
s = 0
while j < n:
    square = (j + 1) ** 2
    s = s + square
    j = j + 1

print(f"����� ��������� ���� ����� �����  {s}")



#G
a = int(input("Insert a: "))
b = int(input("Insert b: "))
while b < a:
    print(f"Error b<a")
    b = int(input("Insert b: "))
c = 0

for i in range(a, b+1):
    c += i**2
    print(c)







