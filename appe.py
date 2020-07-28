"""
@auteur : Walid.MENGHOUR
@DATE : 28/07/2020
@Description :  Appe to see everyday Statictic about coivd19 in every Country 
"""


# Import Tkinter Laybriyt
from tkinter import *
import tkinter.ttk as tk
import tkinter.tix as tix
import datetime
# Import  Covid Laybriry
from covid import Covid


covid = Covid()
countries_ = covid.list_countries()
lcoun = [(countries_[i]['name']) for i in range(len(countries_))]


root = Tk()
root['bg'] = "#2c2c54"
root.geometry("900x500+200+200")
root.resizable(False, False)
root.title("ZoomCOVID19")
lbfgcolor = "#ff793f"
lbbgcolor = "#2c2c54"
n = StringVar()

f = ("Fira Code", 10, 'bold')
appetitle = Label(root, text="ZoomCovid19", bg="#218c74", font=("Fira Code", 20, 'bold'), fg=lbfgcolor, width=30,
                  height=2).grid(row=1, column=1, columnspan=5, padx=80, pady=5)
# Foor Country
lbcontry = Label(root, text="Country :", bg=lbbgcolor, fg=lbfgcolor, font=f).grid(
    row=4, column=0, padx=20, pady=20)
countriesch = tk.Combobox(root, font=f, values=sorted(
    lcoun), textvariable=n)

countriesch.current(2)
countriesch.grid(row=4, column=1, padx=20, pady=20)
data = covid.get_status_by_country_name(countriesch.get())


# FOR COnfitrme CAse
lbnbcasconf = Label(root, text="Confirmed Case : ", font=f, bg=lbbgcolor, fg=lbfgcolor).grid(
    row=5, column=0)

caseconftext = Text(root, font=f, width=20, height=1,
                    bg=lbbgcolor, fg=lbfgcolor)

caseconftext.grid(row=5, column=1, padx=20, pady=20)


# For Active Case
lbactivecase = Label(root,  font=f, text="Active Cases : ", bg=lbbgcolor, fg=lbfgcolor).grid(
    row=6, column=0, padx=20, pady=20)
ActiveCase = Text(root, font=f, width=20, height=1, bg=lbbgcolor, fg=lbfgcolor)

ActiveCase.grid(row=6, column=1, padx=20, pady=20)
# For Recoverd CAse

lbRecoverdCase = Label(root, font=f, text="Recovered Cases : ", bg=lbbgcolor, fg=lbfgcolor).grid(
    row=7, column=0, padx=20, pady=20)

RecoverdCase = Text(root, font=f, width=20, height=1,
                    bg=lbbgcolor, fg=lbfgcolor)
RecoverdCase.grid(row=7, column=1, padx=20, pady=20)

# FOr deaths
lbdeaths = Label(root, font=f, text="Deaths Case :", bg=lbbgcolor, fg=lbfgcolor).grid(
    row=8, column=0, padx=20, pady=20)
deathsCase = Text(root, font=f, width=20, height=1, bg=lbbgcolor, fg=lbfgcolor)
deathsCase.grid(row=8, column=1, padx=20, pady=20)

Lastupdate = Label(root, font=f, text="Last Update at :", bg=lbbgcolor, fg=lbfgcolor).grid(
    row=9, column=0, padx=20, pady=20)

lastupdate = Text(root, font=f, width=20, height=1, bg=lbbgcolor, fg=lbfgcolor)
lastupdate.grid(row=9, column=1, padx=20, pady=20)


# get_total_active_cases()

lbtotal_active = Label(root, font=f, text="Total Active Case :", bg=lbbgcolor, fg=lbfgcolor).grid(
    row=4, column=3, padx=20, pady=20)
total_active = Text(root, font=f, width=20, height=1,
                    bg=lbbgcolor, fg=lbfgcolor)
total_active.insert(END, covid.get_total_active_cases())
total_active.grid(row=4, column=4, padx=20, pady=20)

# get_total_confirmed_cases()

lbtotal_confirmed_ = Label(root, font=f, text="Total confirmed Case :", bg=lbbgcolor, fg=lbfgcolor).grid(
    row=5, column=3, padx=20, pady=20)
total_confirmed = Text(root, font=f, width=20, height=1,
                       bg=lbbgcolor, fg=lbfgcolor)
total_confirmed.insert(END, covid.get_total_confirmed_cases())
total_confirmed.grid(row=5, column=4, padx=20, pady=20)
# get_total_deaths()

lbtotal_deaths = Label(root, font=f, text="Total deaths :", bg=lbbgcolor, fg=lbfgcolor).grid(
    row=6, column=3, padx=20, pady=20)
total_deaths = Text(root, font=f, width=20, height=1,
                    bg=lbbgcolor, fg=lbfgcolor)
total_deaths.insert(END, covid.get_total_deaths())
total_deaths.grid(row=6, column=4, padx=20, pady=20)
# get_total_recovered()
lbtotal_recovered = Label(root, font=f, text="Total Recovered:", bg=lbbgcolor, fg=lbfgcolor).grid(
    row=7, column=3, padx=20, pady=20)
total_recovered = Text(root, font=f, width=20, height=1,
                       bg=lbbgcolor, fg=lbfgcolor)
total_recovered.insert(END, covid.get_total_recovered())
total_recovered.grid(row=7, column=4, padx=20, pady=20)


def setdata(event):
    data = covid.get_status_by_country_name(countriesch.get())
    ActiveCase.insert(END, data['active'])
    caseconftext.insert(END, data['confirmed'])
    RecoverdCase.insert(END, data['recovered'])
    deathsCase.insert(END, data['deaths'])

    lastupdate.insert(END, data['last_update'])


def clearandset(event):
    try:
        ActiveCase.delete('1.0', END)
        caseconftext.delete('1.0', END)
        RecoverdCase.delete('1.0', END)
        deathsCase.delete('1.0', END)
        lastupdate.delete('1.0', END)
        setdata(event)
    except Exception as e:
        print(e)
        print(e.args)


countriesch.bind('<<ComboboxSelected>>', clearandset)


root.mainloop()
