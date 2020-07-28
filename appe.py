"""
@auteur : Walid.MENGHOUR
@DATE : 28/07/2020
@Description :  Appe to see everyday Statictic about coivd19 in every Country 
"""



#Import Tkinter Laybriyt
from tkinter import *
import tkinter.ttk as tk 
import tkinter.tix as tix
import datetime
#Import  Covid Laybriry 
from covid import Covid


covid = Covid()
countries_=covid.list_countries()
lcoun = [(countries_[i]['name']) for i in range(len(countries_))]


root  = Tk()
#root.geometry("800x400")
root.title("COVID19Zoom")

n = StringVar()

appetitle = Label(root,text="ZoomCovid19",width=30,height=2).grid(row=1)
# Foor Country 
lbcontry  = Label(root,text="Country :").grid(row=4,column=0,padx=20,pady=20)
countriesch = tk.Combobox(root,values=sorted(lcoun),textvariable=n)

countriesch.current(2)
countriesch.grid(row=4,column=1,padx=20,pady=20)
data = covid.get_status_by_country_name(countriesch.get())



# FOR COnfitrme CAse 
lbnbcasconf  = Label(root,text="Confirmed Case : ").grid(row=5,column=0,padx=20,pady=20)

caseconftext = Text(root,width=20,height=1)

caseconftext.grid(row=5,column=1,padx=20,pady=20)


# For Active Case 
lbactivecase = Label(root,text="Active Cases : ").grid(row=6,column=0,padx=20,pady=20)
ActiveCase = Text(root,width=20,height=1)

ActiveCase.grid(row=6,column=1,padx=20,pady=20)
# For Recoverd CAse 

lbRecoverdCase = Label(root,text="Recovered Cases : ").grid(row=7,column=0,padx=20,pady=20)

RecoverdCase = Text(root,width=20,height=1)
RecoverdCase.grid(row=7,column=1,padx=20,pady=20)

# FOr deaths 
lbdeaths = Label(root,text="Deaths Case :").grid(row=8,column=0,padx=20,pady=20)
deathsCase = Text(root,width=20,height=1)
deathsCase.grid(row=8,column=1,padx=20,pady=20)

Lastupdate = Label(root,text="Last Update at :").grid(row=9,column=0,padx=20,pady=20)

lastupdate = Text(root,width=20,height=1)
lastupdate.grid(row=9,column=1,padx=20,pady=20)



#get_total_active_cases()

lbtotal_active= Label(root,text="Total Active Case :").grid(row=4,column=3,padx=20,pady=20)
total_active = Text(root,width=20,height=1)
total_active.insert(END,covid.get_total_active_cases())
total_active.grid(row=4,column=4,padx=20,pady=20)

#get_total_confirmed_cases()

lbtotal_confirmed_= Label(root,text="Total confirmed Case :").grid(row=5,column=3,padx=20,pady=20)
total_confirmed = Text(root,width=20,height=1)
total_confirmed.insert(END,covid.get_total_confirmed_cases())
total_confirmed.grid(row=5,column=4,padx=20,pady=20)
#get_total_deaths()

lbtotal_deaths = Label(root,text="Total deaths :").grid(row=6,column=3,padx=20,pady=20)
total_deaths = Text(root,width=20,height=1)
total_deaths.insert(END,covid.get_total_deaths())
total_deaths.grid(row=6,column=4,padx=20,pady=20)
#get_total_recovered()
lbtotal_recovered = Label(root,text="Total Recovered:").grid(row=7,column=3,padx=20,pady=20)
total_recovered = Text(root,width=20,height=1)
total_recovered.insert(END,covid.get_total_recovered())
total_recovered.grid(row=7,column=4,padx=20,pady=20)


def setdata(event):
    data = covid.get_status_by_country_name(countriesch.get())
    ActiveCase.insert(END,data['active'])
    caseconftext.insert(END,data['confirmed'])
    RecoverdCase.insert(END,data['recovered'])
    deathsCase.insert(END,data['deaths'])
    lastupdate.insert(END,data['last_update'])


def clearandset(event):
    try:
        ActiveCase.delete('1.0',END)
        caseconftext.delete('1.0',END)
        RecoverdCase.delete('1.0',END)
        deathsCase.delete('1.0',END)
        lastupdate.delete('1.0',END)
        setdata(event)
    except Exception as e:
        print(e)
    
countriesch.bind('<<ComboboxSelected>>', clearandset)



root.mainloop()
