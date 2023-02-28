# Running this image with docker-compose

[<< Go back](./README.md)

## Base version - apache with MariaDB/MySQL

This version will use the apache image and add a [MariaDB](https://hub.docker.com/_/mariadb/) container (you can also use [MySQL](https://hub.docker.com/_/mysql/) if you prefer). The volumes are set to keep your data persistent. This setup provides **no ssl encryption** and is intended to run behind a proxy.

Make sure to set the variables `MYSQL_ROOT_PASSWORD`, `MYSQL_PASSWORD`, `DOLI_DB_PASSWORD` before you run this setup.

Create `docker-compose.yml` file using [docker-compose_apache.yml](/template/docker-compose.apache.test.yml) as template.

Then run all services `docker-compose up -d`. Now, go to <http://localhost:80/install> to access the new Dolibarr installation wizard.
In this example, the Dolibarr scripts, documents, HTML and database will all be stored locally in the following folders:

- `/srv/dolibarr/html`
- `/srv/dolibarr/scripts`
- `/srv/dolibarr/documents`
- `/srv/dolibarr/db`

[<< Go back](./README.md)
