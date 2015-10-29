"""
    default_config
    ~~~~~~~~~~~~~~
    This module contains configuration keys for the application.
    See http://flask.pocoo.org/docs/config/ for more information.
"""
# Set to True to get interactive debug output instead of HTTP 500 error
DEBUG = False

# The secret key will be used to encrypt cookies.
SECRET_KEY = "This string will be replaced with a proper key in production."

# Database settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///'
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

# CSRF settings
CSRF_ENABLED = False
CSRF_SESSION_KEY = "somethingimpossibletoguess"

# Localhost Recaptcha settings
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}

# This folder will hold all user and job produced files, an `staging` directory
# will be created in instance folder in case this is not defined.
# STAGING_DIR = '/path/to/staging_dir'

# Mail settings
MAIL_SERVER = 'localhost'
DEFAULT_MAIL_SENDER = 'monitor@sqmpy'

# Number of results to show when using pagination
PER_PAGE = 10

# Will try to send notification emails when job status changes.
NOTIFICATION = False

# Default web server address. Set this to whatever address the server will run
# This will be used to generate urls outside of a request context for example
# for notifications which contain links to certain pages such as job details.
# SERVER_NAME = 'sqmpy.example.com:3000'

# Admin email to send job status notifications to, in case login is disabled
# ADMIN_EMAIL = 'me@example.com'

# For first release there is no login-procedure
LOGIN_DISABLED = True

# Enables LDAP login, this will cause LDAP credentials to be
#   used for SSH as well
USE_LDAP_LOGIN = False
# LDAP_SERVER = 'example.com'
# LDAP_BASEDN = 'ou=People,ou=IWM,o=Fraunhofer,c=DE'

# User user login information for SSH. Default option is password-less access.
# When set, sqmpy will user the provided username and password to obtain an
# SSH connection to any remote host.
SSH_WITH_LOGIN_INFO = False
