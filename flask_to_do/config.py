from datetime import timedelta


class Config(object):
    DEBUG = True
    SECRET_KEY = "tamagochi"
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)
