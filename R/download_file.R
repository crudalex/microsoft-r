cwd = getwd()
setwd(cwd)

if (!file.exists("data")){
  dir.create("data")
}
datadir = file.path(cwd, "data")

src = "https://data.baltimorecity.gov/api/views/dz54-2aru/rows.csv?accessType=DOWNLOAD"
dest = file.path(datadir, 'cameras.csv')
download.file(url = src, destfile = dest, method = 'auto')
list.files(datadir)

dl_date = date()
