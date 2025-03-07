from django.core.mail import send_mail
from django.conf import settings

class EmailService:
    def sent_otp_email(self,email,otp):
        subject = 'Your OTP Verification Code'
        message = f'Your OTP code is: {otp}'
        from_email = settings.DEFAULT_FROM_EMAIL
        send_mail(subject,message,from_email,[email])