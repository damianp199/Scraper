from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
from tkinter import ttk
import scrapy
from scrapy.crawler import CrawlerProcess
import json
from pymongo import MongoClient
import datetime


def root_Window():
    global g_entry_root_01
    global g_entry_root_02
    global dzisiejsza_data
    dzisiejsza_data = str(datetime.datetime.now())


    root = Tk()
    root.geometry("590x376")
    root.title("Scraper")

    mainframe_root = LabelFrame(root,
                                padx=177,
                                pady=136)
    mainframe_root.grid(row=0,
                        column=0)

    #     my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/Damian/Desktop/splash.jpg"))
    #     myLabel = Label(image = my_img1).place(x = 0, y = 0, relwidth = 1, relheight = 1)

    greetext2_root = 'Witaj \n Wybierz sport oraz wprowadź miejscowość'

    Label(mainframe_root,
          text=greetext2_root).grid(row=1,
                                    column=0,
                                    columnspan=2)

    option_list = ('Kitesurfing',)
    g_entry_root_01 = StringVar(mainframe_root)
    g_entry_root_01.set(option_list[0])
    OptionMenu(mainframe_root, g_entry_root_01, *option_list).grid(row=2,
                                                                   column=0)

    g_entry_root_02 = Entry(mainframe_root,
                            width=15)

    g_entry_root_02.insert(0, 'Miasto')

    g_entry_root_02.grid(row=2,
                         column=1)

    Button(mainframe_root,
           text='Wykonaj',
           command=Conditions).grid(row=3,
                                    column=0,
                                    columnspan=2)

    mainloop()


def Conditions():
    sport = g_entry_root_01.get()
    miasto = g_entry_root_02.get()
    sport = sport.lower()
    miasto = miasto.lower()

    if sport == 'kitesurfing' and \
            miasto == 'gdansk' or \
            miasto == 'sopot' or \
            miasto == 'gdynia' or \
            miasto == 'gdańsk' or \
            miasto == 'trojmiasto':
        Window_trojmiasto()
        Window_bing()
        # Send.Trojmiasto()
    elif sport == 'kitesurfing' and \
            miasto == 'hel' or \
            miasto == 'jastarnia' or \
            miasto == 'chałupy' or \
            miasto == 'chalupy' or \
            miasto == 'jurata' or \
            miasto == 'kuznica' or \
            miasto == 'kuźnica':
        Window_polwysep_helski()
        Window_bing()
        # Send.PH()
    elif sport == 'kitesurfing' and miasto == 'puck':
        Window_puck()
        Window_bing()
        # Send.Puck()
    elif sport == 'kitesurfing' and miasto == 'krynica morska':
        Window_Krynica_Morska()
        Window_bing()
        # Send.Krynica()
    elif sport == 'kitesurfing' and miasto == 'wicko':
        Window_Wicko()
        Window_bing()
        # Send.Wicko()

    elif sport == 'żeglarstwo':
        pass
    else:
        messagebox.showinfo("Błąd", "Nie znaleziono danych dla wybranej miescowości")


