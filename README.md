Python апликација со вградено GUI користејќи ја ttkinker библиотеката 
Пристапува до API на Народна Банка на Македонија користејќи ја HTTP GET методата и добива JSON објект со информации за курсната листа.

Преглед на функциите во апликацијата:
* getExchangeRate(date, getBuySellInfo) апликацијата пристапува го прави HTTP повикот кон API-то. 
  При што date e датумот за кој сакаме да ги добиеме информациите за курсната листа а getBuySellInfo е булеан променлива со која означуваме дали дополнително сакаме да добиеме и информации за продажниот и куповниот курс за тој датум
  Во dictionary објектот кој се враќа од функцијата се сместени следните податоци: датум на валута, име на валута и нејзината ознака, држава, среден, (продажен и куповен - опционално) курс на таа валута.

* getFormatedExchangeRate(json): е помошна функција која додава уште еден запис на листата и помага при извршување на логиката понатаму во апликацијата.

* getCompareExchangeRateForTwoDates(firstDate, secondDate, getBuySellInfo = False): функција која ја имплементира getExchangeRate функцијата,
  како резултатат дава листа од речници во кој се сместени информациите за валутите и разликата помегу валутите која е настаната мегу првиот и вториот датум.

* clearAllFrames(): ги брише сите деца прикачени на моменталниот прозорец и го крие истиот од поглед, при што овозможува простор на новиот прозорец да се генерира.

Апликацијата нуди 3 прозорци и истите се генерираат со користење на 3 функции кој се повикуваат при соодветно користење на менито.


Приказ на менито:

* ![image](https://github.com/gkotlar/Python-app-utilizing-the-foreigh-exchange-API-of-NRBM/assets/147694259/ee6b7513-1ed7-47ba-aa63-6f5c109388db)

Соодветните прозори

* showConversionRatesFrame()
  
  Се генерира табела која ја прикажува курсната листа за денес.

* ![image](https://github.com/gkotlar/Python-app-utilizing-the-foreigh-exchange-API-of-NRBM/assets/147694259/dd0fe949-8a45-49c5-856e-ae7363bc5433)
  


* showConversionCalculatorFrame()
  
  Прави конверзија на валутите од една селектирана вредност во друга, Односно од македонски денари до било која од понудените валути, или пак обратно од понудените валути во денари.
  Користејќи ја најновата курсна листа која е понудена од НРБМ.
  
* ![image](https://github.com/gkotlar/Python-app-utilizing-the-foreigh-exchange-API-of-NRBM/assets/147694259/c0cba39b-cedc-40e9-955c-1765e749cf90)
  



* showCurrencyConversionChangeFrame()

 Се генерира табела која ја прикажува настанатата разлика во валутата од почетниот внесен датум до крајниот внесен датум.

* ![image](https://github.com/gkotlar/Python-app-utilizing-the-foreigh-exchange-API-of-NRBM/assets/147694259/9961ba5b-d1a6-4220-8b2d-55682d1ebf09)
  


Дополнително има фукнции за валидација на внесените дати и покажува error покара доколку корисникот внесе невалидна дата.
  

Искористени библиотеки:
>  requests,
>  json,
>  datetime,
>  tkinter.

За искористување на апликацијата е потребно корисникот да има Python интерпретер на својата машина и дополнително да ги има спуштено и искористените библиотеки.
Во инсталациите на Python вообичаено се спуштени сите библиотеки освен requests библиотеката која корисникот би можел сам да ја превземе користејќи pip.

Потребна е постојана интернет конекција за апликацијата да работи.

Искористена литература:
https://www.nbrm.mk/content/Instructions_for_utilization_of_the_web_service_of_the_NB_for_the_exchange_rate_list_and_the_exchange_rates_for_government_bodies.pdf
    * 2. https://www.nbrm.mk/web-servis-novo-en.nspx
    * 3. Prezentacija: "HTTP-HyperText Transfer Protocol, urllib, httplib во Python" - Вон. проф. Д-р Марко Порјазоски
    * 4. https://tkinter.com/using-frames-with-menus-python-tkinter-gui-tutorial-47/
    * 5. https://thepythoncode.com/article/currency-converter-gui-using-tkinter-python
    * 6. https://pythonguides.com/python-tkinter-table-tutorial/
    * 7. https://stackoverflow.com/questions/63200167/problem-with-horizontal-scrollbar-in-treeview-tkinter
    * 8. https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
    * 9. https://www.w3schools.com/python/python_dictionaries.asp
    * 10. https://www.w3schools.com/python/python_try_except.asp
    * 11. https://www.pythontutorial.net/tkinter/tkinter-radio-button/
    * 12. https://docs.python.org/3/library/datetime.html
