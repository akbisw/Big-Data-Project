# Download Datasets
cd data
if [ ! -f weather ]; then
    wget https://ndownloader.figshare.com/files/4975923 --no-check-certificate -O weather;
fi
if [ ! -f citibike ]; then
    wget https://ndownloader.figshare.com/files/4944970 --no-check-certificate -O citibike;
fi
# Prepare HDFS
sh load-hdfs-structure
sh load-spatial
sh load-datasets
