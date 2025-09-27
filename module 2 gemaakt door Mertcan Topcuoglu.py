from tkinter import *
import time
import datetime
from tkinter import messagebox
import psycopg2
from TwitterAPI import TwitterAPI


#Twitter API id gegevens
# api = TwitterAPI('ZIHHWZSnmNPDEnAE7MNJl8voC',
#                  'P4CyDKj9yZK21tZPuYh1PKksXsyVeYxtoRunoKHMPrSujQbYWX',
#                  '1303237879863431178-ZZwl5IH64YsScn0AojBSwk17g4qH4w',
#                  'T6VJNY9oiGLFUIRa8JPYj56yC4CifLeGz0BfJmM9TlYiL')
#
#
# #connectie met database
#
# con = psycopg2.connect(
# host='localhost',  # De host waarop je database runt
# database='NT',  # Database naam
# user='postgres',  # Als wat voor gebruiker je connect, standaard postgres als je niets veranderd
# password='Ankarali1',  # Wachtwoord die je opgaf bij installatie
# port=5433) #poort nummer
#
#

#functie om beoordelingstablad te laten verschijnen als de moderator is ingelogd
def beoordeel_scherm():

    global bericht #globaliseer variabel
    global Opmerking_text_reiziger #globaliseer variabel
    global afkeurreden #globaliseer variabel

    beoordeel_scherm = Toplevel(master=root) #beginnen met layout van beoordeelscherm
    beoordeel_scherm.geometry("500x750")  #resolutie
    beoordeel_scherm.configure(bg="#ffcc00") #achtergrond kleur naar geel kleuren


    welkom_beoordelings_label = Label(beoordeel_scherm,
                                      text='Beoordelingsruimte', #beoordelingstablad titel naam
                                      background='#ffcc00', #kleur naar geel
                                      foreground='dark blue', #kleur van letters naar donker blauw
                                      font=('Frutiger', 19, 'bold'), #stijl en lettertype, vetgedrukt
                                      width=33, #breedte van label
                                      height=2 #hoogte van label
                                      )


    welkom_beoordelings_label.pack() #beoordelingstablad is gevormd

    #label met titel naam opmerking van reiziger
    Opmerking_reiziger_label = Label(beoordeel_scherm, #opmerking van reiziger label (titel)
                                     text='Opmerking van reiziger', #tekst in label
                                     background='#ffcc00', #achtergrond naar geel
                                     foreground='dark blue', #kleur letters naar donkerblauw
                                     font=('Frutiger', 14), #lettertype,lettergrootte
                                     width=55, #breedte
                                     height=3) #hoogte

    Opmerking_reiziger_label.pack() #opmerkingslabel van reiziger is gevormd

    Opmerking_text_reiziger = Message(beoordeel_scherm, #berichtvak waar opmerkingen op komen
                                     text='', #tekst wat erop komt
                                     background='#ffcc00', #achtergrond naar geel
                                     foreground='dark blue', #kleur letters naar donkerblauw
                                     font=('Frutiger', 12), #lettertype en grootte
                                     width=1200, #breedte
                                     )

    cur = con.cursor() #connect naar cursor

    Opmerking_text_reiziger.pack(pady = 40) #berichtvak is gevormd en met verticaal gecreeerde afstand

    cur.execute('SELECT id from Tweet where beoordelingsopmerking is NULL') #selecteer tweetid waar beoordelingsopmerking leeg is
    con.commit() #sla wijzigingen op
    id_nummer = cur.fetchone() #haal 1 gegeven op uit uitvoer (cur.execute)

    print(id_nummer) #laat id nummer zien
    cur.execute('SELECT naam,opmerking from Tweet where beoordelingsopmerking is NULL') #selecteer naam en opmerking van tweet waar beoordelingsopmerking leeg is
    con.commit() #sla wijzigingen op
    bericht = cur.fetchone() #haal 1 gegeven op uit uitvoer(cur.execute)
    print(bericht) # print bericht

    goedkeurknop = Button(beoordeel_scherm, text="goedkeuren", command=goedgekeurd, background='#ffcc00', #knop voor goedkeuren
                          foreground='dark blue', width=10)
    goedkeurknop.place(x=670, y=480) #plaats op gegeven locatie

    afkeurknop = Button(beoordeel_scherm, text="afkeuren", command=afgekeurd, background='#ffcc00', #knop voor afkeuren
                        foreground='dark blue', width=10)
    afkeurknop.place(x=770, y=480) #plaats opgegeven locatie

    afkeur_label = Label(beoordeel_scherm, #beoordeel scherm label, titel voor tekst vak die hieronder zit
                         text='Bij afkeuring een reden invoeren!',
                         background='#ffcc00',
                         foreground='dark blue',
                         font=('Frutiger', 11),
                         width=55,
                         height=2)

    afkeur_label.pack() #vorm beoordeelscherm label

    afkeurreden = Text(beoordeel_scherm, #tekstvak waar afkeurreden inkomt
                       font=('Frutiger', 11),
                       background='#ffcc00',
                       foreground='dark blue',
                       width=45,
                       height=5)

    afkeurreden.pack(padx=10, pady=1) #tekstvak is gevormd met verticaal en horizontaal gecreeerde afstand
    bericht_vertoning()  #roep functie aan


