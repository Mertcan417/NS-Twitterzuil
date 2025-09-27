from tkinter import *
import time
from tweepy import *
import datetime

#twitter gegevens
auth = OAuthHandler('ZIHHWZSnmNPDEnAE7MNJl8voC','P4CyDKj9yZK21tZPuYh1PKksXsyVeYxtoRunoKHMPrSujQbYWX')
auth.set_access_token('1303237879863431178-ZZwl5IH64YsScn0AojBSwk17g4qH4w','T6VJNY9oiGLFUIRa8JPYj56yC4CifLeGz0BfJmM9TlYiL')
api = API(auth)

#start met tkinter code
root = Tk()


#functie om digitale klok te weergeven
def tik():
    time_string = time.strftime("Datum: %D \t Tijd: %H:%M:%S")
    klok.config(text=time_string,foreground='dark blue')
    klok.after(200, tik)


#functie om nieuwe tweets op te halen
def fetchnieuwopmerkingen():
    nu = datetime.datetime.now() #datum/tijdstip op dit moment
    vorige = nu - datetime.timedelta(days=1) #verschil in tijd
    nu = nu.strftime("%Y-%m-%d") #sorteer datum in jaar/minuut/dag
    vorige = vorige.strftime("%Y-%m-%d") #jaar/minuut/dag
    opmerkingen = api.user_timeline(  #tijdlijn van testaccount
        since=vorige, #roep variabele
        id='test142719', #naam van testaccount
        until=nu #roep variabele
    )
    Lijstvannieuweopmerkingen = list() #lijst van de nieuwe tweets
    for opmerking in opmerkingen: #door loop nieuwe tweet van lijst
        Lijstvannieuweopmerkingen.append(opmerking.text) #zet tweet in tekst
    return Lijstvannieuweopmerkingen #geef lijst van nieuwe tweets terug


fetchnieuwopmerkingen()

def wijzigopmerkingen(): #update tweetberichten
    opmerkingen_vertonen = fetchnieuwopmerkingen() #haal de nieuwe tweets op
    try: #pas text vak aan
        opmerking1_label['text'] = opmerkingen_vertonen[0]
    except:
        opmerking1_label['text'] = ""
    try:#pas text vak aan
        opmerking2_label['text'] = opmerkingen_vertonen[1]
    except:
        opmerking2_label['text'] = ""
    try:#pas text vak aan
        opmerking3_label['text'] = opmerkingen_vertonen[2]
    except:
        opmerking3_label['text'] = ""
    root.after(60000, wijzigopmerkingen)


root.after(100, wijzigopmerkingen) #update de tweets en laat verschijnen




root.geometry("500x500")

#foto van trein
background_image=PhotoImage(file='C:\\Users\\Mertcan\\Pictures\\Saved Pictures\\vettens.png')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#klok label
klok = Label(master=root,
                   font=("Frutiger", 17, "bold"),
                   width=140,
                   height=1,
                   background = '#ffcc00')

klok.pack()

tik() #functie voor klok wordt aangeroepen


#foto van trein
Nslogo3 = PhotoImage(file='C:\\Users\\Mertcan\\Pictures\\NS-Twitterzuil\\trein.jpg')
Nslogolabel2 = Label(root,borderwidth=0,width = 248, height = 94, # label border width
relief=RIDGE, # label border style
image=Nslogo3)
Nslogolabel2.pack(padx = 1, pady=1, side = BOTTOM)


#welkom label dus titel van pagina
welkom_label = Label(master=root,
              text='Meest recente Tweets van onze reizigers!',
              background='#0E1C85',
              foreground='white',
              font=('Frutiger', 17, 'bold'),
              width=140,
              height=1
               )
welkom_label.pack(pady=1)


#opmerking label die wordt geupdate
opmerking1_label = Label(master=root,
               text= '',
               background='#0E1C85',
               foreground='white',
               font=('Frutiger', 13),
               width=80,
               height=6)

opmerking1_label.pack(pady=20)

#opmerking label die wordt geupdate
opmerking2_label = Label(master=root,
               text= '',
               background='#0E1C85',
               foreground='white',
               font=('Frutiger', 13),
               width=80,height = 6)

opmerking2_label.pack(pady=20)

#opmerking label die wordt geupdate
opmerking3_label = Label(master=root,
               text= '',
               background='#0E1C85',
               foreground='white',
               font=('Frutiger', 13),
               width=80,
               height=6)

opmerking3_label.pack(pady=20)


root.mainloop()