# KEEP ALL SECRETS IN ../config.local.py !!!
SECRET_KEY = "CHANGE_ME"  # does not matter, remember to change it if app is working in the production environment!!!
APP_NAME = "Bazar AGH"
APP_DEBUG = False

DEBUG_LOG = 'logs/debug.log'
ERROR_LOG = 'logs/error.log'

BABEL_DEFAULT_LOCALE = 'pl'

DB_HOST = "localhost"
DB_NAME = "db_name"
DB_PORT = 3306
DB_USER = "db_user"
DB_PASSWORD = "db_password"

MAIL_SERVER = "localhost"
MAIL_PORT = 587
MAIL_USERNAME = "mail_user"
MAIL_PASSWORD = "mail_password"
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_DEFAULT_SENDER = "BazarAGH.pl <no-reply@bazaragh.pl>"

# Bcrypt is set as default SECURITY_PASSWORD_HASH, which requires a salt
# Generate a good salt using: secrets.SystemRandom().getrandbits(128)
SECURITY_PASSWORD_SALT = '123456789012345678901234567890123456789'
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = True
SECURITY_POST_REGISTER_VIEW = 'security.register'
SECURITY_CHANGEABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_RECOVERABLE = True
