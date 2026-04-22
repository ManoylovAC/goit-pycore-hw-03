from datetime import datetime
import re


def get_days_from_today(date: str) -> int:
    '''
    The function calculates the number of days from the entered date to the current day.
    
    Args:
        days (str): date in format 'YYYY-MM-DD'
    
    Returns:
        int: count of days from input date to current today

    Raises:
        TypeError: if type date not str
        ValueError: if date not match format 'YYYY-MM-DD'
    '''

    if type(date) != str:
        raise TypeError(f'Input value must be a string, but your type is {type(date)}')
    
    if not re.match(r'\d{4}-\d{2}-\d{2}', date):
        raise ValueError(f'input value "{date}" does not match format: "YYYY-MM-DD"')

    choosed_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()

    return today.toordinal() - choosed_date.toordinal()


if __name__ == '__main__':
    try:
        print(get_days_from_today('2026-10-21'))
    except Exception as e:
        print(e)
    