#!/usr/bin/env bash

set -o errexit

readarray -t PROXIES < scrapy/proxies/proxies.txt

for i in {0..49}
do
    NUM=$(( $i ))
    docker-compose run --rm --user=1000:1000 python scrapy crawl yandex_market \
        -a start=$NUM -s CUSTOM_PROXY="http://${PROXIES[$i]}" \
        -L INFO --logfile=logs/$NUM.log &
done
