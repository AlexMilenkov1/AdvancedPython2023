def find_sums(*args):
    negative_num_sums = 0
    positive_num_sums = 0

    for number in args[0]:
        if number < 0:
            negative_num_sums += number
        else:
            positive_num_sums += number

    return positive_num_sums, negative_num_sums


numbers = [int(x) for x in input().split()]

sums = find_sums(numbers)

print(sums[1])
print(sums[0])
if sums[0] > abs(sums[1]):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')
