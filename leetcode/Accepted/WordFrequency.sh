#!/usr/bin/env bash

cat words.txt | tr '\n' ' ' | perl -pe 's/\s+/\n/g' | sort | uniq -c | sort -rnk2 | awk '{ print $2, $1}'
