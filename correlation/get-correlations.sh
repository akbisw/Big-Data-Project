#!/usr/bin/env bash
# Get correlation
# generate all possible scalar functions at different spatio-temporal resolutions
for filename in `hadoop fs -ls "correlations/*/" | awk '{print $NF}' | grep "-" | tr '\n' ' '`
do
    output=$(echo "$filename" | sed 's/correlations\///g' | sed 's/\//-/g' )
    hadoop fs -getmerge $filename correlations/$output
done
