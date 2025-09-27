from tkinter import *
import psycopg2
import datetime
import time
from tkinter.messagebox import showinfo
from tkinter import messagebox
import sys


con = psycopg2.connect(
host='localhost',  # De host waarop je database runt
database='NT',  # Database naam
user='postgres',  # Als wat voor gebruiker je connect, standaard postgres als je niets veranderd
password='*******************************',  # Wachtwoord die je opgaf bij installatie
port=5433 #poortnummer

)


def verzenden(): #functie om opmerking en naam te verzenden naar database
    cur = con.cursor() #bereid om wijzigingen, toevoegingen in de database aan te brengen
    reizigers_naam = naam_reiziger.get() #de tekstvak waar reiziger zijn naam invult wordt opgepakt

    if len(reizigers_naam) < 1: #als de lengte van de naam kleiner is dan 1 teken, defineer de naam als 'anoniem'
        reizigers_naam = "Anoniem"

    review_reiziger = opmerking_reiziger.get("1.0", 'end-1c') #pak de opmerkingstekst vak van de reiziger op, van begin tot het einde van het tekstvak

    if len(review_reiziger) > 140: #als de lengte groter is dan 140 tekens, geef een error melding dat de reiziger maximaal 140 tekens mag invoeren
        error1 = "U kunt maximaal 140 tekens invoeren!"
        messagebox.showerror(title="Foutmelding!",message=error1)

    elif len(review_reiziger) <= 1: #als de lengte kleiner is dan 1, bij het opmerkingstekstvak, geef foutmelding: voer u opmerking in
        error2 = "Voer u opmerking in!"
        messagebox.showerror(title="Foutmelding!",message=error2)

    else: #als lengte van opmerkingstekstvak 1<140 zit, geef melding dat bericht is verzonden
        messagebox.showinfo(title= "Melding!", message = "Het bericht is verzonden, dank voor u mededeling en nog een fijne reis!")
        opmerking_reiziger.delete("1.0", 'end-1c') #verwijder opmerking van reiziger van begin regel tot eind
        naam_reiziger.delete(0,END) #verwijder naam van reiziger van begin regel tot eind
        x = datetime.datetime.now() #geef datum en tijd op dit moment
        cur.execute("insert into Tweet(naam,opmerking,datum,tijd) values (%s,%s,%s,%s)", #voeg in database de opmerking
                    (reizigers_naam, review_reiziger, x, x))
        con.commit() #sla wijzigingen op in database


def tik(): #functie om digitale tijd te vergeven
    time_string = time.strftime("Datum: %D \t Tijd: %H:%M:%S") #functie geeft datum in maand/dag/jaar en tijd in uur/minuten/seconden
    klok.config(text=time_string) #zet in klok
    klok.after(200, tik) #snelheid van overgang naar ander tijdstip oftwel tik tak tik tak snelheid


root = Tk() #begin met tkinter code

root.geometry("500x550") #resolutie van GUI

root.configure(bg = "#ffcc00") #achtergrond naar geel




klok = Label(master=root, #koppel label in root
                   font=("Frutiger", 18, "bold"), #lettertype,lettergrootte,dikgedrukt
                   background = '#ffcc00', #achtergrond
                   foreground = 'dark blue', #letters kleur donkerblauw
                   width=33, #breedte
                   height=3) #hoogte

klok.pack() #verpak label en zet hem in GUI

tik() #roep klok functie aan
Nslogo = PhotoImage(file='C:\\Users\\Mertcan\\Pictures\\NS-Twitterzuil\\NS-logo.png') #foto van NS logo
Nslogolabel = Label(root,borderwidth=0,width = 245, height = 120, # label rand,breedte en hoogte
relief=RIDGE, # label begrenzingstijl
image=Nslogo) #zet logo erin
Nslogolabel.pack(padx = 10, pady=10, side = BOTTOM) #zet logo onderaan in de GUI

label1 = Label(master=root, #koppel label aan root
               text='Heeft u iets mee te delen?', #tekst in label
               background='#ffcc00', #geel achtergrond
               foreground='dark blue', #donker blauwe tekst
               font=('Frutiger', 18, 'bold'), #stijl,lettergrootte,dikgedrukt
               width=33, #breedte
               height=3 #hoogte
                   )

label1.pack() #verpak label en zet hem in GUI


label2 = Label(master=root, #koppel label aan root
               text='Voer hier u naam in (optioneel)', #tekst in label
               background='#ffcc00', #geel achtergrond
               foreground='dark blue', #tekst kleur
               font=('Frutiger', 11), #stijl,lettergrootte
               width=55, #breedte
               height=3) #hoogte

label2.pack() #verpak label en zet hem in GUI

naam_reiziger = Entry(master=root, #koppel tekstvak aan root
                      font=('Helvetica', 11), #stijl,lettergrootte
                      background='#ffcc00',#achtergrond
                      foreground='dark blue')#kleur van tekst

naam_reiziger.pack(padx=10, pady=1) #verticaal en horizontaal afstand creeeren en zet tekstvak in GUI




opmerking_label = Label(master=root, #koppel label aan root
                        text='Voer hier u opmerking in! \n (maximaal 140 tekens toegestaan)', #tekst
                        background='#ffcc00', #geel achtergrond
                        foreground='dark blue', #donker blauwe letters
                        font=('Frutiger', 11), #stijl,lettergrootte
                        width=55, #breedte
                        height=4) #hoogte

opmerking_label.pack() #verpak label en zet hem in GUI

opmerking_reiziger = Text(master=root, #koppel tekstvak aan root
                          font=('Helvetica', 11), #stijl, grootte letters
                          background='#ffcc00', #gele achtergrond
                          foreground='dark blue', #letterskleur
                          width=45,#breedte
                          height=12) #hoogte


opmerking_reiziger.pack(padx=1, pady=1)
#verticaal en horizontaal afstand creeeren en zet tekstvak in GUI

def update(event): #functie telt aantal worden in tekstvak
    var.set(str(len(opmerking_reiziger.get("1.0", 'end-1c')))) #haal lengte van tekstvak op

var = StringVar()

woordenteller = Label(textvariable=var, background = '#ffcc00',font = ('Frutiger', 11) ,text="Message") #maak een woordentel label

woordenteller.pack(pady=5, padx=5) #verpak label en zet in GUI
opmerking_reiziger.bind("<KeyRelease>", update)

verzenden_knop = Button(master=root, #koppel knop aan root
                        text=" Bericht verzenden", #tekst op de knop
                        command = verzenden, #als er op knop wordt gedrukt doorloop functie verzenden
                        background='#ffcc00', #gele achtergrond
                        foreground='dark blue', #donker blauwe tekst
                        width=15) #breedte
verzenden_knop.pack(pady=20) #zet knop in GUI en creeer verticaal afstand

root.mainloop() #beeindig tkinter code