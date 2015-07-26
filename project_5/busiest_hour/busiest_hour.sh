#! /bin/bash

cat $( cd "$(dirname "$0")" ; pwd -P )/turnstile_data_master_with_weather.csv | python busiest_hour_mapper.py | sort | python busiest_hour_reducer.py