class Send():

    @staticmethod
    def Trojmiasto():
        client = MongoClient(
            "mongodb+srv://user:asdzx@scrapycluster.3ojmw.mongodb.net/ScrapyCluster?retryWrites=true&w=majority")
        db = client["Scrapy"]
        test = db["Scrap"]
        with open('tr1Sopotsurf.com.json') as file:
            file_data = json.load(file)
        test.insert_many(file_data) if isinstance(file_data, list) else test.insert_one(file_data)

        with open('tr2onewave.pl.json') as file:
            file_data = json.load(file)
        test.insert_many(file_data) if isinstance(file_data, list) else test.insert_one(file_data)

        with open('tr3aloha.pl.json') as file:
            file_data = json.load(file)
        test.insert_many(file_data) if isinstance(file_data, list) else test.insert_one(file_data)

        with open('tr4bssurf.pl.json') as file:
            file_data = json.load(file)
        test.insert_many(file_data) if isinstance(file_data, list) else test.insert_one(file_data)

    @staticmethod
    def PH():
        client = MongoClient(
            "mongodb+srv://user:asdzx@scrapycluster.3ojmw.mongodb.net/ScrapyCluster?retryWrites=true&w=majority")
        db = client["Scrapy"]
        Test = db["Scrap"]
        with open('ph1kitecrew.pl.json') as file:
            file_data = json.load(file)
        Test.insert_many(file_data) if isinstance(file_data, list) else Test.insert_one(file_data)

        with open('ph2polsporty.pl.json') as file:
            file_data = json.load(file)
        Test.insert_many(file_data) if isinstance(file_data, list) else Test.insert_one(file_data)

        with open('ph3easy-surfcenter.pl.json') as file:
            file_data = json.load(file)
        Test.insert_many(file_data) if isinstance(file_data, list) else Test.insert_one(file_data)

        with open('ph5szkola.abcsurf.pl.json') as file:
            file_data = json.load(file)
        Test.insert_many(file_data) if isinstance(file_data, list) else Test.insert_one(file_data)

    @staticmethod
    def Wicko():
        client = MongoClient(
            "mongodb+srv://user:asdzx@scrapycluster.3ojmw.mongodb.net/ScrapyCluster?retryWrites=true&w=majority")
        db = client["Scrapy"]
        Test = db["Scrap"]
        with open('wicko.json') as file:
            file_data = json.load(file)
        Test.insert_many(file_data) if isinstance(file_data, list) else Test.insert_one(file_data)

    @staticmethod
    def Krynica():
        client = MongoClient(
            "mongodb+srv://user:asdzx@scrapycluster.3ojmw.mongodb.net/ScrapyCluster?retryWrites=true&w=majority")
        db = client["Scrapy"]
        Test = db["Scrap"]
        with open('krynica.json') as file:
            file_data = json.load(file)
        Test.insert_many(file_data) if isinstance(file_data, list) else Test.insert_one(file_data)

    @staticmethod
    def Puck():
        client = MongoClient(
            "mongodb+srv://user:asdzx@scrapycluster.3ojmw.mongodb.net/ScrapyCluster?retryWrites=true&w=majority")
        db = client["Scrapy"]
        Test = db["Scrap"]
        with open('puck.json') as file:
            file_data = json.load(file)
        Test.insert_many(file_data) if isinstance(file_data, list) else Test.insert_one(file_data)


