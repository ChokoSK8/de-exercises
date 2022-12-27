import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
from os.path import exists

weether_uri = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/";

def	getPageContent(uri):
	response = requests.get(uri);
	if (response.status_code == 200):
		return (response.content);

def	displayHtmlContent(html_content):
	soup = BeautifulSoup(html_content, 'html.parser');
	print(soup.prettify());

def	getStrInQuotes(string, firstQuotePos):
	counter = firstQuotePos;
	strInQuotes = "";
	while string[counter] != '"':
		strInQuotes += string[counter];
		counter += 1;
	return strInQuotes;

def getHrefInStr(strWithHref):
	hrefPos = strWithHref.find("href=");
	href = getStrInQuotes(strWithHref, hrefPos + 6);
	print("href = |" + href + "|");
	return href;

def	getHrefByDate(html_content, html_wrapper, date):
	soup = BeautifulSoup(html_content, 'html.parser');
	elements = soup.find_all(html_wrapper);
	for element in elements:
		if str(element).find(date) > 0:
			strWithHref = str(element);
	href = getHrefInStr(strWithHref);
	return href;

def	createDir(dirname):
	path = os.path.join('./', dirname);
	if not os.path.exists(path):
		os.mkdir(path);

def	downloadInDir(uri, dirname):
	createDir(dirname);
	response = requests.get(uri)
	if response.status_code == 200:
		spliter = uri.split('/');
		filename = spliter[len(spliter) - 1];
		file_location = "./" + dirname + "/";
		print("Downloading " + filename);
		if not exists(file_location + filename):
			if open(file_location + filename, "wb").write(response.content) == False:
				print("Cannot write content in " + file_location + filename);
			else:
				print(filename + " downloaded !")

def	getDfFromCsv(csv_path):
	df = pd.read_csv(csv_path);
	df.head();
	return df;

def getHighestOf(df, column):
	highest = df[column].astype(float, errors='ignore').max();
	return highest;

def	printColumns(df):
	cols = df.columns;
	for col in cols:
		print("col: " + col);

def	getDtypeOfColumn(df, column):
	rows = df[column];
	for row in rows:
		print(type(row));

def	convertToFloatInColumn(df, column):
	df[column] = df[column].astype(float, errors='ignore');
	return (df);

def	convertToFloat():
	x = "12s";
	print("x type: " + str(type(x)));
	x = float(x);
	print("x new type: " + str(type(x)));

def	countFloatValueInColumn(df, column):
	rows = df[column];
	n = 0;
	for row in rows:
		if (type(row) == float):
			n += 1;
	print("Number of float: " + str(n));

def main():
#	html_content = getPageContent(weether_uri);
#	if (not html_content):
#		return ;
#	href = getHrefByDate(html_content, "tr", "2022-02-07 14:03");
	href = "A0002453848.csv";
#	downloadInDir(weether_uri + href, "download");
	df = getDfFromCsv("./download/" + href);
	countFloatValueInColumn(df, "HourlyDryBulbTemperature");
	df = convertToFloatInColumn(df, "HourlyDryBulbTemperature");
	countFloatValueInColumn(df, "HourlyDryBulbTemperature");
	getDtypeOfColumn(df, "HourlyDryBulbTemperature");
	highest = getHighestOf(df, "HourlyDryBulbTemperature");
	print(highest);
	pass


if __name__ == '__main__':
    main()


# need to use array to catch the line with the date
# find the beacon that wraps the date and the href
