# localstack-environment

```
# Create a local adyndb (one time only)
docker run --name adyndb -e POSTGRES_USER=$ADYN_POSTGRES_USER -e POSTGRES_PASSWORD=$ADYN_POSTGRES_PASSWORD -e POSTGRES_DB=$ADYN_POSTGRES_DB -p 5432:5432 -d postgres:10.3

# Create tables
psql -h $(docker-machine ip adyndev) -U $ADYN_POSTGRES_USER -d $ADYN_POSTGRES_DB -f schema.sql -W

# Boot localstack
cd ~/repos/localstack-environment && source venv/bin/activate && SERVICES=cloudwatch,s3,ses,iam,sqs,lambda localstack start

# Start all of the services
cd ~/repos/customer-service
source venv/bin/activate
python3 main.py

cd ~/repos/address-service
source venv/bin/activate
python3 main.py

cd ~/repos/auth-service
source venv/bin/activate
python3 main.py

cd ~/repos/email-service
source venv/bin/activate
python3 main.py
```

## Generating Staging SSL Certs
```
docker run -it -v "$(pwd)":/etc/letsencrypt --env AWS_ACCESS_KEY_ID= --env AWS_SECRET_ACCESS_KEY= certbot/dns-route53 certonly --dns-route53 --preferred-challenges dns --email rob@adyn.com --server https://acme-v02.api.letsencrypt.org/directory --agree-tos -d 'api.adyn.com' -d 'dashboard.adyn.com' -d 'my-staging.adyn.com' -d 'my.adyn.com' -d 'website-staging.adyn.com'

This certificate expires on 2021-09-06.
These files will be updated when the certificate renews.

NEXT STEPS:
- The certificate will need to be renewed before it expires. Certbot can automatically renew the certificate in the background, but you may need to take steps to enable that functionality. See https://certbot.org/renewal-setup for instructions.
``` 
# localstack-environment