def Window_bing():
    import requests

    window_00 = Toplevel()
    window_00.title("Scraper")
    window_00.geometry("660x376")
    main_frame = Frame(window_00)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    window_01 = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=window_01, anchor="nw")

    g_zm_01 = g_entry_root_01.get()
    g_zm_02 = g_entry_root_02.get()

    Label(window_01,
          text='Wyniki wyszukiwania w wyszukiwarce ' +
               g_zm_01 +
               ' dla ' +
               g_zm_02 +
               '.\n').grid(row=0,
                           column=0)

    search_phrase = (g_zm_01 + g_zm_02 + ' kurs' + ' -ceneo')
    params = {"q": search_phrase}
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    }
    r = requests.get("http://www.bing.com/search", params=params, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find("ol", {"id": "b_results"})
    links = results.findAll("li", {"class": "b_algo"})

    for item in links:
        item_text = item.find("a").text
        item_href = item.find("a").attrs["href"]

        if item_text and item_href:
            label_01_link = Label(window_01,
                                  text=item_text).grid(column=0)
            label_01_link_02 = Label(window_01,
                                     text=item_href).grid(column=0)
            my_text = Text(window_01,
                           height=1,
                           selectbackground="lightblue",
                           selectforeground="black",
                           undo=True)
            my_text.insert(END,
                           item_href)
            my_text.grid(column=0)


def Window_trojmiasto():
    window_02 = Toplevel()
    window_02.title("Scraper")
    window_02.geometry("635x376")

    label_01_quote = Label(window_02, text='Wyniki wyszukiwania dla całego województwa: \n').grid(column=0)

    class KitesurfSpider_Pomorskie(scrapy.Spider):
        name = 'kitesurf'
        allowed_domains = ['pomorskie.travel/pl_PL/na_wodzie-windsurfing_i_kitesurfing-szk_ki_i_wypo_yczalnie']
        start_urls = ['http://pomorskie.travel/pl_PL/na_wodzie-windsurfing_i_kitesurfing-szk_ki_i_wypo_yczalnie/']

        def parse(self, response):
            tytuly = response.xpath('//*[@class="title-wrapper"]')
            for tytul in tytuly:
                text = tytul.xpath('.//p/text()').extract()
                label_02_quote = Label(window_02, text=text).grid(column=0)

    window_01 = Toplevel()
    window_01.title("Scraper")
    window_01.geometry("635x376")
    main_frame = Frame(window_01)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    Window_02_scroll = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=Window_02_scroll, anchor="nw")

    class KitesurfSpider_tr_01(scrapy.Spider):
        name = 'sopotsurf'
        allowed_domains = ['http://sopotsurf.com']
        start_urls = ['http://sopotsurf.com/']

        def parse(self, response):
            row = response.xpath('//*[@class="row"]')
            row2 = row.xpath('.//*[@class="row-hover"]')
            tr1 = open("./tr1Sopotsurf.com.json ", "w+")
            js = {}
            js2 = {}
            label_01_quote = Label(Window_02_scroll, text='Oferta szkoły Sopotsurf.com: \n').grid(column=0)
            for it in range(1):
                dane = "dane" + str(it + 1)
                text = row2.xpath('.//*/text()').extract()
                js.update({dane: text})
                label_02_quote = Label(Window_02_scroll, text=text).grid(column=0)
            js2.update({"Oferta strony": "Sopotsurf.com"})
            js2.update({"Miejscowość": "Sopot"})
            js2.update({"Data pobrania": dzisiejsza_data})
            js2.update({"Data": js})
            tr1.write(json.dumps((js2), indent=4, separators=(',', ':')))
            label_02_quote = Label(Window_02_scroll, text='\n\n').grid(column=0)

    class KitesurfSpider_tr_02(scrapy.Spider):
        name = 'onewave'
        allowed_domains = ['https://onewave.pl/tour/szkolenia-kitesurfing']
        start_urls = ['https://onewave.pl/tour/szkolenia-kitesurfing/']

        def parse(self, response):
            row = response.xpath('//*[@class="vc_tta-panel-body"]')
            row2 = row.xpath('.//tr')
            js = {}
            js2 = {}
            tr2 = open("./tr2onewave.pl.json ", "w+")
            label_01_quote = Label(Window_02_scroll, text='Oferta szkoły onewave.pl: \n').grid(column=0)
            for it in range(1):
                text = row2.xpath('.//text()').extract()
                dane = "dane" + str(it + 1)
                js.update({dane: text})
                label_02_quote = Label(Window_02_scroll, text=text).grid(column=0)
            js2.update({"Oferta strony": "onewave.pl"})
            js2.update({"Miejscowość": "Gdańsk"})
            js2.update({"Data pobrania": dzisiejsza_data})
            js2.update({"Data": js})
            tr2.write(json.dumps(js2, indent=4, separators=(',', ':')))
            label_02_quote = Label(Window_02_scroll, text='\n\n').grid(column=0)

    class KitesurfSpider_tr_03(scrapy.Spider):
        name = 'aloha'
        allowed_domains = ['https://aloha.pl/kursy-kite-2']
        start_urls = ['https://aloha.pl/kursy-kite-2/']

        def parse(self, response):
            row = response.xpath('//*[@class="row-hover"]')
            row3 = row.xpath('.//*[@class="column-3"]')
            tr3 = open("./tr3aloha.pl.json ", "w+")
            js = {}
            js2 = {}
            label_01 = Label(Window_02_scroll, text='Oferta szkoły aloha.pl: \n').grid(column=0)
            for it, row3 in enumerate(row):
                dane = "dane" + str(it + 1)
                text2 = row3.xpath('.//text()').extract()
                js.update({dane: text2})
                label_03 = Label(Window_02_scroll, text=text2).grid(column=0)
                label_04 = Label(Window_02_scroll, text='\n').grid(column=0)
            js2.update({"Oferta strony": "aloha.pl"})
            js2.update({"Miejscowość": "Gdynia"})
            js2.update({"Data pobrania": dzisiejsza_data})
            js2.update({"Data": js})
            tr3.write(json.dumps(js2, indent=4, separators=(',', ':')))
            label_02_quote = Label(Window_02_scroll, text='\n\n').grid(column=0)

    class KitesurfSpider_tr_04(scrapy.Spider):
        name = 'onewave'
        allowed_domains = ['http://bssurf.pl/szkolenia']
        start_urls = ['http://bssurf.pl/szkolenia/']

        def parse(self, response):
            row = response.xpath('//*[@itemprop="text"]')
            tr4 = open("./tr4bssurf.pl.json ", "w+")
            js = {}
            js2 = {}
            label_01_quote = Label(Window_02_scroll, text='Oferta szkoły bssurf.pl: \n').grid(column=0)
            for it, row3 in enumerate(row):
                text = row.xpath('.//text()').extract()
                dane = "dane" + str(it + 1)
                js.update({dane: text})
                label_02_quote = Label(Window_02_scroll, text=text).grid(column=0)
            js2.update({"Oferta strony": "bssurf.pl"})
            js2.update({"Miejscowość": "Gdańsk"})
            js2.update({"Data pobrania": dzisiejsza_data})
            js2.update({"Data": js})
            tr4.write(json.dumps(js2, indent=4, separators=(',', ':')))
            label_02_quote = Label(Window_02_scroll, text='\n\n').grid(column=0)

    process = CrawlerProcess()
    process.crawl(KitesurfSpider_Pomorskie)
    process.crawl(KitesurfSpider_tr_01)
    process.crawl(KitesurfSpider_tr_02)
    process.crawl(KitesurfSpider_tr_03)
    process.crawl(KitesurfSpider_tr_04)
    process.start()


