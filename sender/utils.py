from django.core.mail import send_mail
from mailsender.settings import EMAIL_HOST_USER
def send_email(subject, message, recipient_list):
    """
    Sends an email using Django's send_mail function.

    Parameters:
    - subject: The subject of the email.
    - message: The content of the email.
    - recipient_list: A list of recipient email addresses.
    """
    from_email = EMAIL_HOST_USER  # Replace with your email
    send_mail(subject, message, from_email, recipient_list)
