#!/bin/bash

if [ -z "$1" ]
then
  echo "Error: Please provide a filepath as an argument."
  exit 1
fi

python ignore.py "$1"