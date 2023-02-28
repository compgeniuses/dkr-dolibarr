# Persistent data

[<< Go back](./README.md)

The Dolibarr installation and all data beyond what lives in the database (file uploads, etc) are stored in the [unnamed docker volume](https://docs.docker.com/engine/tutorials/dockervolumes/#adding-a-data-volume) volume `/var/www/html` and  `/var/www/documents`. The docker daemon will store that data within the docker directory `/var/lib/docker/volumes/...`. That means your data is saved even if the container crashes, is stopped or deleted.

To make your data persistent to upgrading and get access for backups is using named docker volume or mount a host folder. To achieve this you need one volume for your database container and Dolibarr.

Dolibarr:

- `/var/www/html/` folder where all Dolibarr data lives
- `/var/www/documents/` folder where all Dolibarr documents lives

```shell
$ docker run -d \
    -v dolibarr_html:/var/www/html \
    -v dolibarr_docs:/var/www/documents \
    -e DOLI_AUTO_CONFIGURE='' \
    maximelaplanche/docker-dolibarr
```

Database:

- `/var/lib/mysql` MySQL / MariaDB Data
- `/var/lib/postgresql/data` PostgreSQL Data

```shell
$ docker run -d \
    -v db:/var/lib/mysql \
    mariadb \
    --character_set_client=utf8 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --character-set-client-handshake=FALSE
```

If you want to get fine grained access to your individual files, you can mount additional volumes for config, your theme and custom modules.
The `conf` is stored in subfolder inside `/var/www/html/`. The modules are split into core `apps` (which are shipped with Dolibarr and you don't need to take care of) and a `custom` folder. If you use a custom theme it would go into the `theme` subfolder.

Overview of the folders that can be mounted as volumes:

- `/var/www/html` Main folder, needed for updating
- `/var/www/html/custom` installed / modified modules
- `/var/www/html/conf` local configuration
- `/var/www/html/theme/<YOUR_CUSTOM_THEME>` theming/branding

If you want to use named volumes for all of these it would look like this

```shell
$ docker run -d \
    -v dolibarr:/var/www/html \
    -v apps:/var/www/html/custom \
    -v config:/var/www/html/conf \
    -v theme:/var/www/html/theme/<YOUR_CUSTOM_THEME> \
    -e DOLI_AUTO_CONFIGURE='' \
    maximelaplanche/docker-dolibarr
```
[<< Go back](./README.md)
