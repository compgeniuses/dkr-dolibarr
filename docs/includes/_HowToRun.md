
## How to run this image

This image is based on the [officiel PHP repository](https://registry.hub.docker.com/_/php/).
It is inspired from [nextcloud](https://github.com/nextcloud/docker), [tuxgasy/docker-dolibarr](https://github.com/tuxgasy/docker-dolibarr) and [Monogramm/docker-dolibarr](https://github.com/Monogramm/docker-dolibarr).

This image does not contain the database for Dolibarr. You need to use either an existing database or a database container.

This image is designed to be used in a micro-service environment. There are two versions of the image you can choose from.

The `apache` tag contains a full Dolibarr installation including an apache web server. It is designed to be easy to use and gets you running pretty fast. This is also the default for the `latest` tag and version tags that are not further specified.

The second option is a `fpm` container. It is based on the [php-fpm](https://hub.docker.com/_/php/) image and runs a fastCGI-Process that serves your Dolibarr page. To use this image it must be combined with any webserver that can proxy the http requests to the FastCGI-port of the container.
