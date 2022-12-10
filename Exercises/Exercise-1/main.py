import requests
import os
from os.path import exists
from zipfile import ZipFile
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time
import random

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

def	downloadUri(uri):
	response = requests.get(uri)
	if response.status_code == 200:
		spliter = uri.split('/');
		filename = spliter[len(spliter) - 1];
		file_location = "./" + download_dir + "/"; 
		print("Downloading " + filename);
		if not exists(file_location + filename):
			if open(file_location + filename, "wb").write(response.content) == False:
				print("Cannot write content in " + file_location + filename);
			else:
				print(filename + " downloaded !")
				spliter = filename.split('.');
				if spliter[len(spliter) - 1] == "zip":
					lenLoop = len(spliter) - 2;
					i = 0;
					unzipFile = "";
					while i <= lenLoop:
						unzipFile += spliter[i];
						i += 1;
					print("Extracting " + unzipFile);
					with ZipFile(file_location + filename, 'r') as zObject:
						zObject.extractall(path=file_location);
					zObject.close();
					os.remove(file_location + filename);
					print("Zip file removed");
		else:
			print("File already exist");
	else:
		print('URL passed is invalid');

async def	downloadUriAsync(dirname, uri):
	async with aiohttp.ClientSession() as session:
		async with session.get(uri) as response:
			if response.status == 200:
				spliter = uri.split('/');
				filename = spliter[len(spliter) - 1];
				file_location = "./" + dirname + "/"; 
				print("Downloading " + filename);
				content = await response.read();
				if not exists(file_location + filename):
					if open(file_location + filename, "wb").write(content) == False:
						print("Cannot write content in " + file_location + filename);
					else:
						print(filename + " downloaded !")
						spliter = filename.split('.');
						if spliter[len(spliter) - 1] == "zip":
							lenLoop = len(spliter) - 2;
							i = 0;
							unzipFile = "";
							while i <= lenLoop:
								unzipFile += spliter[i];
								i += 1;
							print("Extracting " + unzipFile);
							with ZipFile(file_location + filename, 'r') as zObject:
								zObject.extractall(path=file_location);
							zObject.close();
							os.remove(file_location + filename);
							print("Zip file removed");
				else:
					print("File already exist");
			else:
				print('URL passed is invalid');

def	downloadUrisMultiThreads(dirname, uris):
	with ThreadPoolExecutor(max_workers=len(uris)) as executor:
		executor.map(downloadUri, uris);
				

def main():
	createDir(download_dir);
	downloadUrisMultiThreads(download_dir, download_uris);
	pass


if __name__ == '__main__':
    main()
