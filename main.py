import random

random_list = [random.randint(-10, 10) for _ in range(10)]
print("Random list:", random_list)

first_positive_index = -1
for i in range(len(random_list)):
    if random_list[i] > 0:
        first_positive_index = i
        break

last_positive_index = -1
for i in range(len(random_list) - 1, -1, -1):
    if random_list[i] > 0:
        last_positive_index = i
        break

if first_positive_index != -1 and last_positive_index != -1:
    sum_between_positives = sum(random_list[first_positive_index + 1:last_positive_index])
    print("The sum of the elements between the first and last positive elements:", sum_between_positives)
else:
    print("The list contains no positive items or less than two.")
