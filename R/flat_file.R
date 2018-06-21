rm(list = ls())
cwd = getwd()
setwd(cwd)
cwd

datadir = file.path(cwd, "data")
datafile = file.path(datadir, 'cameras.csv')
list.files(datadir)

cameraDF = read.table(datafile, header = T, sep = ',')
head(cameraDF)

cameraDF2 = read.csv(datafile, quote = '"')
head(cameraDF2)
