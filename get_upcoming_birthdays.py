from datetime import datetime, timedelta


def get_upcoming_birthdays(users, days_ahead=7):
    upcoming_birthdays = []
    today = datetime.today().date()
    end_date = today + timedelta(days=days_ahead)

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%d.%m.%Y").date()
        birthday_this_year = datetime(
            year=today.year, month=birthday.month, day=birthday.day
        ).date()

        if birthday_this_year < today:
            continue

        congratulation_date = birthday_this_year
        if congratulation_date.weekday() == 5:
            congratulation_date = congratulation_date + timedelta(days=2)
        elif congratulation_date.weekday() == 6:
            congratulation_date = congratulation_date + timedelta(days=1)

        if birthday_this_year <= end_date:
            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y"),
                }
            )

    return upcoming_birthdays
