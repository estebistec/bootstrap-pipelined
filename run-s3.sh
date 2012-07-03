#!/bin/sh
bootstrap_pipelined
cd bootstrap_pipelined
./manage.py collectstatic --settings=bootstrap_pipelined.s3_settings --noinput
./manage.py runserver --settings=bootstrap_pipelined.s3_settings
