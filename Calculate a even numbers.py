list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [1, 6, 3, 7, 5, 9, 7, 10, 9, 10]
list_3 = [1, 9, 3, 4, 4, 6, 7, 11, 9, 10]
list_4 = [1, 2, 6, 5, 6, 6, 7, 13, 9, 10]

def sum_even_numbers(list):
    sum_even = 0
    for number in list:
        if number % 2 == 0:
            sum_even += number
    return sum_even

list_1 = [1, 2, 3, 4]
print(sum_even_numbers(list_1)) # choose list_#




