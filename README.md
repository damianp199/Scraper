# Scraper
To run program, make sure you have: Python 3.0 or higher, Scrapy (on Windows use Anaconda or other package manager, for further info please see https://docs.scrapy.org/en/latest/intro/install.html)

Also needed: Tkinter, bs4, json, PyMongo, python-dns

This program is called Scraper 1.0, the first and only release. What it does is just basically enter pages and download specific data with prices about kitesurfing courses in Pomeranian Voivodeship. After program opens, you can choose between eleven cities listed below. Data are saved to a JSON file in location of the program, to export to MongoDB Database follow instructions down below.

Program shows 3 windows, one shows results of searching phrase kitesurfing + city + kurs in search engine (with some cities, sometimes, windows is empty, it is because of captcha, I tried to get past it but it does not always work, just try "Sopot"). Second one shows list of available kitesurfing schools in Pomerania from local tourist portal "pomorskie.travel". Third one shows results of scrapped data from pages (page choice is selective), data is readable and always up to date :) To download and parse data I used Scrapy, Beautiful Soup and Requests.

To scrap again with another city, please re-open the program - that is obviously a program's feature :)

To upload files to MongoDB database in cloud please: -uncomment all 'Send.(...)' classes from 'def Conditions()' && -fill all 5 "client = MongoClient()" in class "Send" with your client connection string, example: client = MongoClient( "mongodb+srv://user1:password1@scrapycluster.3ojmw.mongodb.net/ScrapyCluster?retryWrites=true&w=majority")

AVAILABLE CITIES! (for one and only 1.0 release): Gdańsk, Sopot, Gdynia, Hel, Jastarnia, Kuźnica, Jurata, Chałupy, Puck, Krynica Morska, Wicko.

Please be patient while executing, it can take up to 1 minute, it is mostly because of sending files to database.
