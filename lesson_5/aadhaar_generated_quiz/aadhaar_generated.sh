#! /bin/bash

cat $( cd "$(dirname "$0")" ; pwd -P )/aadhaar_data.csv | python aadhaar_generated_mapper.py | sort | python aadhaar_generated_reducer.py
