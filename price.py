import requests
from bs4 import BeautifulSoup
import time

def convert_price(s):
	final = ""
	for i in s:
		if i == ".":
			break
		if i >= '0' and i<='9':
			final += i
	return final



def scrape(URL, website):
	curr_price = ""
	url = URL
	headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
	page = requests.get(url, headers=headers)
	soup = BeautifulSoup(page.content, 'lxml')
	
	if website == 1:
		price = soup.find(id="priceblock_dealprice")
		if price is not None:
			curr_price = convert_price(price.text) 
			print(curr_price)
		else:
			price = soup.find("span", id="priceblock_ourprice")
			curr_price = convert_price(price.text) 
			print(curr_price)
	elif website == 2:
		price = soup.find('div', attrs={'class': '_1vC4OE _3qQ9m1'})
		if price is None:
			print("Error!")
		else:
			curr_price = convert_price(price.text) 
			print(curr_price)
	elif website == 3:
		price = soup.find('span', {'class': 'pdp-price'})
		print(price)
		if price is None:
			print("Error")
		else:
			curr_price = convert_price(price.text) 
			print(curr_price)
	else:
		print("Error!")

	return curr_price

if __name__== "__main__":

	url = 'https://www.myntra.com/socks/levis/levis-men-pack-of-3-shoe-liners/2283078/buy'
	website = 3
	scrape(url, website)