#functie om een digitale 'tikkende 'klok te weergeven
def tik():
    time_string = time.strftime("Datum: %D \t Tijd: %H:%M:%S")
    klok.config(text=time_string)
    klok.after(200, tik) #klok "snelheid"

def bericht_vertoning(): #vertoon berichten uit database
    cur = con.cursor()
    cur.execute('SELECT naam,opmerking from Tweet where beoordelingsopmerking is NULL') #selecteer de naam en de opmerking van tabel tweet waar geen beoordelingsopmerking over is
    con.commit()
    bericht = cur.fetchone() # gegevens worden opgehaald

    if bericht != None: #als er berichten zijn geef berichten weer
        naam = bericht[0] #naam van reiziger
        opmerking = bericht[1] #opmerking van reiziger
        Opmerking_text_reiziger['text'] = str("reizigersnaam: " + naam + "        opmerking: " + opmerking) #dit komt in het tekstlabel wat wordt geupdate
    else:
        Opmerking_text_reiziger['text'] = 'Er zijn geen tweets meer om te beoordelen!' #geen berichten? geef melding

#functie als er op goedkeurknop wordt gedrukt
def goedgekeurd(): #functie voor goedkeuring
    bericht_vertoning() #roep functie aan

    cur = con.cursor()
    cur.execute('SELECT id from Tweet where beoordelingsopmerking is NULL') #selecteer tweet id van tabel tweet waar nog geen beoordelingsopmerking over is
    con.commit()
    id_nummer = cur.fetchone() #haal tweetid op
    id = id_nummer_tekstvak.get()  # de ingevoerde id nummer uit inlogscherm wordt opgeroepen
    y = datetime.datetime.now()  # datum en tijd op dit moment
    reden = 'Geen' #geen reden, omdat het is goedgekeurd

    cur.execute("update Tweet SET beoordelingsopmerking = %s, beoordelingsdatum = %s, beoordelingstijd = %s, moderatoridnummer = %s where id = %s",
        (reden, y, y, id,id_nummer)) #update beoordelingsopmerking,beoordelingsdatum,beoordelingstijd,moderatoridnummer waar de cur.fetchone() wordt opgeroepen
    con.commit()
    api.request('statuses/update', {'status': bericht[0] + ' schreef: ' + '  ' + bericht[1]}) #stuur bericht naar twitter [0] = naam van reiziger [1]= opmerking van reiziger
    bericht_vertoning() #roep functie aan

    #het bericht wat goedgekeurd is heb ik nodig


#functie als er op afkeurknop wordt gedrukt
def afgekeurd():
    bericht_vertoning()

    cur = con.cursor()
    cur.execute('SELECT id from Tweet where beoordelingsopmerking is NULL') #selecteer tweetid waar nog geen beoordelingsopmerking over is
    con.commit()
    id_nummer = cur.fetchone()
    id = id_nummer_tekstvak.get()  # de ingevoerde id nummer uit inlogscherm wordt opgeroepen
    y = datetime.datetime.now()  # datum en tijd op dit moment

    reden = afkeurreden.get("1.0", 'end-1c') #de afkeurreden wordt opgeroepen
    afkeurreden.delete("1.0", 'end-1c') #de afkeurreden wordt weer weggehaald
    cur.execute("update Tweet SET beoordelingsopmerking = %s, beoordelingsdatum = %s, beoordelingstijd = %s, moderatoridnummer = %s where id = %s",(reden,y,y,id,id_nummer))
    con.commit()
    bericht_vertoning()



