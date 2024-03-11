from datetime import datetime

def get_days_from_today(date):
    while True:
        try:
            date_dt = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return "Given date is in a wrong format. Please try again"
        else:
            break
    today_dt = datetime.today()

    difference = today_dt - date_dt
    return difference.days

days_difference = get_days_from_today(input())
print("Difference in days:", days_difference)