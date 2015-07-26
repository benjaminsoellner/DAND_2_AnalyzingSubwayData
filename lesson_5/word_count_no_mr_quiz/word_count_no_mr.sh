#! /bin/bash

cat $( cd "$(dirname "$0")" ; pwd -P )/aliceInWonderland.txt | python word_count.py
