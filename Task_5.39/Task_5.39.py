#5.39. Даны числа a1.a2...an  определить их сумму.
sequenceLength=int(input("Длинна последоватеьлности= "))
count=0
for i in range(sequenceLength):
    userInput=int(input(f"введите {i+1} число: "))
    count+=userInput
print(f"сумма чисел={count}")
