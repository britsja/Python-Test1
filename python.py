def check_if_even(number):
    if number % 2 == 0 and number > 0:
        return True
    else:
        return False
        
def even_number_of_evens(numbers):
    count = 0
    for number in numbers:
        if check_if_even(number):
            count += 1
    if check_if_even(count):
        return True
    else:
        return False

        
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All the tests passed")

