# Base version - FPM with PostgreSQL

[<< Go back](./README.md)

When using the FPM image you need another container that acts as web server on port 80 and proxies the requests to the Dolibarr container. In this example a simple nginx container is combined with the maximelaplanche/docker-dolibarr-fpm image and a [PostgreSQL](https://hub.docker.com/_/postgres/) database container. The data is stored in docker volumes. The nginx container also need access to static files from your Dolibarr installation. It gets access to all the volumes mounted to Dolibarr via the `volumes_from` option. The configuration for nginx is stored in the configuration file `nginx.conf`, that is mounted into the container.

As this setup does **not include encryption** it should to be run behind a proxy.

Make sure to set the variables `POSTGRES_PASSWORD` and `DOLI_DB_PASSWORD` before you run this setup.

Create `docker-compose.yml` file using [docker-compose_fpm.yml](/template/docker-compose.fpm.test.yml) as template.

Here is a sample `nginx.conf` file expected to be in the same folder:
```nginx
    server {
        listen 80;
        server_name ${NGINX_HOST};

        root /var/www/html;
        index index.php;

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        location / {
            try_files $uri $uri/ index.php;
        }

        location ~ [^/]\.php(/|$) {
            # try_files $uri =404;
            fastcgi_split_path_info ^(.+?\.php)(/.*)$;
            fastcgi_pass dolibarr:9000;
            fastcgi_index index.php;
            include fastcgi_params;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_param PATH_INFO $fastcgi_path_info;
        }

        location /api {
            if ( !-e $request_filename) {
                rewrite ^.* /api/index.php last;
            }
        }

    }
```

[<< Go back](./README.md)
