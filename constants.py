import os
from shlex import quote
from config import config

cfg = config[os.environ['ENVIRONMENT']]

LAMBDA_ENV_VARS = quote('{SQS_ENDPOINT=%s,USE_SSL=%s,ADYN_AWS_SECRET_ACCESS_KEY=%s,ADYN_AWS_ACCESS_KEY=%s,AWS_REGION=%s}' % (cfg.LOCALSTACK_ENDPOINT, cfg.USE_SSL, cfg.ADYN_AWS_SECRET_ACCESS_KEY, cfg.ADYN_AWS_ACCESS_KEY, cfg.REGION))

LAMBDAS = [{
    # 'package': 'referral-hero-worker',
    # 'path': '/home/rob/repos/referral-hero-worker/',
    # 'name': 'ReferralHeroWorker',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': None
# }, {
    # 'package': 'hubspot-creator',
    # 'path': '/home/rob/repos/hubspot-creator/',
    # 'name': 'HubspotCreator',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': None
# }, {
    'package': 'hubspot-adopter',
    'path': '/home/rob/repos/hubspot-adopter/',
    'name': 'HubspotAdopter',
    'role': 'LambdaExecutionRole',
    'env_vars': None
}, {
    # 'package': 'shipment-service',
    # 'path': '/home/rob/repos/shipment-service/',
    # 'name': 'ShipmentService',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': None
# }, {
    # 'package': 'usps-tracker',
    # 'path': '/home/rob/repos/usps-tracker/',
    # 'name': 'USPSTracker',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': None
# }, {
    # 'package': 'usps-mocker',
    # 'path': '/home/rob/repos/usps-mocker/',
    # 'name': 'USPSMocker',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': None
# }, {
    'package': 'usps-checker',
    'path': '/home/rob/repos/usps-checker/',
    'name': 'USPSChecker',
    'role': 'LambdaExecutionRole',
    'env_vars': None
}, {
    'package': 'order-service',
    'path': '/home/rob/repos/order-service/',
    'name': 'OrderService',
    'role': 'LambdaExecutionRole',
    'env_vars': None
# }, {
    # 'package': 'auth-service',
    # 'path': '/home/rob/repos/auth-service/',
    # 'name': 'AuthService',
    # 'queue': 'Emailer',
    # 'queue_endpoint': 'sqs.us-east-1.amazonaws.com/031113038430/Emailer',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': LAMBDA_ENV_VARS,
    # 'kickstart_body': 'Subject',
    # 'kickstart_attributes': 'file://mailer-attributes.json'
}, {
    'package': 'behavior-worker',
    'path': '/home/rob/repos/behavior-worker/',
    'name': 'BehaviorWorker',
    'role': 'LambdaExecutionRole',
    'env_vars': None
}, {
    'package': 'jotform-worker',
    'path': '/home/rob/repos/jotform-worker/',
    'name': 'JotformWorker',
    'role': 'LambdaExecutionRole',
    'env_vars': None
}, {
    'package': 'medical-bio-service',
    'path': '/home/rob/repos/medical-bio-service/',
    'name': 'MedicalBioService',
    'role': 'LambdaExecutionRole',
    'env_vars': None
}, {
    'package': 'address-service',
    'path': '/home/rob/repos/address-service/',
    'name': 'AddressService',
    'role': 'LambdaExecutionRole',
    'env_vars': None
}, {
    'package': 'customer-service',
    'path': '/home/rob/repos/customer-service/',
    'name': 'CustomerService',
    'role': 'LambdaExecutionRole',
    'env_vars': None
}, {
    'package': 'email-service',
    'path': '/home/rob/repos/email-service/',
    'name': 'EmailService',
    'role': 'LambdaExecutionRole',
    'env_vars': None
# }, {
    # 'package': 'email-worker',
    # 'path': '/home/rob/repos/email-worker/',
    # 'name': 'EmailWorker',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': None
}, {
    'package': 'stripe-service',
    'path': '/home/rob/repos/stripe-service/',
    'name': 'StripeService',
    'role': 'LambdaExecutionRole',
    'env_vars': None
# }, {
    # 'package': 'stripe-worker',
    # 'path': '/home/rob/repos/stripe-worker/',
    # 'name': 'StripeWorker',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': None
}, {
    'package': 'allied-broker',
    'path': '/home/rob/repos/allied-broker/',
    'name': 'AlliedBroker',
    'role': 'LambdaExecutionRole',
    'env_vars': None
}, {
    'package': 'allied-checker',
    'path': '/home/rob/repos/allied-checker/',
    'name': 'AlliedChecker',
    'role': 'LambdaExecutionRole',
    'env_vars': None
# }, {
    # 'package': 'allied-tracker',
    # 'path': '/home/rob/repos/allied-tracker/',
    # 'name': 'AlliedTracker',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': None
# }, {
    # 'package': 'allied-resetter',
    # 'path': '/home/rob/repos/allied-resetter/',
    # 'name': 'AlliedResetter',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': None
# }, {
    # 'package': 'allied-mocker',
    # 'path': '/home/rob/repos/allied-mocker/',
    # 'name': 'AlliedMocker',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': None
# }, {
    # 'package': 'activation-service',
    # 'path': '/home/rob/repos/activation-service/',
    # 'name': 'ActivationService',
    # 'role': 'LambdaExecutionRole',
    # 'env_vars': None
}]
