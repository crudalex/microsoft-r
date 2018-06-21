# Configure Data and Working Directories
projectDir <- getwd()
if (dir.exists(file.path(projectDir, "data")) == FALSE) { dir.create(file.path(projectDir, "data")) }
dataRead <- file.path(projectDir, "data")
dataWrite <- dataRead

# -------------------------------------------------------------------------

## define data file to read 
list.files(dataRead)
sqlperfCsv <- file.path(dataRead, "DEVCIWSFUJSQL1_PerfLog_20151008.csv")

# Build a data frame in memory for analysis
sqlperfDF1 <- read.table(file = sqlperfCsv, header = TRUE, sep = ",")

# Clean non-numeric columns
filter1 <- unlist(lapply(sqlperfDF1, is.numeric))
sqlperfDF2 <- sqlperfDF1[ , filter1]

# Clean zero and na columns
filter2 <- unlist(lapply(sqlperfDF2, function(x){ x != 0 & !is.na(x)}))
sqlperfDF3 <- sqlperfDF2[ , filter2]

# Calculate corelation cofficients between to database transactions and other metrics
grep("Transaction", colnames(sqlperfDF3), value = T)
sqlCor <- cor(x = sqlperfDF3$DEVCIWSFUJSQL1_MSSQL_DBAAGINS1_Databases_Total_Transactions_sec, 
              y = sqlperfDF3, 
              use = "na.or.complete")

sqlCorCsv <- file.path(dataWrite, "DEVCIWSFUJSQL1_PerfLog_20151008_Corelation.csv")
write.csv(x = sqlCor, file = sqlCorCsv)

