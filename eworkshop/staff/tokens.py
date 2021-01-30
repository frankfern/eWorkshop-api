from datetime import timedelta
from rest_framework_simplejwt.tokens import Token


class EmailToken(Token):
    token_type = 'password_reset'
    lifetime = timedelta(minutes=5)
