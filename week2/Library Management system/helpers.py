from datetime import datetime


def calculate_fees(days_overdue):
    """Calculate late fees: $0.25/day + $2 base fee"""
    return 2.00 + (days_overdue * 0.25)

def send_reminder_email(member, book, days_overdue):
    """Generate reminder email content"""
    subject = f"Overdue Book: {book.title}"
    body = (f"Dear {member.name},\n\n"
            f"Your book '{book.title}' is {days_overdue} days overdue.\n"
            f"Please return it immediately to avoid additional fees.")

    print(f"Email sent to {member.email}:\n{subject}\n{body}")
    
def validate_date(date_str):
    """Check if date string is correct (YYYY-MM-DD)"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False