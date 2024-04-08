"""
    references :
    * 1. https://www.nbrm.mk/content/Instructions_for_utilization_of_the_web_service_of_the_NB_for_the_exchange_rate_list_and_the_exchange_rates_for_government_bodies.pdf
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

    python interpreter used: Python 3.12.1 64-bit;

    libliaries needed to be imported to run the program: requests, tkinter

    command that can be used to install them: "pip install requests" + "pip install tkinter"
"""
import requests
import json
from datetime import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

#URI link to access the API ref 1. ref 2.
address1 = 'https://www.nbrm.mk/KLServiceNOV/GetExchangeRate'
address2 = 'https://www.nbrm.mk/KLServiceNOV/GetExchangeRates'

#global variables
global currency_list
global selected_mode 

#color resourses
primary = '#081F4D'
secondary = '#0083FF'
white = '#FFFFFF'

def getExchangeRate(date, getBuySellInfo = False):
    """pass date in a DD.MM.YYYY format or write 'today' to get todays exchange rates

    getBuySellInfo configures weather or not the JSON object will have the selling/buying rates for the currencies

    The function returns a list of exchange rates for the given date as a deserialized Python object (list of dictionaries)"""

    #Reference 12. https://docs.python.org/3/library/datetime.html
    if date == 'today':
        now = datetime.now()
        startDate = now.strftime("%d.%m.%Y")
    else:
        startDate = date
    endDate = startDate
    #Reference 1 nbrm API https://www.nbrm.mk/content/Instructions_for_utilization_of_the_web_service_of_the_NB_for_the_exchange_rate_list_and_the_exchange_rates_for_government_bodies.pdf
    #Reference 2 nbrm API https://www.nbrm.mk/web-servis-novo-en.nspx
    # Reference 3. Requests
    paramethers = {'StartDate': startDate,'EndDate': endDate, 'format': 'json'}

    if getBuySellInfo:
        response = requests.get(address2, params=paramethers)
    else:
        response = requests.get(address1, params=paramethers)

    #print("URL = ",response.url)
    res = json.loads(response.text)
    return res

def getFormatedExchangeRate(json):
    """
    Formats the data in a list of Dictionaries the KEY is the short acronym of the currency, the VALUE is a dictionary object of said currency
     
    A MKD value is hardcoded. 

    it only affects the global variable 'currency_list'
    """
    #Reference 1 nbrm API https://www.nbrm.mk/content/Instructions_for_utilization_of_the_web_service_of_the_NB_for_the_exchange_rate_list_and_the_exchange_rates_for_government_bodies.pdf
    #Reference 2 nbrm API https://www.nbrm.mk/web-servis-novo-en.nspx
    # Reference 9. dictionaries
    currency_list.update({'MKD' : 
    {
        "oznaka": "MKD",
        "drzava": "МАКЕДОНИЈА",
        "nomin": 1,
        "kupoven": 1,
        "sreden": 1,
        "prodazen": 1,
        "drzavaAng": "MKD",
        "nazivMak": "Македонски денар",
        "nazivAng": "Macedonian denar",
    }})

    for item in json:
        currency_list.update( {item['oznaka'] : item} )

def printExchangeRate(response):
    """serializes a obj to a JSON formated string and prints with with an indentaion"""    
    text=json.dumps(response, indent=4 )
    print(text)