def Window_puck():
    import scrapy
    from scrapy.crawler import CrawlerProcess

    window_pom = Toplevel()
    window_pom.title("Scraper")
    window_pom.geometry("635x376")

    label_01_quote = Label(window_pom, text='Wyniki wyszukiwania dla całego województwa: \n').grid(column=0)

    class KitesurfSpider_Pomorskie(scrapy.Spider):
        name = 'kitesurf'
        allowed_domains = ['pomorskie.travel/pl_PL/na_wodzie-windsurfing_i_kitesurfing-szk_ki_i_wypo_yczalnie']
        start_urls = ['http://pomorskie.travel/pl_PL/na_wodzie-windsurfing_i_kitesurfing-szk_ki_i_wypo_yczalnie/']

        def parse(self, response):
            tytuly = response.xpath('//*[@class="title-wrapper"]')
            for tytul in tytuly:
                text = tytul.xpath('.//p/text()').extract()
                label_02_quote = Label(window_pom, text=text).grid(column=0)

    window_01 = Toplevel()
    window_01.title("Scraper")
    window_01.geometry("635x376")
    main_frame = Frame(window_01)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    window_puck_01 = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=window_puck_01, anchor="nw")

    class KitesurfSpider_Puck_01(scrapy.Spider):
        name = 'okonska'
        allowed_domains = ['http://www.okonska.pl/szkola/lekcje-indywidualne']
        start_urls = ['http://www.okonska.pl/szkola/lekcje-indywidualne/']

        def parse(self, response):
            row = response.xpath('//*[@class="shaka-table"]')
            puckjson = open("./puck.json ", "w+")
            js = {}
            js2 = {}
            label_01_quote = Label(window_puck_01, text='Oferta szkoły okonska.pl/: \n').grid(column=0)
            for it, row3 in enumerate(row):
                text = row.xpath('.//text()').extract()
                dane = "dane" + str(it + 1)
                js.update({dane: text})
                label_02_quote = Label(window_puck_01, text=text).grid(column=0)
            js2.update({"Oferta strony": "okonska.pl"})
            js2.update({"Miejscowość": "Puck"})
            js2.update({"Data pobrania": dzisiejsza_data})
            js2.update({"Data": js})
            puckjson.write(json.dumps(js2, indent=4, separators=(',', ':')))
            label_02_quote = Label(window_puck_01, text='\n\n').grid(column=0)

    process = CrawlerProcess()
    process.crawl(KitesurfSpider_Pomorskie)
    process.crawl(KitesurfSpider_Puck_01)
    process.start()


