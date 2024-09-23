l3: list[int] = []
MULTI_10 = 10
SENTINEL: int = -999
for i in range(MULTI_10, MULTI_10 ** 2 + MULTI_10, MULTI_10):
    l3.append(i)
print(l3)

while True:
    number: int = int(input("Enter number:"))
    if number == SENTINEL:
        break;
    index = number // MULTI_10 - 1
    while l3[index] < number:
        index += 1
    l3.insert(index, number)
    print(l3)
