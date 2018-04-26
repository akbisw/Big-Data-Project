import sys
from pyspark import SparkContext
from csv import reader
from datetime import datetime
import pytz

sc = SparkContext()
citibikeRdd = sc.textFile(sys.argv[1])
citibikeRdd = citibikeRdd.mapPartitions(lambda x : reader(x))

def try_parsing_date(text):
    for fmt in ('%Y-%m-%d %H:%M:%S', '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found for this date: ' + text)

def map_date_to_epoch(x):
    # Retrieve the start and end times from list x
    local_start_time = x[1].strip()
    local_end_time = x[2].strip()
    # define timezones from pytz library
    utc = pytz.utc
    eastern = pytz.timezone('US/Eastern')
    # Create a datetime object for each time
    date_start = try_parsing_date(local_start_time)
    date_end = try_parsing_date(local_end_time)
    # Normalize (daylight) and localize (eastern time zone) the datetime objects
    date_start_est = eastern.normalize(eastern.localize(date_start,is_dst=True))
    date_end_est = eastern.normalize(eastern.localize(date_end,is_dst=True))
    # Convert to UTC
    date_start_utc = date_start_est.astimezone(utc)
    date_end_utc = date_end_est.astimezone(utc)
    # Convert to epoch
    ts_start = (date_start_utc - datetime(1970, 1, 1, tzinfo=utc)).total_seconds()
    ts_end = (date_end_utc - datetime(1970, 1, 1, tzinfo=utc)).total_seconds()
    # Write the epoch back into the list
    x[1] = int(ts_start)
    x[2] = int(ts_end)
    # return the list as a csv string
    return ",".join(str(y) for y in x) 

citibikeRdd = citibikeRdd.map(map_date_to_epoch).saveAsTextFile("data/citibike2013to2017")
