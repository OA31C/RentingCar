from renting_car.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def exception_email(message, send_to):
    """Catches an error if there are problems. with sending a letter."""
    try:
        send_mail('Renting Car Django', message,
                  EMAIL_HOST_USER, send_to)
    except:
        print('Лист не можна відправити.Сталася помилка на стороні серверу.')
