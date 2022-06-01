def running_sums(numbers):
    new_numbers = []
    # sums = 0

    for idx in range(len(numbers)):
        summed_element = sum(numbers[:idx + 1])
        new_numbers.append(summed_element)

    return new_numbers

"""TIM SOLUTION"""
def running_sums(numbers):
    sums = []

    current_sum = 0
    for number in numbers:
        current_sum += number
        sums.append(current_sum)

    return sums