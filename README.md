# Goals
1. Build the infrastructure to find temporal correlations between datasets (using Spark or Hadoop). Event detection: find correlations without and with event detection (any technique), to see if they can find correlations with rare events.
2. Choose some correlations that are potentially interesting and try to explain / come up with hypotheses, etc. For instance, how is the correlation for specific neighborhoods / zip codes?
3. Groups have the freedom to choose the temporal resolutions they will work on -- the more the merrier -- and they should also play with correlations for specific neighborhoods / zip codes when trying to explain a relationship. Any decision taken during the project (data cleaned, chosen resolution, architecture, etc.) must be written down on the final report.
4. Use Spearman's rank as a correlation measure.

# Run Project
1. Clone the repo: `git clone https://github.com/akbisw/Citi-Bike-Big-Data.git`
2. Change dir into the repo: `cd Citi-Bike-Big-Data`
3. Run the setup script to download datasets and setup hdfs: `sh setup.sh`
4. Run the experiment: `run_experiment.sh`

Charts and pretty print results have not been scripted yet.

But the correlations from our test run can be found here: https://github.com/akbisw/Citi-Bike-Big-Data/tree/master/correlations and the relationship result can be found here: https://github.com/akbisw/Citi-Bike-Big-Data/blob/master/performance-evaluation/output-events/weather-citibike-hour-city-events-restricted
