# download_blast_db
Python script which opens an ftp connection at 'ftp.ncbi.nlm.nih.gov' and 
downloads all files needed to have a complete BLAST database. <br>
After each download, the .tar.gz file will be removed and the extracted files will be 
put in a new folder named 'blast_db'
