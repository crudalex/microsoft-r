
# install the required packages
install.packages("devtools")
install.packages("nycflights13")
install.packages(c("magrittr", "DBI", "assertthat","tibble"))
devtools::install_github("RevolutionAnalytics/dplyrXdf")
library(dplyrXdf)
library(nycflights13)
library(magrittr)

# inspect the data
# Notice we have a column carrier
# the goal is to list carriers by their average delay time

head(flights)


# Write the data as an xdf file
# rxDataFrameToXdf is deprecated - this is is to just showcase the step
# Use rxDataStep as in the next piece of code
flightsXdf <- rxDataFrameToXdf(flights, "flights.xdf", overwrite = TRUE)
head(flightsXdf)
rm(flightsXdf)

flightsXdf <- rxDataStep(flights, "flights.xdf", overwrite = TRUE)
head(flightsXdf)

# Using RxDataStep load data for the first six months of 2013
flights_rx1 <- rxDataStep(flights, outFile = "flights_rx1.xdf",
                          rowSelection = month <= 6 & year == 2013,
                          overwrite = TRUE)
head(flights_rx1)

# variable transformations
# calculate distances in km and calculate average delay for each flight
flights_rx2 <- rxDataStep(flights_rx1, outFile = "flights_rx2.xdf",
                          transforms = list(dist_km = distance * 1.6093,
                                            delay = (arr_delay + dep_delay) / 2),
                          overwrite = TRUE)
head(flights_rx2)

# convert carrier into a factor variable (or rxSummary will complain)
flights_rx3 <- rxFactors(flights_rx2,
                         factorInfo = "carrier",
                         outFile = "flights_rx3.xdf",
                         overwrite = TRUE)

# use rxSummary to get the summary table(s) 
rxSummary(~delay:carrier + dist_km:carrier,
          data = flights_rx3,
          summaryStats = c("mean", "sum"))

# Store the above for further processing
flights_rx4 <- rxSummary(~delay:carrier + dist_km:carrier,
                         data = flights_rx3,
                         summaryStats = c("mean", "sum"))


# extract the desired tables - delay means and total distances from the rxSummary output
flights_carrier_delay_means <- flights_rx4$categorical[[1]][c("carrier", "Means")]
names(flights_carrier_delay_means)[2] <- "mean_delay"
head(flights_carrier_delay_means)

flights_carrier_dist_sums <- flights_rx4$categorical[[2]][c("carrier", "Sum")]
names(flights_carrier_dist_sums)[2] <- "sum_dist"

# merge the tables together
flights_rx5 <- merge(flights_carrier_delay_means,
                     flights_carrier_dist_sums,
                     by = "carrier", all = TRUE)

# sort the results by delay in descending order
flights_rx5 <- flights_rx5[order(flights_rx5$mean_delay, decreasing = TRUE),]

head(flights_rx5)

###############################################################################

# the equivalent in dplyrXdf would be the following pipeline:
# flightsXdf <- rxDataStep(flights, "flights.xdf", overwrite = TRUE)
flightsSmry <- flightsXdf %>%
    filter(month <= 6, year == 2013) %>%
    mutate(dist_km = distance * 1.6093, delay = (arr_delay + dep_delay) / 2) %>%
    group_by(carrier) %>%
    summarise(mean_delay = mean(delay), sum_dist = sum(dist_km)) %>%
    arrange(desc(mean_delay))

head(flightsSmry)

###############################################################################

# Two-table verbs
# Lets say we have a table of airports and we wnat to join it to the flights table
airportsXdf <- rxDataStep(airports, "airports.xdf", overwrite = TRUE)
head(airportsXdf)

# notice that we have the column "faa" that gives the airport code
# to join the "airports" table to the "flights" table "dest" column  
flightsJoin <- left_join(
                         flightsXdf %>% select(year:day, hour, origin, dest, tailnum, carrier),
                         airportsXdf,
                         by = c("dest" = "faa")
                         )

head(flightsJoin)

# Cleanup
if (file.exists("flights.xdf")) file.remove("flights.xdf")
if (file.exists("flights_rx1.xdf")) file.remove("flights_rx1.xdf")
if (file.exists("flights_rx2.xdf")) file.remove("flights_rx2.xdf")
if (file.exists("flights_rx3.xdf")) file.remove("flights_rx3.xdf")
if (file.exists("airports.xdf")) file.remove("airports.xdf")