def Window_polwysep_helski():
    import scrapy
    from scrapy.crawler import CrawlerProcess

    window_pom = Toplevel()
    window_pom.title("Scraper")
    window_pom.geometry("635x376")

    label_01_quote = Label(window_pom, text='Wyniki wyszukiwania dla całego województwa: \n').grid(column=0)

    class KitesurfSpider_Pomorskie(scrapy.Spider):
        name = 'kitesurf'
        allowed_domains = ['pomorskie.travel/pl_PL/na_wodzie-windsurfing_i_kitesurfing-szk_ki_i_wypo_yczalnie']
        start_urls = ['http://pomorskie.travel/pl_PL/na_wodzie-windsurfing_i_kitesurfing-szk_ki_i_wypo_yczalnie/']

        def parse(self, response):
            tytuly = response.xpath('//*[@class="title-wrapper"]')
            for tytul in tytuly:
                text = tytul.xpath('.//p/text()').extract()
                label_02_quote = Label(window_pom, text=text).grid(column=0)

    window_01 = Toplevel()
    window_01.title("Scraper")
    window_01.geometry("635x376")
    main_frame = Frame(window_01)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    window_polwysep_01 = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=window_polwysep_01, anchor="nw")

    class KitesurfSpider_Chalupy_01(scrapy.Spider):
        name = 'page'
        allowed_domains = ['https://www.kitecrew.pl/kursy-kitesurfingu']
        start_urls = ['https://www.kitecrew.pl/kursy-kitesurfingu/']

        def parse(self, response):
            row = response.xpath('//*[@class="portfolio-container clickable clearfix"]')
            row2 = row.xpath('.//*[@class="lablel single"]//text()')
            row3 = row.xpath('.//*[@class="element-inner"]//text()')
            ph1 = open("./ph1kitecrew.pl.json ", "w+")
            js = {}
            js3 = {}
            label_01_quote = Label(window_polwysep_01, text='Oferta szkoły kitecrew.pl/: \n').grid(column=0)
            for it, row4 in enumerate(row2):
                text = row2[it].extract()
                text2 = row3[it].extract()
                dane = "dane" + str(it * 2 + 1)
                dane2 = "dane" + str(it * 2 + 2)
                js.update({dane: text2})
                js.update({dane2: text})
                label_02_quote = Label(window_polwysep_01, text=text2).grid(column=0)
                label_04_quote = Label(window_polwysep_01, text=text).grid(column=0)
            js3.update({"Oferta strony": "kitecrew.pl/"})
            js3.update({"Miejscowość": "Chałupy"})
            js3.update({"Data pobrania": dzisiejsza_data})
            js3.update({"Data": js})
            ph1.write(json.dumps(js3, indent=4, separators=(',', ':')))
            label_02_quote = Label(window_polwysep_01, text='\n\n').grid(column=0)

    class KitesurfSpider_Chalupy_02(scrapy.Spider):
        name = 'page'
        allowed_domains = ['http://www.polsporty.pl/oferta,kitesurfing,kursy-kitesurfingowe']
        start_urls = ['http://www.polsporty.pl/oferta,kitesurfing,kursy-kitesurfingowe']

        def parse(self, response):
            row = response.xpath('//*[@class="ceny"]')
            ph2 = open("./ph2polsporty.pl.json ", "w+")
            js = {}
            js2 = {}
            label_01_quote = Label(window_polwysep_01, text='Oferta szkoły polsporty.pl/: \n').grid(column=0)
            for it in range(1):
                text = row.xpath('.//text()').extract()
                dane = "dane" + str(it + 1)
                js.update({dane: text})
                label_04_quote = Label(window_polwysep_01, text=text).grid(column=0)
            js2.update({"Oferta strony": "polsporty.pl/"})
            js2.update({"Miejscowość": "Chałupy"})
            js2.update({"Data pobrania": dzisiejsza_data})
            js2.update({"Data": js})
            ph2.write(json.dumps((js2), indent=4, separators=(',', ':')))
            label_02_quote = Label(window_polwysep_01, text='\n\n').grid(column=0)

    class KitesurfSpider_Chalupy_03(scrapy.Spider):
        name = 'page'
        allowed_domains = ['https://www.easy-surfcenter.pl/kurs-kitesurfingu']
        start_urls = ['https://www.easy-surfcenter.pl/kurs-kitesurfingu']

        def parse(self, response):
            row = response.xpath('//tbody')
            ph3 = open("./ph3easy-surfcenter.pl.json ", "w+")
            js = {}
            js2 = {}
            label_01_quote = Label(window_polwysep_01, text='Oferta szkoły easy-surfcenter.pl/: \n').grid(column=0)
            for it, row3 in enumerate(row):
                text = row.xpath('.//text()').extract()
                dane = "dane" + str(it + 1)
                js.update({dane: text})
                label_04_quote = Label(window_polwysep_01, text=text).grid(column=0)
            js2.update({"Oferta strony": "easy-surfcenter.pl"})
            js2.update({"Miejscowość": "Chałupy"})
            js2.update({"Data pobrania": dzisiejsza_data})
            js2.update({"Data": js})
            ph3.write(json.dumps((js2), indent=4, separators=(',', ':')))
            label_02_quote = Label(window_polwysep_01, text='\n\n').grid(column=0)

    class KitesurfSpider_Hel_01(scrapy.Spider):
        name = 'page'
        allowed_domains = ['http://szkola.abcsurf.pl/lekcje-kite']
        start_urls = ['http://szkola.abcsurf.pl/lekcje-kite/']

        def parse(self, response):
            row = response.xpath('//*[@class="wrapper lekcje-3-col lowercase"]')
            ph5 = open("./ph5szkola.abcsurf.pl.json ", "w+")
            js = {}
            js2 = {}
            label_01_quote = Label(window_polwysep_01, text='Oferta szkoły szkola.abcsurf.pl: \n').grid(column=0)
            for it in range(1):
                text = row.xpath('.//text()').extract()
                dane = "dane" + str(it + 1)
                js.update({dane: text})
                label_04_quote = Label(window_polwysep_01, text=text).grid(column=0)
            js2.update({"Oferta strony": "szkola.abcsurf.pl"})
            js2.update({"Miejscowość": "Hel"})
            js2.update({"Data pobrania": dzisiejsza_data})
            js2.update({"Data": js})
            ph5.write(json.dumps(js2, indent=4, separators=(',', ':')))
            label_02_quote = Label(window_polwysep_01, text='\n\n').grid(column=0)

    process = CrawlerProcess()
    process.crawl(KitesurfSpider_Pomorskie)
    process.crawl(KitesurfSpider_Chalupy_01)
    process.crawl(KitesurfSpider_Chalupy_02)
    process.crawl(KitesurfSpider_Chalupy_03)
    process.crawl(KitesurfSpider_Hel_01)
    process.start()