def getCompareExchangeRateForTwoDates(firstDate, secondDate, getBuySellInfo = False):
    """pass date in a DD.MM.YYYY format or write 'today' to get todays exchange rates

    getBuySellInfo configures weather or not the JSON object will have the selling/buying rates for the currencies

    The function returns the diference of the exchange rates between the first date and the second date as formated as a float (list of dictionaries KEY='oznaka' Value=currency data)"""
    #Reference 1 nbrm API https://www.nbrm.mk/content/Instructions_for_utilization_of_the_web_service_of_the_NB_for_the_exchange_rate_list_and_the_exchange_rates_for_government_bodies.pdf
    #Reference 2 nbrm API https://www.nbrm.mk/web-servis-novo-en.nspx

    print("called getCompareExchangeRatefor2 dates with the following arguments", firstDate, secondDate, getBuySellInfo)

    json1 = getExchangeRate(firstDate, getBuySellInfo)
    json2 = getExchangeRate(secondDate, getBuySellInfo)


    result = {}

    res1 = []

    for item in json1:
        result.update({item['oznaka'] : item})

    for item in json2:
        #Reference 10. try/exept
        try:
            temp1 = result[item['oznaka']]
            #Reference 9. how to update values in dict
            result.update({item['oznaka'] : {"rBr" : temp1['rBr'], "datum": temp1['datum'],"valuta": temp1['valuta'],"oznaka": temp1['oznaka'],"drzava": temp1['drzava'],"nomin" : temp1['nomin'],"kupoven" : temp1['kupoven'] - item['kupoven'],"sreden" : temp1['sreden'] - item['sreden'],"prodazen" : temp1['prodazen'] - item['prodazen'],"drzavaAng" : temp1['drzavaAng'],"drzavaAl": temp1['drzavaAl'],"nazivMak": temp1['nazivMak'],"nazivAng": temp1['nazivAng'],"nazivAl" : temp1['nazivAl'],"datum_f" :temp1['datum_f']}})
            res1.append({"rBr" : temp1['rBr'], "datum": temp1['datum'],"valuta": temp1['valuta'],"oznaka": temp1['oznaka'],"drzava": temp1['drzava'],"nomin" : temp1['nomin'],"kupoven" : temp1['kupoven'] - item['kupoven'],"sreden" : temp1['sreden'] - item['sreden'],"prodazen" : temp1['prodazen'] - item['prodazen'],"drzavaAng" : temp1['drzavaAng'],"drzavaAl": temp1['drzavaAl'],"nazivMak": temp1['nazivMak'],"nazivAng": temp1['nazivAng'],"nazivAl" : temp1['nazivAl'],"datum_f" :temp1['datum_f']})
        except:
            result.update({item['oznaka'] : 'ERROR NO INFORMATION ON THIS CURRENCY'})

    return res1

def showConversionRatesFrame():
    """Funtion that is called to generate the Todays Conversion Rate Table frame

    utilizes ttk.Treeview, ScrollBar, dictionaries..."""
    clearAllFrames()

    columns_dic = [{"ime" : "curr_datum", "vred": "Date"}, {"ime" : "curr_valuta", "vred" : 'Valuta'}, {"ime":"curr_drzava", "vred" : "Country"}, {"ime" : "curr_oznaka", "vred" : "Currency Code"}, {"ime" : "curr_kupoven", "vred": "Buying Rate"},{"ime" : "curr_sreden", "vred": "Middle Rate"}, {"ime": "curr_prodazen", "vred" : "Selling Rate"},{"ime" : "curr_drzavaAng", "vred" : "Country Name ENG"}, {"ime" : "curr_nazivMak", "vred" : "Money Name MKD"}, {"ime":  "curr_nazivAng", "vred" : 'MoneyName ENG'}] 

    columns_dic_names = []
    for item in columns_dic:
        columns_dic_names.append(item['ime'])

    #Reference 6. table tutorial ####################################### https://pythonguides.com/python-tkinter-table-tutorial/#Python_Tkinter_Table_Input
    top_frame.grid(row=0, column=0)
    bottom_frame.grid(row=1, column=0)

    # label for the Conversion Rate List
    name_label = Label(top_frame, text='Conversion Rate List', bg=primary, fg=white, pady=30, padx=15, justify=CENTER, font=('Poppins 20 bold'))
    name_label.grid(row=0, column=0)

    my_curr = ttk.Treeview(bottom_frame, height=12, show='headings')

    my_curr.grid(row=1, column=0, padx=5, pady=5, sticky='NSEW')

    my_curr['columns'] = (columns_dic_names)

    my_curr.column("#0", width=125, stretch=FALSE)
    my_curr.heading("#0",text="",anchor=W)

    for items in columns_dic:
        my_curr.column(items["ime"],anchor=CENTER, width=28, minwidth=125)
        my_curr.heading(items["ime"],text=items["vred"],anchor=CENTER)

    my_curr.update()

    #Reference 7. scroll bar ########################################## https://stackoverflow.com/questions/63200167/problem-with-horizontal-scrollbar-in-treeview-tkinter
    #scrollbar
    curr_scroll_y = Scrollbar(bottom_frame, orient='vertical', command=my_curr.yview)
    curr_scroll_x = Scrollbar(bottom_frame, orient='horizontal', command=my_curr.xview)

    curr_scroll_y.grid(row=1, column=1, sticky="NS", pady=5)
    curr_scroll_x.grid(row=2, column=0, sticky="EW", padx=5)

    my_curr.configure(yscrollcommand=curr_scroll_y.set, xscrollcommand=curr_scroll_x.set)

    #Reference 7. end scroll bar  ##################################### 
    
    ## populate table with data
    global count
    count = 0
    data = getExchangeRate('today', TRUE)

    for record in data:
        my_curr.insert(parent='',index='end',iid=count, text='', values=(
            record["datum"], 
            record["valuta"], 
            record["drzava"], 
            record["oznaka"], 
            record["kupoven"], 
            record["sreden"], 
            record["prodazen"], 
            record["drzavaAng"], 
            record["nazivMak"], 
            record["nazivAng"]
        ))
        count+=1

    #Reference 6. table tutorial end ##################################

