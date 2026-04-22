import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    '''
    The function generates a sorted list of unique random numbers in a given range.

    Args:
        min (int): The minimum value for the range of numbers, not less than 1.
        max (int): The maximum value for the range of numbers, not more than 1000.
        quantity (int): The number of unique numbers to generate within the range (min, max).

    Returns:
        list: A sorted list of unique random numbers within the specified range.

    Raises:
        TypeError: if type min, max, quantity not int
    '''

    if type(min) != int or type(max) != int or type(quantity) != int:
        raise TypeError(f'All input values must be a integers, but your type is {type(min)}, {type(max)}, {type(quantity)}')

    if min < 1 or max > 1000 or quantity > max or quantity > max - min + 1:
        return []
    
    range_min_max_numbers = range(min, max + 1)
    random_numbers = random.sample(range_min_max_numbers, quantity)
    sorted_random_numbers = sorted(random_numbers)
      
    return sorted_random_numbers


if __name__ == '__main__':
    lottery_numbers = get_numbers_ticket(20, 50, 6)
    print('Ваші лотерейні числа:', lottery_numbers)
