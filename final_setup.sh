#!/usr/bin/env bash

# CD to data directory and download citibike datasets 2013 to 2017
cd data/citibike_raw
sh download_data.sh

# Extract everything and merge all the citi bike datasets into one file
sh extract_data.sh
# Merge to filename citibike2013to2017
sh merge_data.sh

# Upload the merged dataset to hdfs
hdfs dfs -put citibike2013to2017

# Run the spark program to 
# 1. clean the merged citi bike dataset
# 2. convert the date to epoch format
# ... more things 
# output directory is set to data/citibike2013to2017
spark-submit clean-citibike.py citibike2013to2017
