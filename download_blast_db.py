#!/usr/bin/python
"""
Python script which opens an ftp connection at 'ftp.ncbi.nlm.nih.gov' and 
downloads all files needed to have a complete BLAST database.
After each download, the .tar.gz file will be removed and the extracted files will be 
put in a new folder named 'blast_db'
"""
from ftplib import FTP
import tarfile
import os

# open ftp connection
ftp = FTP('ftp.ncbi.nlm.nih.gov') 
ftp.login()
# switch to correct directory
ftp.cwd('blast/db/')
filenames = ftp.nlst()
# search only tar.gz files
tar_gz_files = [f for f in filenames if f.endswith(".tar.gz")]
num_files = len(tar_gz_files)
print "Found {} files.".format(num_files)

# create folder only if something will be downloaded
if num_files > 0:
	if not os.path.exists("blast_db"):
		try:
			os.makedirs("blast_db")
		except OSError as e:
			print "An error occurred: {}".format(e)
			ftp.quit()
else:
	print "No files found."

# start download files
counter = 0
for file in tar_gz_files:
	ftp.retrbinary('RETR ' + file, open("blast_db/" + file, 'wb').write)
	# extract downloaded file
	tar_file = tarfile.open("blast_db/" + file, "r:gz")
	tar_file.extractall("blast_db")
	tar_file.close()
	
	# remove extracted file
	os.remove("blast_db/" + file)
	
	counter += 1
	print "The {} file has been processed. {} files has been downloaded.".format(file, counter)

print "Process completed"
# close connection
ftp.quit()