def Window_Krynica_Morska():
    import scrapy
    from scrapy.crawler import CrawlerProcess

    window_pom = Toplevel()
    window_pom.title("Scraper")
    window_pom.geometry("635x376")

    label_01_quote = Label(window_pom, text='Wyniki wyszukiwania dla całego województwa: \n').grid(column=0)

    class KitesurfSpider_Pomorskie(scrapy.Spider):
        name = 'kitesurf'
        allowed_domains = ['pomorskie.travel/pl_PL/na_wodzie-windsurfing_i_kitesurfing-szk_ki_i_wypo_yczalnie']
        start_urls = ['http://pomorskie.travel/pl_PL/na_wodzie-windsurfing_i_kitesurfing-szk_ki_i_wypo_yczalnie/']

        def parse(self, response):
            tytuly = response.xpath('//*[@class="title-wrapper"]')
            for tytul in tytuly:
                text = tytul.xpath('.//p/text()').extract()
                label_02_quote = Label(window_pom, text=text).grid(column=0)

    window_01 = Toplevel()
    window_01.title("Scraper")
    window_01.geometry("635x376")
    main_frame = Frame(window_01)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    window_Krynica_01 = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=window_Krynica_01, anchor="nw")

    class KitesurfSpider_Krynica_01(scrapy.Spider):
        name = 'page'
        allowed_domains = ['https://e-windsurfing.pl/lekcje-indywidualne']
        start_urls = ['https://e-windsurfing.pl/lekcje-indywidualne/']

        def parse(self, response):
            row = response.xpath('//*[@class="wp-block-table"]')
            row2 = row.xpath('.//td')
            krynicajson = open("./krynica.json ", "w+")
            js = {}
            js2 = {}
            label_01_quote = Label(window_Krynica_01, text='Oferta szkoły e-surfing.pl: \n').grid(column=0)
            for it, row3 in enumerate(row2):
                text = row2[it].xpath('.//text()').extract()
                dane = "dane" + str(it + 1)
                js.update({dane: text})
                label_04_quote = Label(window_Krynica_01, text=text).grid(column=0)
            js2.update({"Oferta strony": "e-surfing.pl"})
            js2.update({"Miejscowość": "Krynica Morska"})
            js2.update({"Data pobrania": dzisiejsza_data})
            js2.update({"Data": js})
            krynicajson.write(json.dumps(js2, indent=4, separators=(',', ':')))
            label_02_quote = Label(window_Krynica_01, text='\n\n').grid(column=0)

    process = CrawlerProcess()
    process.crawl(KitesurfSpider_Pomorskie)
    process.crawl(KitesurfSpider_Krynica_01)
    process.start()


