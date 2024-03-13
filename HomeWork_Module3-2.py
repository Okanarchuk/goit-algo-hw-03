import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min < quantity < max + 1:
            return "Quantity should not be less or greater than the range."
        if min <= 1 or max <= 1000:
            return "Minumum should be greater than 1. Maximum should not exceed 1000."
        
        unique_numbers = set()
        numbers = list(range(min, max + 1))
        if quantity > len(numbers):
            return "Quantity should not exceed the range between Min and Max."  

        unique_numbers = random.sample(numbers, quantity)
        unique_numbers.sort()
        return unique_numbers
    
    except TypeError:
        return "Invalid numbers input"

lottery_numbers = get_numbers_ticket(4, 49, 600)
print("Ваші лотерейні числа:", lottery_numbers)