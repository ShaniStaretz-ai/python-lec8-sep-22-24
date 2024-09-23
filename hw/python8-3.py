l3: list[int] = []
MULTI_10 = 10
SENTINEL: int = -999
for i in range(MULTI_10, MULTI_10 ** 2 + MULTI_10, MULTI_10):
    l3.append(i)
print(l3)

while True:
    number: int = int(input("Enter number:"))
    if number == SENTINEL: #break point
        break;
    index = number // MULTI_10 - 1  # since the values are in multiples 10,
    while l3[index] < number:  # find the right index
        index += 1
    l3.insert(index, number) #when find the right index add to the list
    print(l3)