def Window_Wicko():
    import scrapy
    from scrapy.crawler import CrawlerProcess
    import json

    window_pom = Toplevel()
    window_pom.title("Scraper")
    window_pom.geometry("635x376")

    label_01_quote = Label(window_pom, text='Wyniki wyszukiwania dla całego województwa: \n').grid(column=0)

    class KitesurfSpider_Pomorskie(scrapy.Spider):
        name = 'kitesurf'
        allowed_domains = ['pomorskie.travel/pl_PL/na_wodzie-windsurfing_i_kitesurfing-szk_ki_i_wypo_yczalnie']
        start_urls = ['http://pomorskie.travel/pl_PL/na_wodzie-windsurfing_i_kitesurfing-szk_ki_i_wypo_yczalnie/']

        def parse(self, response):
            tytuly = response.xpath('//*[@class="title-wrapper"]')
            for tytul in tytuly:
                text = tytul.xpath('.//p/text()').extract()
                label_02_quote = Label(window_pom, text=text).grid(column=0)

    window_01 = Toplevel()
    window_01.title("Scraper")
    window_01.geometry("635x376")
    main_frame = Frame(window_01)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    window_Wicko_01 = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=window_Wicko_01, anchor="nw")

    class KitesurfSpider_Wicko_01(scrapy.Spider):
        name = 'page'
        allowed_domains = ['https://www.windsurfing-habenda.pl/kurs-windsurfingu']
        start_urls = ['https://www.windsurfing-habenda.pl/kurs-windsurfingu/']

        def parse(self, response):
            row = response.xpath('//*[tbody]')
            label_01_quote = Label(window_Wicko_01, text='Oferta szkoły e-surfing.pl: \n').grid(column=0)
            wickojson = open("./wicko.json ", "w+")
            js = {}
            js2 = {}
            for it in range(1):
                text = row.xpath('.//text()').extract()
                dane = "dane" + str(it + 1)
                js.update({dane: text})
                label_04_quote = Label(window_Wicko_01, text=text).grid(column=0)
            js2.update({"Oferta strony": "e-surfing.pl"})
            js2.update({"Miejscowość": "Wicko"})
            js2.update({"Data pobrania": dzisiejsza_data})
            js2.update({"Data": js})
            wickojson.write(json.dumps(js2, indent=4, separators=(',', ':')))
            label_02_quote = Label(window_Wicko_01, text='\n\n').grid(column=0)

    process = CrawlerProcess()
    process.crawl(KitesurfSpider_Pomorskie)
    process.crawl(KitesurfSpider_Wicko_01)
    process.start()


if __name__ == "__main__":
    import sys

    root_Window()
