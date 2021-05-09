from bs4 import BeautifulSoup
import urllib.request
import time
from tkinter import Tk, messagebox


class WebScraper:

    def __init__(self):
        root = Tk()
        root.withdraw()

    def scrape(self, url, update_rate):
        html_parsed_before = ""

        while True:

            print(f"Sending request to {url}")
            response = urllib.request.urlopen(url)
            html = response.read()

            html_parsed = BeautifulSoup(html, "html.parser")
            
            if html_parsed != html_parsed_before:
                print(f"Site Updated! Website '{url}' is different from the last request.")
                messagebox.showinfo(title="Site Updated", message=f"{url} has been updated and is different from the last request!")

            html_parsed_before = html_parsed
            response.close()

            time.sleep(update_rate) #Wait for x seconds before sending next request


my_scraper = WebScraper()
target_url = input("Please Enter URL: ")

my_scraper.scrape(target_url, 1)
