install.packages("tm")
library(tm)

# grab the text from a document
SQLServerTxt <- "SQLServer.txt"
textFile <- scan(SQLServerTxt, what = "character", sep = "\n")
str(textFile)

# work out where the book starts and finishes.
limits <- local({
  limitTerms <- c("Mission-Critical Performance", "accessed May 15, 2013")
  sapply(limitTerms, grep, textFile, USE.NAMES=FALSE)  + c(1, -1)
})
limits

# put the relevent part of the document into a data.frame
textFile <- textFile[limits[1]:limits[2]]

# The transform function to remove parts of the text e.g. punctuation, stop words
tmTransform <- function(dataList) {
    x <- dataList$text
    x <- tolower(x)
    x <- removePunctuation(x)
    x <- removeNumbers(x)
    x <- removeWords(x, stopwords("english"))
    dataList$text <- x
    return(dataList)
}

# create an XDF object for output
cdXdf <- RxXdfData("SQLServerTxt.xdf")


# run the transformation on each chunk
rxDataStep(inData = data.frame(text=textFile, stringsAsFactors=FALSE), 
           outFile = cdXdf,
           overwrite=TRUE,
           transformFunc = tmTransform,
           transformPackages = "tm",
           rowsPerRead=100)

# original
head(textFile, 10)
# cleaned
head(cdXdf, 10)

# Cleanup
if (file.exists("SQLServerTxt.xdf")) file.remove("SQLServerTxt.xdf")