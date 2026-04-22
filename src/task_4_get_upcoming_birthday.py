from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    '''
    The function returns a list of users with greeting dates.

    Args:
        users (list[dict{name: str, birthday: str}]): list of users with name and birthday in format 'YYYY.MM.DD'

    Returns:
        list[dict{name: str, congratulation_date: str}]: list of users with name and congratulation dates in format 'YYYY.MM.DD'

    Raises:
        TypeError: if type users not list
    '''

    if type(users) != list:
        raise TypeError(f'Input value must be a list, but your type is {type(users)}')

    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        next_birthday = datetime \
            .strptime(user['birthday'], '%Y.%m.%d') \
            .date() \
            .replace(year=today.year)

        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
            
        days_difference = next_birthday.toordinal() - today.toordinal()
        birthday_week_day = next_birthday.isoweekday()

        if days_difference < 7:
            if birthday_week_day < 6:
                congratulation_date = next_birthday
            else:
                days_to_next_monday = 7 - birthday_week_day + 1
                congratulation_date = next_birthday + timedelta(days=days_to_next_monday)

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays


if __name__ == '__main__':
    users = [
        {'name': 'John Doe',   'birthday': '1985.02.23'},
        {'name': 'Pink Floyd', 'birthday': '1989.04.18'},
        {'name': 'Tom Hanks',  'birthday': '1985.04.19'},
        {'name': 'Jim Carrey', 'birthday': '1975.04.25'},
        {'name': 'Jane Smith', 'birthday': '1990.04.26'},
        {'name': 'Dan Landy',  'birthday': '1990.04.24'},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print('Список привітань на наступні 7 днів:', upcoming_birthdays)

