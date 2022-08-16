#5.47. Даны числа a1.a2 ... an Определить их произведение.


sequenceLength=int(input("Длинна последоватеьлности= "))
count=1
for i in range(sequenceLength):
    userInput=int(input(f"введите {i+1} число: "))
    count*=userInput
print(f"произведение чисел={count}")
