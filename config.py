import os


class Default:
    REGION = 'us-east-1'
    PROFILE = 'localstack'


class Development(Default):
    USE_SSL = 0
    LOCALSTACK_ENDPOINT = 'https://' if os.environ['USE_SSL'] == '1' else 'http://' + os.environ['LOCALSTACK_ENDPOINT']
    ADYN_AWS_SECRET_ACCESS_KEY = os.environ['ADYN_AWS_SECRET_ACCESS_KEY']
    ADYN_AWS_ACCESS_KEY = os.environ['ADYN_AWS_ACCESS_KEY']


class Production(Default):
    USE_SSL = 1


config = {
    'default': Default,
    'development': Development,
    'production': Production
}
