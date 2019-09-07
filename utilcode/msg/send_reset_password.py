from django.core.mail import send_mail
from django.conf import settings


def send_reset_email(email, link):
    try:
        subject = "Password Reset Requested"
        message = "Kindly click the link to reset password {}/commerce/reset-change/{}".format(
            settings.FRONTEND_URL, link
        )
        email_from = 'admin@shopstack.co'
        recipient_list = [email]
        print(email)
        print(send_mail(subject, message, email_from, recipient_list))
        return True
    except Exception as identifier:
        print(identifier)
        return False
