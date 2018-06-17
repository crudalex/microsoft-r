rm(list = ls())

cwd = getwd()
setwd(cwd)
cwd

datadir = file.path(cwd, "data")
datafile = file.path(datadir, 'cameras.xlsx')
list.files(datadir)

install.packages('xlsx')
library(xlsx)

cameraDF2 = read.xlsx(datafile, quote = '"')
head(cameraDF2)
