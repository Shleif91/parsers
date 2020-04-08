#!/usr/bin/env bash

set -o errexit

docker-compose run --rm --user=1000:1000 python scrapy $@
