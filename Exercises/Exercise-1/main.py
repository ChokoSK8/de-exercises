import requests
import os

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]

download_dir = "downloads"

	# FUNCTIONS #

def	createDir(name_dir):
	path = os.path.join('./', name_dir);
	if not os.path.exists(path):
		os.mkdir(path);

def	downloadUris(uris):
	for uri in uris:
		response = requests.get(uri)
		if response.status_code == 200:

def main():
	createDir(download_dir)
	downloadUris(download_uris)
	pass


if __name__ == '__main__':
    main()
