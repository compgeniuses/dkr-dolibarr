# Using an external database

[<< Go back](./README.md)

By default this container does not contain the database for Dolibarr. You need to use either an existing database or a database container.

The Dolibarr setup wizard (should appear on first run) allows connecting to an existing MySQL/MariaDB or PostgreSQL database. You can also link a database container, e. g. `--link my-mysql:mysql`, and then use `mysql` as the database host on setup. More info is in the docker-compose section.
