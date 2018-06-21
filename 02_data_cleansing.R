## set up pointer to xdf mortgage data
mortgages <- RxXdfData("mortgages.xdf")
head(mortgages)

# get the global min and max credit scores
minScore <- rxGetVarInfo(mortgages)[["creditScore"]][["low"]]
maxScore <- rxGetVarInfo(mortgages)[["creditScore"]][["high"]]
minScore
maxScore

# Create transform function to normalize Credit Score
# and create a boolean column to show if the score is more than 0.5
simply_normalize <- function(lst) {
    lst[["normCreditScore"]] <- as.numeric((lst[["creditScore"]] - minCreditScore) / (maxCreditScore - minCreditScore))
    lst[["moreThanHalf"]] <- lst[["normCreditScore"]] > 0.5
    return(lst)
}

# Create an xdf file mortgagesNorm.xdf from the original file morgages.xdf
# This is just to keep a pristine copy of mortgages.xdf
outputFile <- file.path(getwd(), "mortgagesNorm.xdf")
mortgagesNorm <- rxImport(inData = mortgages, outFile = outputFile)

# run the transform function on each block in the datastep
# this adds two columns to the data and writes it back to the file
rxDataStep(inData = mortgagesNorm,
           outFile = mortgagesNorm,
           transformFunc = simply_normalize,
           transformObjects = list(minCreditScore = minScore, maxCreditScore = maxScore),
           append = "cols",
           overwrite = TRUE)
mortgagesNorm <- RxXdfData("mortgagesNorm.xdf")
head(mortgagesNorm)


# check the new variables
rxGetVarInfo(data = mortgagesNorm)

# Cleanup
if (file.exists("mortgagesNorm.xdf")) file.remove("mortgagesNorm.xdf")

