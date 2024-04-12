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

* showConversionRatesFrame()
* ![image](https://github.com/gkotlar/Python-app-utilizing-the-foreigh-exchange-API-of-NRBM/assets/147694259/dd0fe949-8a45-49c5-856e-ae7363bc5433)
  
  Се генерира табела која ја прикажува курсната листа за денес


* showConversionCalculatorFrame()
* ![image](https://github.com/gkotlar/Python-app-utilizing-the-foreigh-exchange-API-of-NRBM/assets/147694259/c0cba39b-cedc-40e9-955c-1765e749cf90)
  
  Прави конверзија на валутите од една селектирана вредност во друга, Односно од македонски денари до било која од понудените валути, или пак обратно од понудените валути во денари.
  Користејќи ја најновата курсна листа која е понудена од НРБМ.


* showCurrencyConversionChangeFrame()
* ![image](https://github.com/gkotlar/Python-app-utilizing-the-foreigh-exchange-API-of-NRBM/assets/147694259/9961ba5b-d1a6-4220-8b2d-55682d1ebf09)
  
  Се генерира табела која ја прикажува настанатата разлика во валутата од почетниот внесен датум до крајниот внесен датум

Искористени библиотеки:
>  requests,
>  json,
>  datetime,
>  tkinter.
И е потребно нивно симнување со цел проектот да работи.

Потребна е постојана интернет конекција за апликацијата да работи.
