# Convert a text file to xdf
txt <- RxTextData("orange_small_test.data", delimiter = "\t")
xdf <- RxXdfData("orange.xdf")
rxDataStep(txt, xdf, overwrite = TRUE)

head(xdf)
rxGetVarInfo(xdf)

# The first 190 variables are numerical and the last 41 are
# categorical
factorCols <- paste("Var", 191:230, sep = "")
xdfFactors <- RxXdfData("orange_factors.xdf")
rxFactors(xdf, factorCols, outFile=xdfFactors, overwrite = TRUE)
rxGetVarInfo(xdfFactors)

# determine which columns have a large amount of missing values
# e.g. 50%
summData <- rxSummary( ~ ., xdfFactors)$sDataFrame
summData
missingThreshold <- 0.5
summData$missProp <- summData$MissingObs/dim(xdf)[1]
missingColumns <- summData[summData$missProp > missingThreshold, 1]
missingColumns

# which columns have a large number of factors (say over 50)
myStr <- rxGetVarInfo(xdfFactors)
levelThreshold <- 50
nLevels <- unlist(lapply(myStr, function(x) { length(x$levels)}))
ix <- which(nLevels > levelThreshold)
lotsOfLevels <- names(nLevels)[ix]
lotsOfLevels

# because xdf is a column based store we can use varsToDrop
# in our object rather than having to create a new xdf
xdfToUse <- RxXdfData("orange_factors.xdf", varsToDrop = unique(c(missingColumns, lotsOfLevels)))
rxGetVarInfo(xdfToUse)

# Cleanup
if (file.exists("orange.xdf")) file.remove("orange.xdf")
if (file.exists("orange_factors.xdf")) file.remove("orange_factors.xdf")
