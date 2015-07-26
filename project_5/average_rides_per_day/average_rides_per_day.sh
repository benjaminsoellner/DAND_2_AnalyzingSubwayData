#! /bin/bash

cat $( cd "$(dirname "$0")" ; pwd -P )/turnstile_data_master_with_weather.csv | python average_rides_per_day_mapper.py | sort | python average_rides_per_day_reducer.py
