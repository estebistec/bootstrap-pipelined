# Twitter Bootstrap Pipelined

## Overview

This is a simple template project utilizing [Twitter Bootstrap](http://twitter.github.com/bootstrap) and managing static assets with [django-pipeline](http://django-pipeline.readthedocs.org).

The purpose of this project is two-fold.

 * Keep a template project that can be improved later
 * Compare django-pipeline with other methods of managing static assets with
   Django

## Obtaining

 * `git clone git://github.com/estebistec/bootstrap-pipelined.git`
 * `cd bootstrap-pipelined`
 * `git submodule update --init # Pull in the Twitter Bootstrap git submodule`

## Running in development mode

 * `cd bootstrap_pipelined`
 * `./manage.py collectstatic --noinput`
 * `./manage.py runserver`

## Running an nginx "production" setup

Run the following command from the source root directory:

  * `./run-nginx.sh`

This script will run collectstatic, fire up nginx as the current user based on
a local conf, and then run the Django app behind it. nginx will server your
static files. After your terminate the Django app, nginx will stop too.

**NOTE** I run nginx on Mac OSX, as installed by [homebrew](http://mxcl.github.com/homebrew). YMMV on Linux or Windows.

## Updating Twitter Bootstrap

The Bootstrap git submodule can be updated as follows:

 * `cd bootstrap_pipelined/twitter_bootstrap/static`
 * `git checkout v2.0.5 # Or other commit, preferably a release tag`
