#5.39. ���� ����� a1.a2...an  ���������� �� �����.
sequenceLength=int(input("������ ������������������= "))
count=0
for i in range(sequenceLength):
    userInput=int(input(f"������� {i+1} �����: "))
    count+=userInput
print(f"����� �����={count}")
