# KEEP ALL SECRETS IN ../config.local.py !!!
SECRET_KEY = "CHANGE_ME"  # does not matter, remember to change it if app is working in the production environment!!!
APP_NAME = "Bazar AGH"

DB_HOST = "localhost"
DB_NAME = "db_name"
DB_PORT = 3306
DB_USER = "db_user"
DB_PASSWORD = "db_password"

# Bcrypt is set as default SECURITY_PASSWORD_HASH, which requires a salt
# Generate a good salt using: secrets.SystemRandom().getrandbits(128)
SECURITY_PASSWORD_SALT = '123456789012345678901234567890123456789'
