cat file.txt | perl -ne 'print if (/^\d{3}-\d{3}-\d{4}$/ or /^\(\d{3}\) \d{3}-\d{4}$/ )'
