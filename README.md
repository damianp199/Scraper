# Scraper
To run the program, make sure you have: Python 3.0 or higher, Scrapy (on Windows use Anaconda or another package manager, for further info please see https://docs.scrapy.org/en/latest/intro/install.html)

Also needed: Tkinter, bs4, JSON, PyMongo, python-DNS

This program is called Scraper 1.0, the first and the only release. What it does is just enters pages and downloads specific data with prices about kitesurfing courses in Pomeranian Voivodeship. After the program opens, you can choose between eleven cities, listed below. Data is saved to a JSON file in a location of the program, to export to MongoDB Database, follow the instructions down below.

The program shows 3 windows, one shows results of searching phrases: kitesurfing, city, and course in the search engine. The second one shows a list of available kitesurfing schools in Pomerania from the local tourist portal "pomorskie. travel". The third one shows results of scrapped data from pages (page choice is selective), data is readable and always up to date :) To download and parse data I used Scrapy, Beautiful Soup, and Requests.

To scrap again with another city, please re-open the program - that is obviously a program's feature :)

To upload files to the MongoDB database in the cloud please: -uncomment all 'Send. (...)' classes from 'def Conditions()' && -fill all 5 "client = MongoClient()" in class "Send" with your client connection string, example: client = MongoClient( "mongodb+srv://user1:password1@scrapycluster.3ojmw.mongodb.net/ScrapyCluster?retryWrites=true&w=majority")

AVAILABLE CITIES! (for only 1.0 release): Gdańsk, Sopot, Gdynia, Hel, Jastarnia, Kuźnica, Jurata, Chałupy, Puck, Krynica Morska, Wicko.

Please be patient while executing, it can take up to 1 minute, and it is mostly because of sending files to the database.
