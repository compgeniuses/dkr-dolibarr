# Using image with other web server

[<< Go back](./README.md)

## Using the apache image

The apache image contains a webserver and exposes port 80. To start the container type:

```shell
$ docker run -d -e DOLI_AUTO_CONFIGURE='' -p 8080:80 n0xcode/docker-dolibarr
```

Now you can access Dolibarr at <http://localhost:8080/> from your host system.

## Using the fpm image

To use the fpm image you need an additional web server that can proxy http-request to the fpm-port of the container. For fpm connection this container exposes port 9000. In most cases you might want use another container or your host as proxy.
If you use your host you can address your Dolibarr container directly on port 9000. If you use another container, make sure that you add them to the same docker network (via `docker run --network <NAME> ...` or a `docker-compose` file).
In both cases you don't want to map the fpm port to you host.

```shell
$ docker run -d -e DOLI_AUTO_CONFIGURE='' n0xcode/docker-dolibarr:fpm
```

As the fastCGI-Process is not capable of serving static files (style sheets, images, ...) the webserver needs access to these files. This can be achieved with the `volumes-from` option. You can find more information in the docker-compose section.

Then run all services `docker-compose up -d`. Now, go to <http://localhost:80/install> to access the new Dolibarr installation wizard.
In this example, the Dolibarr scripts, documents, HTML and database will all be stored in Docker's default location.
Feel free to edit this as you see fit.

[<< Go back](./README.md)
