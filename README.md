# synology-ddns-python-route53

A serverless AWS Lambda function that updates a Route53 record for a domain name using the [Synology Dynamic DNS](https://www.synology.com/en-us/support/dynamic-dns/dynamic-dns-overview/) service.

Inspired by https://www.synoforum.com/resources/ddns-with-aws-lambda-and-route53.25/

# Usage

## Deployment

The function has three constants/environment variables defined:

USERNAME: A random string used to authenticate the function from the Synology Dynamic DNS service.
PASSWORD: A random password that is used to authenticate from the Synology Dynamic DNS service.HOSTED_ZONE_ID: The ID of the hosted zone that is used to update the DNS record.

```
serverless deploy \
--param="username=mysupersecretusername" \
--param="password=mysupersecretpassword" \
--param="hostedzoneid=myawsdomainhostedzoneid"
```

## Update Synology DDNS

Update Synology's DDNS service with the API Geateway URL given when this deploys. Use the same USERNAME and PASSWORD as defined in the deployment.
The query in Synology should look like this:
https://<Your Unique Lambda ID>.execute-api.<Your Region>.amazonaws.com?hostname=__HOSTNAME__&ip=__MYIP__&username=__USERNAME__&password=__PASSWORD__


