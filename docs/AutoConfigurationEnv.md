# Auto configuration via environment variables

[<< Go back](./README.md)

The Dolibarr image supports auto configuration via environment variables. You can preconfigure nearly everything that is asked on the install page on first run. To enable auto configuration, set your database connection via the following environment variables. ONLY use one database type!

See [conf.php.example](https://github.com/Dolibarr/dolibarr/blob/develop/htdocs/conf/conf.php.example) and [install.forced.sample.php](https://github.com/Dolibarr/dolibarr/blob/develop/htdocs/install/install.forced.sample.php) for more details on install configuration.

## DOLI_AUTO_CONFIGURE

_Default value_: `1`

_Possible values_: `1`, `''`

This parameter triggers the Dolibarr default configuration generation based on environment variables.

Examples:
``` properties
    DOLI_AUTO_CONFIGURE=1
    DOLI_AUTO_CONFIGURE=''
```

## DOLI_DB_TYPE

_Default value_: `mysqli`

_Possible values_: `mysqli`, `pgsql`

This parameter contains the name of the driver used to access your Dolibarr database.

Examples:
```properties
    DOLI_DB_TYPE=mysqli
    DOLI_DB_TYPE=pgsql
```

## DOLI_DB_HOST

_Default value_:

This parameter contains host name or ip address of Dolibarr database server.

Examples:
```properties
    DOLI_DB_HOST=localhost
    DOLI_DB_HOST=127.0.2.1
    DOLI_DB_HOST=192.168.0.10
    DOLI_DB_HOST=mysql.myserver.com
```

## DOLI_DB_PORT

_Default value_: `3306`

This parameter contains the port of the Dolibarr database.

Examples:
```properties
    DOLI_DB_PORT=3306
    DOLI_DB_PORT=5432
```

## DOLI_DB_NAME

_Default value_: `dolibarr`

This parameter contains name of Dolibarr database.

Examples:
```properties
    DOLI_DB_NAME=dolibarr
    DOLI_DB_NAME=mydatabase
```

## DOLI_DB_USER

_Default value_: `dolibarr`

This parameter contains user name used to read and write into Dolibarr database.

Examples:
```properties
    DOLI_DB_USER=admin
    DOLI_DB_USER=dolibarruser
```

## DOLI_DB_PASSWORD

_Default value_:

This parameter contains password used to read and write into Dolibarr database.

Examples:
```properties
    DOLI_DB_PASSWORD=myadminpass
    DOLI_DB_PASSWORD=myuserpassword
```

## DOLI_DB_PREFIX

_Default value_: `llx_`

This parameter contains prefix of Dolibarr database.

Examples:
```properties
    DOLI_DB_PREFIX=llx_
```

## DOLI_DB_CHARACTER_SET

_Default value_: `utf8`

Database character set used to store data (forced during database creation. value of database is then used).
Depends on database driver used. See `DOLI_DB_TYPE`.

Examples:
```properties
    DOLI_DB_CHARACTER_SET=utf8
```

## DOLI_DB_COLLATION

_Default value_: `utf8_unicode_ci`

Database collation used to sort data (forced during database creation. value of database is then used).
Depends on database driver used. See `DOLI_DB_TYPE`.

Examples:
```properties
    DOLI_DB_COLLATION=utf8_unicode_ci
```

## DOLI_DB_ROOT_LOGIN

_Default value_:

This parameter contains the database server root username used to create the Dolibarr database.

If this parameter is set, the container will automatically tell Dolibarr to create the database on first install with the root account.

Examples:
```properties
    DOLI_DB_ROOT_LOGIN=root
    DOLI_DB_ROOT_LOGIN=dolibarruser
```

## DOLI_DB_ROOT_PASSWORD

_Default value_:

This parameter contains the database server root password used to create the Dolibarr database.

Examples:
```properties
    DOLI_DB_ROOT_PASSWORD=myrootpass
```

## DOLI_ADMIN_LOGIN

_Default value_: `admin`

This parameter contains the admin's login used in the first install.

Examples:
```properties
    DOLI_ADMIN_LOGIN=admin
```

## DOLI_MODULES

_Default value_:

This parameter contains the list (comma separated) of modules to enable in the first install.

Examples:
```properties
    DOLI_MODULES=modSociete
    DOLI_MODULES=modSociete,modPropale,modFournisseur,modContrat,modLdap
```

## DOLI_URL_ROOT

_Default value_: `http://localhost`

This parameter defines the root URL of your Dolibarr index.php page without ending "/".
It must link to the directory htdocs.
In most cases, this is autodetected but it's still required

-   to show full url bookmarks for some services (ie: agenda rss export url, ...)
-   or when using Apache dir aliases (autodetect fails)
-   or when using nginx (autodetect fails)

Examples:
```properties
    DOLI_URL_ROOT=http://localhost
    DOLI_URL_ROOT=http://mydolibarrvirtualhost
    DOLI_URL_ROOT=http://myserver/dolibarr/htdocs
    DOLI_URL_ROOT=http://myserver/dolibarralias
```

## DOLI_AUTH

_Default value_: `dolibarr`

_Possible values_: Any values found in files in htdocs/core/login directory after the `function_` string and before the `.php` string, **except forceuser**. You can also separate several values using a `,`. In this case, Dolibarr will check login/pass for each value in order defined into value. However, note that this can't work with all values.

This parameter contains the way authentication is done.
**Will not be used if you use first install wizard.** See _First use_ for more details.

If value `ldap` is used, you must also set parameters `DOLI_LDAP_*` and `DOLI_MODULES` must contain `modLdap`.

Examples:
```properties
    DOLI_AUTH=http
    DOLI_AUTH=dolibarr
    DOLI_AUTH=ldap
    DOLI_AUTH=openid,dolibarr
```

## DOLI_LDAP_HOST

_Default value_:

You can define several servers here separated with a comma.

Examples:
```properties
    DOLI_LDAP_HOST=localhost
    DOLI_LDAP_HOST=ldap.company.com
    DOLI_LDAP_HOST=ldaps://ldap.company.com:636,ldap://ldap.company.com:389
```

## DOLI_LDAP_PORT

_Default value_: `389`

## DOLI_LDAP_VERSION

_Default value_: `3`

## DOLI_LDAP_SERVERTYPE

_Default value_: `openldap`
_Possible values_: `openldap`, `activedirectory` or `egroupware`

## DOLI_LDAP_DN

_Default value_:

Examples:
```properties
    DOLI_LDAP_DN=ou=People,dc=company,dc=com
```

## DOLI_LDAP_LOGIN_ATTRIBUTE

_Default value_: `uid`

Ex: uid or samaccountname for active directory

## DOLI_LDAP_FILTER

_Default value_:

If defined, the two previous parameters are not used to find a user into LDAP.

Examples:
```properties
    DOLI_LDAP_FILTER=(uid=%1%)
    DOLI_LDAP_FILTER=(&(uid=%1%)(isMemberOf=cn=Sales,ou=Groups,dc=company,dc=com))
```

## DOLI_LDAP_ADMIN_LOGIN

_Default value_:

Required only if anonymous bind disabled.

Examples:
```properties
    DOLI_LDAP_ADMIN_LOGIN=cn=admin,dc=company,dc=com
```

## DOLI_LDAP_ADMIN_PASS

_Default value_:

Required only if anonymous bind disabled. Ex:

Examples:
```properties
    DOLI_LDAP_ADMIN_PASS=secret
```

## DOLI_LDAP_DEBUG

_Default value_: `false`

## DOLI_PROD

_Default value_: `0`

_Possible values_: `0` or `1`

When this parameter is defined, all errors messages are not reported.
This feature exists for production usage to avoid to give any information to hackers.

Examples:
```properties
    DOLI_PROD=0
    DOLI_PROD=1
```

## DOLI_HTTPS

_Default value_: `0`

_Possible values_: `0`, `1`, `2` or `https://my.domain.com`

This parameter allows to force the HTTPS mode.

-   `0` = No forced redirect
-   `1` = Force redirect to https, until `SCRIPT_URI` start with https into response
-   `2` = Force redirect to https, until `SERVER["HTTPS"]` is 'on' into response
-   `https://my.domain.com` = Force redirect to https using this domain name.

_Warning_: If you enable this parameter, your web server must be configured to
respond URL with https protocol.
According to your web server setup, some values may work and other not. Try
different values (`1`, `2` or `https://my.domain.com`) if you experience problems.

Examples:
```properties
    DOLI_HTTPS=0
    DOLI_HTTPS=1
    DOLI_HTTPS=2
    DOLI_HTTPS=https://my.domain.com
```

## DOLI_NO_CSRF_CHECK

_Default value_: `0`

_Possible values_: `0`, `1`

This parameter can be used to disable CSRF protection.

This might be required if you access Dolibarr behind a proxy that make URL rewriting, to avoid false alarms.

Examples:
```properties
    DOLI_NO_CSRF_CHECK=0
    DOLI_NO_CSRF_CHECK=1
```

## PHP_INI_DATE_TIMEZONE

_Default value_: `UTC`

Default timezone on PHP.

## PHP_MEMORY_LIMIT

_Default value_: `256M`

Default memory limit on PHP.

## PHP_MAX_UPLOAD

_Default value_: `20M`

Default max upload size on PHP.

## PHP_MAX_EXECUTION_TIME

_Default value_: `300`

Default max execution time (in seconds) on PHP.

## WWW_USER_ID

_Default value_: `33`

ID of user www-data. ID will not change if left empty. During development, it is very practical to put the same ID as the host user.

## WWW_GROUP_ID

_Default value_: `33`

ID of group www-data. ID will not change if left empty.

[<< Go back](./README.md)
