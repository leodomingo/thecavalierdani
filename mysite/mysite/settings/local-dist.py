"""Copy this file into local.py and fill in blanks"""

# Do NOT fill any of these fields out in local-dist.py or defaults.py
# Only fill these out in local.py, a file that you create on
# your local machine

# Any settings that contain keys should be left blank in
# local-dist.py and in defaults.py
# Each developer should add their own keys in local.py
# This is to avoid putting private keys on Github for
# everyone to see

# SECURITY WARNING: keep the secret key used in production secret!
#  fill this out with a long random string in local.py
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
# If developing locally, set DEBUG to True
# If deploying, set DEBUG to False
DEBUG = True

# Set deployment to be True if deploying
DEPLOYMENT = False


# Save images/statics locally, if not a deployment
# Save images/statics to s3 if deployment
if DEPLOYMENT:
    # django-storages
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    # Log on to aws, go to IAM console
    # Create a user or go to your user if you alread have one
    # Click "Create access key"
    # Copy keys here
    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''

    # Log on to aws, go to s3 console
    # copy name of bucket in the list here
    # it should look like elasticbeanstalk-us-east-1-...
    AWS_STORAGE_BUCKET_NAME = ''

    # Fill in with aws domain (not custom)
    # Go to aws, elastic beanstalk console
    # Go to correct region (top right)
    # Click on the environment
    # Copy URL listed on page here
    ALLOWED_HOSTS = []
