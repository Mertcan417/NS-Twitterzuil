# Schoolopdracht
Dit is een schoolopdracht, wat ik in het eerste jaar heb gerealiseerd. Dit is mijn allereerste project, waar ik kennis heb gemaakt met software ontwikkeling.

# NS-Consumenten zuil
## Aanleiding
De Nederlandse Spoorwegen vinden het erg belangrijk dat zij goed kunnen communiceren met hun klanten én van hun klanten goede of minder goede ervaringen horen. Daarom houden ze van tijd tot tijd een enquête onder de reizigers. Het nadeel van een enquête is dat het lang duurt voordat je de resultaten krijgt. De NS heeft gemerkt dat Twitter veel sneller werkt. Het lijkt de directie daarom een goed plan dat klanten hun opmerkingen/complimenten via een computer, aanwezig op elk het station, kunnen invoeren en dat deze opmerkingen dan zichtbaar worden in die stationshal.

De directie is echter ook wel een beetje bang voor Twitter, want men heeft gemerkt dat het ook gebruikt kan worden als uitlaatklep voor ontevreden reizigers. Daarom is het belangrijk dat de inhoud van de Tweets worden gelezen voordat ze worden gepost op Twitter en zichtbaar worden in de stationshal. Op deze manier kunnen respectloze uitingen en bijvoorbeeld schuttingstaal eruit gefilterd worden.

## Opdracht
De opdracht die jij krijg om dit uit te werken, luidt: ontwerp en bouw een systeem met behulp van Twitter waarbij de mening van klanten zichtbaar wordt voor andere reizigers.

Hiervoor gelden onderstaande eisen:
## Eisen voor het systeem
Om dit idee concreet te maken, denkt men aan de volgende systeemeisen (requirements):

1. Op een computerzuil  (module 1) op een willekeurig NS-station kunnen mensen hun berichtje (hun Tweet) van maximaal 140 karakters invoeren. Dit bericht wordt in een database opgeslagen met de datum en een eventuele naam. Als deze leeg is wordt de naam "anoniem" ingevuld.

2. Daarna krijgt een moderator van de NS het berichtje te zien en diegene kan kiezen voor “accept” of “reject”. Bij “reject” wordt een opmerking samen met datum en tijd aan het bericht in de database toegevoegd. De moderator werkt eerst aan het oudste bericht. Bij de NS zijn verschillende moderators. We willen bij een bericht opslaan welke moderator het bericht heeft beoordeeld.

3. Bij “accept” wordt het berichtje op Twitter geplaatst via een twitteraccount. Het account bevat het woord “test” in de naam, want het gaat nu nog om een Proof-of-Concept (PoC).

4. Op een ander scherm worden een aantal van de meest recente Tweets van het account getoond in de stationshal (module 3). Het is belangrijk dat deze Tweets er goed uitzien.

5. Het kan zijn dat er tijdelijk geen Tweets geplaatst worden, bijvoorbeeld als niemand gedurende een bepaalde tijd een Tweet heeft geplaatst. Zorg ervoor dat je dan het weerbericht laat zien op het scherm in de stationshal (OPTIONEEL)

6. De moderator kan een overzicht kunnen krijgen van de afgekeurde Tweets in module 2 (OPTIONEEL)

Uiteindelijk zal je 3 modules en een database gebouwd hebben.
<img width="457" height="214" alt="architectuur-1" src="https://github.com/user-attachments/assets/54585b43-cf5a-45b4-b18d-27e83d055c17" />

## Eisen aan het ontwerp
Het ontwerp omvat een BPMN-model en Use Case diagram met twee volledig uitgewerkte  Use Cases. Daarnaast is een conceptueel datamodel vereist. Dit model wordt verder uitgewerkt in een logisch en fysiek datamodel.

## Tips voor de realisatie
Maak het bovengenoemde systeem met behulp van Python. Het gebruik van Tkinter kan mooie resultaten opleveren, maar is niet verplicht. Je mag ook gebruik maken van een andere Python GUI library.

Let op: de Twitter-API levert geen XML, maar JSON!

# Resultaten
<img width="350" height="486" alt="afbeelding" src="https://github.com/user-attachments/assets/6ef767d1-c173-4f91-a007-ca27616a16ef" />
<img width="381" height="547" alt="afbeelding" src="https://github.com/user-attachments/assets/47d80562-1741-482e-9649-befbee2e8c96" />
<img width="452" height="520" alt="afbeelding" src="https://github.com/user-attachments/assets/0e9e9f84-902f-4176-b7fd-de2ec92cfa05" />

# Technische modellen (UML, ERD)
<img width="1026" height="625" alt="afbeelding" src="https://github.com/user-attachments/assets/124fefe3-a9d2-4e52-8481-47eaade663a2" />
<img width="865" height="384" alt="afbeelding" src="https://github.com/user-attachments/assets/3ca6c079-834f-426a-b135-7fc79a82fac7" />
<img width="753" height="259" alt="afbeelding" src="https://github.com/user-attachments/assets/eb4f34dd-b2c9-4dc0-8a8d-c020bbf97c47" />
<img width="778" height="283" alt="afbeelding" src="https://github.com/user-attachments/assets/a8f7d3bd-03fc-4935-8ce1-1bd504960341" />
<img width="865" height="259" alt="afbeelding" src="https://github.com/user-attachments/assets/3c4711f9-3378-4053-afa6-852872ce7846" />
