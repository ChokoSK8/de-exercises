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

def main():
	page_content = getPageContent(weether_url);
	if (not page_content):
		return ;
	displayHtmlContent(page_content)
	pass


if __name__ == '__main__':
    main()
