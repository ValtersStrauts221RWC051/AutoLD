# Automātikas Projekts
## Lietotie materiāli
### https://greatist.com/fitness/50-bodyweight-exercises-you-can-do-anywhere#bodyweight-moves-for-beginners
## Projekta uzdevums
### Problēma
Sēžot neskaitāmas stundas pie datora, esu piemirsis sportot.
### Realizēšanas gaita
Protams, ka neesmu gatavs veltīt vairākas minūtes mācīties kā pareizi "sportot". Tādēļ patērēšu vēl dažas stundiņas pie datora lai man vairs nekad nevaidzētu domāt par treniņu.
### Plāns
1. Atrast kādu mājaslapu kur ir sakopoti vairāki vingrojumi
2. Pēc nejaušības principa izvēlēties vienu vingrinājumu\
~~3. Atrast bildi kas parāda kā jāizpilda šis vingrinājums~~ (Bija grūtāk izpauzt nekā domāju)
3. Parādīt nelielu aprakstu kā izpildīt noteikto vingrinājumu
4. Katru dienu izpildīt vizmaz vienu vingrinājumu
5. Kļūt stiprākam un veselākam
## Lietotās bibloteikas
### "requests" 
* Dod iespēju importēt mājaslapas pythonā no to interneta linka
* Pārveido HTML mājaslapas uz formātu ko python var apstrādāt
### "BeautifulSoup"
* Pārveito HTML kodu uz skaidri saprotamu valodu
### "random"
* Palīdzēja izvēlēties nejaušu skaitli
### "Python Standard Library"
* Nav iemesla atspēkot
## Individuālu metožu un īpažibu lietojumu paskaidrojums
### "requests" 
* Metodes
1. requests.get - Importē mājaslapu pythonā
* Īpašības
1. Response.text - Pārveido mājas lapu HTML kodu uz tekstu
### "BeautifulSoup"
* Metodes
1. BeutifulSoup - Izveido bs4.BeautifulSoup objektu, lietojot HTML tekstu kā pamatu
2. bs4.BeautifulSoup.get_text - Pārveido HTML tekstu par sadzīves valodas tekstu
### "random"
* Metodes
1. random.randint - Izveido random skaitli noteiktā klāstā
### "Python Standard Library"
* Metodes
1. String.replace - Izņem vai pārveido noteiktu elementu no String
2. list - pārveido String elementu uz char sarakstu
3. char.isupper - Pārbauda vai char ir lielais rakstītais burts
4. String.join - Savieno char saraksta elementus vienā String
5. char[].clear - Izdzēš visus saraksta elementus 
6. char[].append - Ievieto elementu saraksta galā
7. str - pārveido elementu par String
8. len - pārbauda saraksta garumu