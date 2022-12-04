#!/usr/bin/env bash

set -e

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

if [[ -z "$1" ]]; then
  echo "Missing YEAR parameter"
  echo "Usage: ./init_day.sh YEAR DAY"
  exit 1
fi

if [[ -z "$2" ]]; then
  echo "Missing DAY parameter"
  echo "Usage: ./init_day.sh YEAR DAY"
  exit 1
fi

YEAR="$1"
DAY=`printf %02d $2`


touch $SCRIPT_DIR/$YEAR/inputs/$DAY.txt
touch $SCRIPT_DIR/$YEAR/inputs/$DAY.example.txt
cp $SCRIPT_DIR/day_template.py $SCRIPT_DIR/$YEAR/original_solutions/day$DAY.py

DAY_SIMPLE=`printf %01d $2`
sed -i "s/YEAR, DAY = 2000, 0/YEAR, DAY = $YEAR, $DAY_SIMPLE/" $SCRIPT_DIR/$YEAR/original_solutions/day$DAY.py