def showConversionCalculatorFrame():
    """Funtion that is called to generate the Conversion Rate Calculator frame.

    It uses the exhange rates for the current day, using NBRSM API
    """
    def convertCurrencies():
        #Reference 5. https://thepythoncode.com/article/currency-converter-gui-using-tkinter-python#implementing-currency-conversion 
        #implementing functionality
        """Main function to do the conversion form one value to another, is called with every button press"""

        #Reference 10. try/exept https://www.w3schools.com/python/python_try_except.asp
        try:
            # getting currency from first combobox
            source = from_currency_combo.get()
            # getting currency from second combobox
            destination = to_currency_combo.get()
            # getting amound from amount_entry
            amount = amount_entry.get()

            #checking wheather the source or destionation is MKD
            if source == 'MKD':
                #calculates the needed result and rounds it up to 2 decimal points, the selected more is used to select the exchange rate
                rate = float(currency_list[destination][selected_mode.get()])
                if rate == 0:
                    converted_result = 0
                else:
                    converted_result = float(amount) / rate
                converted_result = round(converted_result,2)

            elif destination == 'MKD':
                rate = float(currency_list[source][selected_mode.get()])
                converted_result = float(amount) * rate
                converted_result = round(converted_result,2)

            else:
                converted_result = 'NULL'

            # formatting the results
            if converted_result == 'NULL':
                formatted_result = 'FROM or TO must be selected as MKD'
            else: 
                #formats the result to a string that can be shown in the result label
                # formatted_result = amount + " " + str.format(source, ",") + " = " + str(converted_result) + " " + destination
                formatted_result = f'{float(amount) : ,} {source} = {converted_result : ,} {destination} | {"Middle" if selected_mode.get() == 'sreden' else "Buying" if selected_mode.get() == 'kupoven' else "Selling"} Rate'


            # adding text to the empty result label
            result_label.config(text=formatted_result)
            
            if converted_result != 'NULL':
                # adding text to the empty time label
                time_label.config(text='Conversion made on : ' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        except:
            showerror(title='Error', message='An error occurred!!')
    
    def switchCurrencyValues():
        # getting currency from first combobox
        source = from_currency_combo.get()
        # getting currency from second combobox
        destination = to_currency_combo.get()

        to_currency_combo.set(source)
        from_currency_combo.set(destination)

        convertCurrencies()

    clearAllFrames()
    
    # Reference 5. https://thepythoncode.com/article/currency-converter-gui-using-tkinter-python#designing-the-gui setting up the project

    top_frame.grid(row=0, column=0)
    bottom_frame.grid(row=1, column=0)

    # label for the text Currency Converter
    name_label = Label(top_frame, text='Currency Converter', bg=primary, fg=white, pady=30, padx=24, justify=CENTER, font=('Poppins 20 bold'))
    name_label.grid(row=0, column=0)

    from_currency_label = Label(bottom_frame, text='FROM:', font=('Poppins 10 bold'), justify=LEFT)
    from_currency_label.place(x=5, y=90)

    to_currency_label = Label(bottom_frame, text='TO:', font=('Poppins 10 bold'), justify=RIGHT)
    to_currency_label.place(x=160, y=90)

    # widgets inside the bottom frame

    selected_mode = StringVar()
    modes = (('Middle Rate', 'sreden'), ('Buying Rate', 'kupoven'), ('Selling Rate', 'prodazen'))

    # label
    label = ttk.Label(bottom_frame, text="Select exchange rate mode", font=('Poppins 10 bold'), justify=LEFT)
    label.place(x=5, y=5)

    iter = 25

    flag = True
    # Reference 11. https://www.pythontutorial.net/tkinter/tkinter-radio-button/
    # radio buttons 
    for mode in modes:
        r = ttk.Radiobutton(bottom_frame, text=mode[0], value=mode[1], variable=selected_mode)
        r.place(x=5, y=iter)
        if flag:
            r.invoke()
            flag = False
        iter +=20
    # end of reference 11

    # Reference 5 https://thepythoncode.com/article/currency-converter-gui-using-tkinter-python#populating-combo-boxes-with-currencies populating with value keys
    # this is the combobox for holding from_currencies
    from_currency_combo = ttk.Combobox(bottom_frame, values=[*currency_list], width=14, font=('Poppins 10 bold'))
    from_currency_combo.place(x=5, y=110)
    # this is the combobox for holding to_currencies
    to_currency_combo = ttk.Combobox(bottom_frame, values=[*currency_list], width=14, font=('Poppins 10 bold'))
    to_currency_combo.place(x=160, y=110)

    # the label for AMOUNT
    amount_label = Label(bottom_frame, text='AMOUNT:', font=('Poppins 10 bold'))
    amount_label.place(x=5, y=135)
    # entry for amount
    amount_entry = Entry(bottom_frame, width=25, font=('Poppins 15 bold'))
    amount_entry.place(x=5, y=160)
    # an empty label for displaying the result
    result_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
    result_label.place(x=5, y=195)

    # an empty label for displaying the time
    time_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
    time_label.place(x=5, y=215)

    # the clickable button for converting the currency
    convert_button = Button(bottom_frame, text="CONVERT", bg=secondary, fg=white, font=('Poppins 10 bold'), command=convertCurrencies)
    convert_button.place(x=5, y=245)

    #Clickable button for switching the currency
    switch_button = Button(bottom_frame, text="Switch", bg=secondary, fg=white, font=('Poppins 10 bold'), command=switchCurrencyValues)
    switch_button.place(x=230, y=245)

    #setting up the values to start with MKD and EUR
    from_currency_combo.current(0)
    to_currency_combo.current(1)

def showCurrencyConversionChangeFrame():
    """Funtion that is called to generate the Todays Conversion Rate Table frame

    utilizes ttk.Treeview, ScrollBar, dictionaries..."""

    global my_curr
    global count
    count = 0
    def valdiateDates(start, end):
        #convert dates to datetime objects
        try:
            if start != 'today':
                date1 = datetime.strptime(start, "%d.%m.%Y").date()
            else:
                date1 = date.today()
            if end != 'today':
                date2 = datetime.strptime(end, "%d.%m.%Y").date()
            else:
                date2 = date.today()
        except:
            #if there's a problem return false
            return False
        
        today = date.today()

        #compare if the date1 is after date2 or if bout of them are after today's date
        if date1 > date2 or date1 > today or date2 > today:
            return False

        return True
    def updateTable():
        try:
            # getting currency from first combobox
            source = date_start_entry.get()
            # getting currency from second combobox
            destination = date_till_entry.get()

            warining_label.config(text='')
            
            #checking wheather the source or destionation is MKD
            if valdiateDates(source, destination):
                
                ## populate table with data
                
                data = getCompareExchangeRateForTwoDates(source, destination, TRUE)

                my_curr.delete(*my_curr.get_children())

                count = 0

                for record in data:
                    my_curr.insert(parent='',index='end',iid=count, text='', values=(
                        record["datum"], 
                        record["valuta"], 
                        record["drzava"], 
                        record["oznaka"], 
                        record["kupoven"], 
                        record["sreden"], 
                        record["prodazen"], 
                        record["drzavaAng"], 
                        record["nazivMak"], 
                        record["nazivAng"]
                    ))
                    count+=1
                converted_result = TRUE
            else:
                converted_result = 'NULL'

            if converted_result == 'NULL':
                # adding text to the empty time label
                warining_label.config(text='Insert dates in dd.MM.yyyy format\n write today for todays date \n from needs to be before till, and both need to be before todays date')

        except:
            showerror(title='Error', message='An error occurred!!')
    
    #clearing the previous frames
    clearAllFrames()

    #defining a dict for use in the table header
    columns_dic = [{"ime" : "curr_datum", "vred": "Date"}, {"ime" : "curr_valuta", "vred" : 'Valuta'}, {"ime":"curr_drzava", "vred" : "Country"}, {"ime" : "curr_oznaka", "vred" : "Currency Code"}, {"ime" : "curr_kupoven", "vred": "Buying Rate"},{"ime" : "curr_sreden", "vred": "Middle Rate"}, {"ime": "curr_prodazen", "vred" : "Selling Rate"},{"ime" : "curr_drzavaAng", "vred" : "Country Name ENG"}, {"ime" : "curr_nazivMak", "vred" : "Money Name MKD"}, {"ime":  "curr_nazivAng", "vred" : 'MoneyName ENG'}] 

    columns_dic_names = []
    for item in columns_dic:
        columns_dic_names.append(item['ime'])

    #Reference 6. table tutorial ####################################### https://pythonguides.com/python-tkinter-table-tutorial/#Python_Tkinter_Table_Input
    top_frame.grid(row=0, column=0)
    bottom_frame.grid(row=1, column=0)

    # label for the Conversion Rate List
    name_label = Label(top_frame, text='Value changes', bg=primary, fg=white, pady=70, padx=100, justify=CENTER, font=('Poppins 12 bold'))
    name_label.grid(row=0, column=0)

    #creating the from and to labels
    from_date_label = Label(top_frame, text='FROM:', font=('Poppins 10 bold'), justify=LEFT)
    from_date_label.place(x=5, y=5)

    till_date_label = Label(top_frame, text='TILL:', font=('Poppins 10 bold'), justify=RIGHT)
    till_date_label.place(x=120, y=5)

    #creating the from and to imput data entries
    date_start_entry = Entry(top_frame, width=10, font=('Poppins 8 bold'))
    date_start_entry.place(x=5, y=25)

    date_till_entry = Entry(top_frame, width=10, font=('Poppins 8 bold'))
    date_till_entry.place(x=120, y=25)

     # the clickable button for converting the currency
    convert_button = Button(top_frame, text="Get Data", bg=secondary, fg=white, font=('Poppins 10 bold'), command=updateTable)
    convert_button.place(x=220, y=25)

    # label for the warning
    warining_label = Label(top_frame, text='', font=('Poppins 5 bold'), justify=CENTER)
    warining_label.place(x=5, y=45)

    #creating and defining the table
    

    my_curr = ttk.Treeview(bottom_frame, height=12, show='headings')

    my_curr.grid(row=1, column=0, padx=5, pady=5, sticky='NSEW')

    my_curr['columns'] = (columns_dic_names)

    #populating the headers
    my_curr.column("#0", width=125, stretch=FALSE)
    my_curr.heading("#0",text="",anchor=W)

    for items in columns_dic:
        my_curr.column(items["ime"],anchor=CENTER, width=28, minwidth=125)
        my_curr.heading(items["ime"],text=items["vred"],anchor=CENTER)

    my_curr.update()

    #Reference 7. scroll bar ########################################## https://stackoverflow.com/questions/63200167/problem-with-horizontal-scrollbar-in-treeview-tkinter
    #scrollbar
    curr_scroll_y = Scrollbar(bottom_frame, orient='vertical', command=my_curr.yview)
    curr_scroll_x = Scrollbar(bottom_frame, orient='horizontal', command=my_curr.xview)

    curr_scroll_y.grid(row=1, column=1, sticky="NS", pady=5)
    curr_scroll_x.grid(row=2, column=0, sticky="EW", padx=5)

    my_curr.configure(yscrollcommand=curr_scroll_y.set, xscrollcommand=curr_scroll_x.set)

    #Reference 7. end scroll bar  ##################################### 
       
def clearAllFrames():
    """function to forget all of the frames, is called for every frame change"""

    #Reference 8. Clearing the frame https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
    
    for widget in top_frame.winfo_children():
       widget.destroy()
    for widget in bottom_frame.winfo_children():
       widget.destroy()
    
    top_frame.grid_forget()
    bottom_frame.grid_forget()
   
if __name__ == '__main__': 
    #importing the data
    list = getExchangeRate('today', TRUE)
    currency_list = {}
    getFormatedExchangeRate(list)

    # Reference 5. https://thepythoncode.com/article/currency-converter-gui-using-tkinter-python
    #creating the main window
    root = Tk()

    #defining the window
    root.geometry('310x390')
    root.title('Currency Converter')
    root.resizable(height=FALSE, width=FALSE)

    #setting up the gridView
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    #Reference 4. ####################################### https://tkinter.com/using-frames-with-menus-python-tkinter-gui-tutorial-47/
    #defining the menu
    my_menu = Menu(root)
    root.config(menu=my_menu)
    modes_menu = Menu(my_menu)
    my_menu.add_cascade(label='Menu', menu=modes_menu)
    modes_menu.add_command(label='Show conversion Rates', command=showConversionRatesFrame)
    modes_menu.add_command(label='MKD 2 Foreign/Foreign 2 MKD Conversion', command=showConversionCalculatorFrame)
    modes_menu.add_command(label='Value changes', command=showCurrencyConversionChangeFrame)

    modes_menu.add_separator()
    modes_menu.add_command(label='Quit', command=root.quit)
    #end of reference 4 ################################

    #Top and bottom frame of the calculatorframe
    top_frame = Frame(root, bg=primary, width=300, height=80)
    bottom_frame = Frame(root, width=300, height=300)

    # r = compareExchangeRateForTwoDates('12.03.2024', '18.03.2024', TRUE)
    # printExchangeRate(r)
    
    #function to initialize the landing page
    showConversionCalculatorFrame()

    #calling the main loop of the GUI
    root.mainloop()
    ###### End of reference 5