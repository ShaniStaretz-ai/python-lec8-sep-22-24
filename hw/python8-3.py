l3: list[int] = []
MULTI_10=10
for i in range(10, 110, 10):
    l3.append(i)
print(l3)
SENTINEL:int=-999
while True:
    number: int = int(input("enter number:"))
    if number == SENTINEL:
        break;
    index = number // 10 - 1
    while l3[index] < number:
        index += 1
    l3.insert(index, number)
    print(l3)
