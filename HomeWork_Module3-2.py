import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min < quantity < max + 1:
            return "Quantity should not be less or greater than the range."
        unique_numbers = set()
        numbers = list(range(min, max + 1))
    except TypeError:
        return "Invalid numbers input"
    
    unique_numbers = random.sample(numbers, quantity)
    unique_numbers.sort()
    return unique_numbers

lottery_numbers = get_numbers_ticket(4, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)