from statistics import mean

l2: list[float] = [];
count_2_above = 0;
SENTINEL: int = -999
MIN_HEIGHT: float = 1.60
MAX_HEIGHT: float = 3.0
while True:
    height: float = float(input("Enter height:"))

    if height == SENTINEL:
        break;
    if height < MIN_HEIGHT or height > MAX_HEIGHT:
        continue;

    if height > 2.0:
        count_2_above += 1;
    l2.append(height)
print("total:", len(l2))
print("l2:", l2)
if l2:
    print("highest:", max(l2))
    print("shortest:", min(l2))
    print("higher than 2.0 m:", count_2_above)
    print("avg:", mean(l2))

count_mean: int = 0;
avg:float=mean(l2)
for i in range(len(l2)):
    if l2[i] > avg:
        count_mean += 1

print(f"higher than average:{count_mean}")
