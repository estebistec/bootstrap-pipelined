#!/bin/sh

sed "s|SOURCE_ROOT|$(pwd)|" nginx.conf.template > nginx.conf
nginx -c $(pwd)/nginx.conf
echo "**** Access running server at http://localhost:8080 ****"

cd bootstrap_pipelined
./manage.py collectstatic --noinput
./manage.py runserver --settings=bootstrap_pipelined.nginx_settings

nginx -s stop
