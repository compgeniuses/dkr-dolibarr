# Update container and add features

[<< Go back](./README.md)

## Update to a newer version

Updating the Dolibarr container is done by pulling the new image, throwing away the old container and starting the new one. Since all data is stored in volumes, nothing gets lost. The startup script will check for the version in your volume and the installed docker version. If it finds a mismatch, it automatically starts the upgrade process. Don't forget to add all the volumes to your new container, so it works as expected. Also, we advised you do not skip major versions during your upgrade. For instance, upgrade from 5.0 to 6.0, then 6.0 to 7.0, not directly from 5.0 to 7.0.

```shell
$ docker pull maximelaplanche/docker-dolibarr
$ docker stop <your_dolibarr_container>
$ docker rm <your_dolibarr_container>
$ docker run <OPTIONS> -d maximelaplanche/docker-dolibarr
```

Beware that you have to run the same command with the options that you used to initially start your Dolibarr. That includes volumes, port mapping.

When using docker-compose your compose file takes care of your configuration, so you just have to run:

```shell
$ docker-compose pull
$ docker-compose up -d
```

## Adding Features

If the image does not include the packages you need, you can easily build your own image on top of it.
Start your derived image with the `FROM` statement and add whatever you like.

```Dockerfile
FROM maximelaplanche/docker-dolibarr:apache

RUN ...

```

You can also clone this repository and use the [update.sh](update.sh) shell script to generate a new Dockerfile based on your own needs.

For instance, you could build a container based on Dolibarr develop branch by setting the `update.sh` versions like this:

```bash
versions=( "develop" )
```

Then simply call [update.sh](update.sh) script.

```shell
bash update.sh
```

Your Dockerfile(s) will be generated in the `images/develop` folder.

If you use your own Dockerfile you need to configure your docker-compose file accordingly. Switch out the `image` option with `build`. You have to specify the path to your Dockerfile. (in the example it's in the same directory next to the docker-compose file)

```yaml
  app:
    build: .
    links:
      - db
    volumes:
      - data:/var/www/html/data
      - config:/var/www/html/config
      - apps:/var/www/html/apps
    restart: always
```

**Updating** your own derived image is also very simple. When a new version of the Dolibarr image is available run:

```shell
docker build -t your-name --pull .
docker run -d your-name
```

or for docker-compose:

```shell
docker-compose build --pull
docker-compose up -d
```

The `--pull` option tells docker to look for new versions of the base image. Then the build instructions inside your `Dockerfile` are run on top of the new image.

[<< Go back](./README.md)
