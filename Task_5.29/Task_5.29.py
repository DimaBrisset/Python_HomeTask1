#�) ������� �������������� ���� ����� ����� �� 1 �� 1000;
#�) ������� �������������� ���� ����� ����� �� 100 �� b (�������� b �������� � ����������; b 100);
#�) ������� �������������� ���� ����� ����� �� a �� 200 (�������� a � b �������� � ����������; a 200);
#�) ������� �������������� ���� ����� ����� �� a �� b (�������� a � b �������� � ����������; b a).

#a  
count=0
for x in range(1001):
   # print(x+1)
    count+=x
print(f"������� ��������������: {count/1000}")



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
