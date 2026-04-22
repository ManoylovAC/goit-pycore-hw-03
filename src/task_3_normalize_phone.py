import re


def normalize_phone(phone_number: str) -> str:
    '''
    The function normalizes the phone number to the standard format: +38xxxxxxxxxx.

    Args:
        phone_number (str): The phone number to be normalized.

    Returns:
        str: The normalized phone number. 
    '''

    ukr_code = '38'
    non_digits_pattern = r'\D'

    cleaned_number = re.sub(non_digits_pattern, '', phone_number)
    prefix = '+' if cleaned_number.startswith(f'{ukr_code}0') else f'+{ukr_code}' 
    normalized_number = f'{prefix}{cleaned_number}'

    return normalized_number


if __name__ == '__main__':
    raw_numbers = [
        '067\\t123 4567',
        '(095) 234-5678\\n',
        '+380 44 123 4567',
        '380501234567',
        '    +38(050)123-32-34',
        '     0503451234',
        '(050)8889900',
        '38050-111-22-22',
        '38050 111 22 11   ',
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print('Нормалізовані номери:', '\n'.join(sanitized_numbers))
