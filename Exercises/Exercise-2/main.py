import requests
import pandas
from bs4 import BeautifulSoup

weether_url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/";

def	getPageContent(url):
	response = requests.get(url);
	if (response.status_code == 200):
		return (response.content);

def	displayHtmlContent(html_content):
	soup = BeautifulSoup(html_content, 'html.parser');
	print(soup.prettify());

def	getDateIndex(array, date):
	index = 0;
	len_array = len(array);
	while index < len_array - 1:
		print(array[index]);
		print(index);
		if array[index].find(date) > 0:
			return (index);
		index += 1;
	return (-1);

def	findBeaconFromArray(html_array, date):
	index = getDateIndex(html_array, date);
	if (index < 0):
		print("|" + date + "| not found");
	else:
		print("index of |" + date + "| is " + str(index));

def	getHtmlPageInArray(html_content):
	soup = BeautifulSoup(html_content, 'html.parser');
#	string = soup.get_text();
	string = soup.prettify();
	array = string.split("/n");
	return (array);

def main():
	page_content = getPageContent(weether_url);
	if (not page_content):
		return ;
#	displayHtmlContent(page_content);
	html_array = getHtmlPageInArray(page_content);
	findBeaconFromArray(html_array, "2022-02-07 14:03");
	pass


if __name__ == '__main__':
    main()


# need to use array to catch the line with the date
# find the beacon that wraps the date and the href
