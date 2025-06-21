from datetime import datetime


def calculate_fees(days_overdue):
    """Calculate late fees: $0.25/day + $2 base fee"""
    return 2.00 + (days_overdue * 0.25)

def send_reminder_email(member, book, days_overdue):
    print(f"Reminder: {member.name} ({member.email}) has '{book.title}' overdue by {days_overdue} days.")

def validate_date(date_str):
    try:
        return datetime.fromisoformat(date_str)
    except Exception:
        return None