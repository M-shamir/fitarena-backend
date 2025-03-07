import pyotp
import redis
from django.conf import settings


redis_client = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=0)

class OTPService:
    def generate_otp(self,email):
        totp = pyotp.TOTP(settings.OTP_SECERT)
        otp = totp.now()
        redis_client.setex(f'otp_{email}',300,otp)
        return otp
        