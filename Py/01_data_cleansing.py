#!/usr/bin/env python

import os
workdir = os.getcwd()
datadir = os.path.join(workdir, 'data')
datafile = os.path.join(datadir, 'orange_small_test.csv')

#  Convert a text file to xdf# Convert a text file to xdf
# txt <- RxTextData("orange_small_test.data", delimiter = "\t")
# xdf <- RxXdfData("orange.xdf")
# rxDataStep(txt, xdf, overwrite = TRUE)
import pandas as pd
pd.options.mode.use_inf_as_na = True
df = pd.read_table(datafile, sep='\t', header=0)

# head(xdf)
# rxGetVarInfo(xdf)
df.head(5)
df.describe().transpose()

# The first 190 variables are numerical and the last 41 are
# categorical
# factorCols <- paste("Var", 191:230, sep = "")
# xdfFactors <- RxXdfData("orange_factors.xdf")
# rxFactors(xdf, factorCols, outFile=xdfFactors, overwrite = TRUE)
import copy
factors = copy.deepcopy(df)
factorCols = ["Var" + str(i) for i in range(191, 230) ]
factors[factorCols] = factors[factorCols].astype('category')

# rxGetVarInfo(xdfFactors)
factors.describe().transpose()

# # determine which columns have a large amount of missing values
# # e.g. 50%
# summData <- rxSummary( ~ ., xdfFactors)$sDataFrame
# summData
# missingThreshold <- 0.5
# summData$missProp <- summData$MissingObs/dim(xdf)[1]
missingThreshold = .5
factors = factors.loc[:, factors.isnull().mean() < missingThreshold]


# missingColumns <- summData[summData$missProp > missingThreshold, 1]
# missingColumns


# # which columns have a large number of factors (say over 50)
# myStr <- rxGetVarInfo(xdfFactors)
# levelThreshold <- 50
# nLevels <- unlist(lapply(myStr, function(x) { length(x$levels)}))
# ix <- which(nLevels > levelThreshold)
# lotsOfLevels <- names(nLevels)[ix]
# lotsOfLevels
#
# # because xdf is a column based store we can use varsToDrop
# # in our object rather than having to create a new xdf
# xdfToUse <- RxXdfData("orange_factors.xdf", varsToDrop = unique(c(missingColumns, lotsOfLevels)))
# rxGetVarInfo(xdfToUse)
#
# # Cleanup
# if (file.exists("orange.xdf")) file.remove("orange.xdf")
# if (file.exists("orange_factors.xdf")) file.remove("orange_factors.xdf")
