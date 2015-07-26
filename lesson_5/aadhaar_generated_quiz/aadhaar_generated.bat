@echo off
type %~dp0%aadhaar_data.csv | python aadhaar_generated_mapper.py | sort | python aadhaar_generated_reducer.py
