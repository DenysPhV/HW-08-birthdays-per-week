from collections import defaultdict
from typing import Dict, List
from datetime import datetime, timedelta
from random import randint


def generate_date() -> datetime.date:

    month_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    year = randint(1970, 2005)
    month = randint(1, 12)
    day = randint(1, month_days[month])
    return datetime(year=year, month=month, day=day).date()


def generate_users(n=500):
    users = {}
    for i in range(n):
        username = "user " + str(i)
        birthday = generate_date()
        users[username] = birthday
    return [users]


users_birthdays: List[Dict[str, datetime.date]] = generate_users()


def get_weekday_by_id(weekday_id: int):

    weekday_map: Dict[int, str] = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    return weekday_map[weekday_id]


def construct_current_date(day_of_birth: datetime.date):
    current_year = datetime.now().year
    return datetime(year=current_year, month=day_of_birth.month, day=day_of_birth.day).date()


def get_birthdays_per_week(users: List[Dict[str, datetime.date]]):

    greeting_scheduler: Dict[str, List] = defaultdict(list)

    start_greeting = datetime.now().date()
    one_week_delta = timedelta(days=7)
    if start_greeting.weekday() == 0:   # we check if the start_greeting is Monday to take out next Sat+Sun
        one_week_delta = timedelta(days=5)
    finish_greeting = start_greeting + one_week_delta

    for user_dict in users:

        for username, birthday in user_dict.items():
            current_year_birthday = construct_current_date(birthday)

            if current_year_birthday < start_greeting or current_year_birthday >= finish_greeting:
                continue

            birthday_day_index = current_year_birthday.weekday()
            weekday = get_weekday_by_id(birthday_day_index)
            if weekday in ["Saturday", "Sunday"]:
                weekday = "Monday"

            greeting_scheduler[weekday].append({username: birthday})

        print(f"Today is: {start_greeting}")
        print("We have the following nearest birthdays:")
        print("\n")
        for weekday, birthday_guy in greeting_scheduler.items():
            print(f"{weekday}: {birthday_guy}")
        return greeting_scheduler


if __name__ == "__main__":
    get_birthdays_per_week(users_birthdays)
