# Make your Dolibarr available from the internet

[<< Go back](./README.md)

Until here your Dolibarr is just available from you docker host. If you want you Dolibarr available from the internet adding SSL encryption is mandatory.

## HTTPS - SSL encryption

There are many different possibilities to introduce encryption depending on your setup.

We recommend using a reverse proxy in front of our Dolibarr installation. Your Dolibarr will only be reachable through the proxy, which encrypts all traffic to the clients. You can mount your manually generated certificates to the proxy or use a fully automated solution, which generates and renews the certificates for you.

[<< Go back](./README.md)
