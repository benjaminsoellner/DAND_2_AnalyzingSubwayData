@echo off
type %~dp0%turnstile_data_master_with_weather.csv | python busiest_hour_mapper.py | sort | python busiest_hour_reducer.py