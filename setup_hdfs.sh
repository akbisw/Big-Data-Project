# Download Datasets
cd data
wget https://ndownloader.figshare.com/files/4975923 --no-check-certificate -O weather
wget https://ndownloader.figshare.com/files/4944970 --no-check-certificate -O citibike
# Prepare HDFS
sh load-hdfs-structure
sh load-spatial