#functie voor inlogscherm
def inloggen():
    global id_nummer_tekstvak #globaliseer variabel

    id_nummer = id_nummer_tekstvak.get() #roep id_nummer van moderator aan

    if len(id_nummer) > 8 or len(id_nummer) < 8: #als id nummer groter dan 8 getallen, en kleiner dan 8 getallen is, geef error melding
        messagebox.showerror(title="Foutmelding"  , message= "Het id nummer bestaat slechts uit 8 cijfers!" )

    naam = naam_tekstvak.get() #haal Moderator naam op
    combo = (int(id_nummer),naam) #deze combineert de naam met idnummer, zo staat het in de database

    if len(naam) <= 1: #als de lengte kleiner is dan 1 bij naamtekstvak, geef error melding
        messagebox.showerror(title="Foutmelding", message="Het is verplicht om u naam in te vullen!")

    cur = con.cursor()
    cur.execute('SELECT id, naam FROM Moderator') #selecteer id en naam van moderator tabel
    rows = cur.fetchall() #haal alle gegevens op
    row = rows[0:] #zet gegevens in rij

    if combo in row: #als id en moderatornaam in rij zit, geef goede melding
        messagebox.showinfo(title="Melding", message="U bent succesvol ingelogd!")
        naam_tekstvak.delete(0,END)
        beoordeel_scherm()

    else: #anders geef foutmelding
        messagebox.showerror(title="Foutmelding", message="De ingevulde gegevens komen niet met elkaar overeen!")


#start met tkinter code
root = Tk()

#resolutei
root.geometry("500x500")
#achtergrond kleur
root.configure(bg = "#ffcc00")

klok = Label(master=root,
                   font=("Frutiger", 17, "bold"),
                   background = '#ffcc00',
                   foreground = 'dark blue',
                   width=33,
                   height=3)

klok.pack()

tik()


#foto van logo in GUI
Nslogo = PhotoImage(file='C:\\Users\\Mertcan\\Pictures\\NS-Twitterzuil\\NS-logo.png')
Nslogolabel = Label(root,borderwidth=0,width = 248, height = 95, # label border width
relief=RIDGE, # label border style
image=Nslogo)
Nslogolabel.pack(padx = 1, pady=1, side = TOP)


#welkom label voor moderator inlogscherm
welkom_label = Label(master=root,
              text='Welkom Moderator van NS!',
              background='#ffcc00',
              foreground='dark blue',
              font=('Frutiger', 17, 'bold'),
              width=34,
              height=5
               )
welkom_label.pack(pady=1)



#label voor id_nummer
id_nummer_label = Label(master=root,
               text='Voer hier u id nummer in! \n (bestaande uit 8 getallen)',
               background='#ffcc00',
               foreground='dark blue',
               font=('Frutiger', 11),
               width=53,
               height=4)

id_nummer_label.pack(pady=1)

#tekstvak voor invoer van id_nummer
id_nummer_tekstvak = Entry(master=root,font=('Frutiger', 11), background='#ffcc00',foreground='dark blue')
id_nummer_tekstvak.pack(padx=10, pady=1)




#een label voor naam van moderator
naam_label = Label(master=root,
               text='Voer hier u naam in!',
               background='#ffcc00',
               foreground='dark blue',
               font=('Frutiger', 11),
               width=55,
               height=4)

naam_label.pack()




#tekstvak voor de naam van de moderator
naam_tekstvak = Entry(master=root,font=('Frutiger', 11), background='#ffcc00',foreground='dark blue')
naam_tekstvak.pack(padx=10, pady=1)




#knop voor inloggen
inlogknop = Button(master = root, text = "inloggen", width = 10, foreground ='dark blue', background ='#ffcc00',command = inloggen,font=('Frutiger', 11))
inlogknop.place(x=717, y =580)



#Ns foto
Nslogo2 = PhotoImage(file='C:\\Users\\Mertcan\\Pictures\\NS-Twitterzuil\\NS-logo.png')
Nslogolabel = Label(root,borderwidth=0,width = 248, height = 95, # label border width
relief=RIDGE, # label border style
image=Nslogo2)
Nslogolabel.pack(padx = 1, pady=1, side = BOTTOM)

root.mainloop()


