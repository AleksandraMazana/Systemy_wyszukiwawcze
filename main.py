import requests
from datetime 
import datetime
import time
import json
import os
import re
import webbrowser
=======

# Zapytanie (GET) do API bip.poznan
r = requests.get('http://bip.poznan.pl/api-json/bip/news/-,c,8380/')
#Przypisanie do zmiennej result otrzymanego tekstu i sformatowanie do JSON
result = r.json()
# Wyciąagnięcie z JSONa listy ogloszen i przypisanie do zmiannej listaOgloszen
listaOgloszen = result.get('bip.poznan.pl').get('data')[0].get('komunikaty_i_ogloszenia').get('items')[0].get('komunikat_ogloszenie') 
# Zainicjalizowanie listy daty 
daty = [' '] * len(listaOgloszen)


#Funkcja sortowania po dacie
def dateSort():
    #Posortowanie listyOgloszen po dacie (lambda)
	sorted_date = sorted(listaOgloszen, key=lambda x: datetime.strptime(x['nw_to_date'], '%Y-%m-%d'))	
	#Pętla po posortowanym JSONie zawierającym ułożone według daty rosnąco wydarzenia
	for i in range(0,len(sorted_date)):
       #Wypisanie zmiennych w konsoli 
	   daty[i] = sorted_date[i].get('nw_to_date')
	   print('===============================================')
	   print(' ')
	   print('DATA: ' + sorted_date[i].get('nw_to_date'))
	   print('TYTUL: '+ sorted_date[i].get('nw_title'))
	   print('_______________________________________________')
	   print(' ')
	   print(cleanhtml(sorted_date[i].get('nw_text')))
	   print(' 			')
	   print(' 			')
	   print('===============================================')
	
	print('Naciśnij dowolny przycisk aby kontynuować')
	x = input()
	#wyczyszczenie konsoli
	clear = lambda: os.system('cls')
	clear()
	#powrót do menu głównego
	mainMenu()
	   
	   
#Funkcja sortowania po miejscu wydarzenia   
def placeSort():
    #Pętla po liście ogłoszeń
	for i in range(0,len(listaOgloszen)):
        #REGEX dla miejsca wydarzenia
		pattern2 =r"na\s[A-Z]\S*\s[A-Z]\S*\s[A-Z]\S*|[przy|ul.]\s[A-Z]\S*\s[A-Z]\S*|na\s[A-Z]\S*\s[A-Z]\S*|na\s[A-Z]\S*\s[A-Z]\S*\s[A-Z]\S*"
		#REGEX dla czasu wydarzenia
		timePattern = r"od\s\d\d[:]\d\d|od\sgodziny\s\d\d[:]\d\d"
		#Przypisanie do zmiennej ogloszenie bieżacego tekstu danego ogłoszenia z listyOgloszen
		ogloszenie = listaOgloszen[i].get('nw_text')
		#Przypisanie do zmiennej dopasowanie wyników dziłania REGEX patern2
		dopasowanie = re.search(pattern2,ogloszenie)
		#Przypisanie do zmiennej time wyników działania REGEX timePattern
		time = re.search(timePattern,ogloszenie)
		#Wypisanie danych w konsoli
		print('===============================================')
		print(' ')
		if dopasowanie:
			print('Lokalizacja: ' + dopasowanie.group())
		else:
			print('Lokalizacja nierozpoznana przez REGEX')
		
		print('Data: ' + listaOgloszen[i].get('nw_to_date'))
		
		if time:
			print('Czas: ' + time.group())
		else:
			print('Czas nierozpoznany przez REGEX' )
		
		print('Tytuł: '+ listaOgloszen[i].get('nw_title'))
		print(' ')
		print('TREŚĆ OGŁOSZENIA')
		print(' ')
		print(cleanhtml(listaOgloszen[i].get('nw_text')))
		print('  ')
		print(' ')
		print('===============================================')
		print('Lokalizacja: ' + dopasowanie.group())
		print('Data: ' + listaOgloszen[i].get('nw_to_date'))
		print('Czas: ' + time.group())
		print('Tytuł: '+ listaOgloszen[i].get('nw_title'))
		print(' ')
		print(listaOgloszen[i].get('nw_text'))
		print('  ')
		print(' ')

	print("Naciśnij dowolny przycisk aby kontynuować")	
	x = input()
	#Czyszenie konsoli
	clear = lambda: os.system('cls')
	clear()
	#Powrót do menu
	mainMenu()
	
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext
	

	

	
def searchByPharse(pharse):



	sorted_date = sorted(listaOgloszen, key=lambda x: datetime.strptime(x['nw_to_date'], '%Y-%m-%d'))	
	#Pętla po posortowanym JSONie zawierającym ułożone według daty rosnąco wydarzenia

	
	for i in range(0,len(sorted_date)):
	
	   clearText = cleanhtml(sorted_date[i].get('nw_text'))
	   
	   if pharse in clearText:
		    print('ZNALEZIONO FRAZE W TEKŚCIE: ')
		    print(' ')
		    daty[i] = sorted_date[i].get('nw_to_date')
		    print('===============================================')
		    print(' ')
		    print('DATA: ' + sorted_date[i].get('nw_to_date'))
		    print('TYTUL: '+ sorted_date[i].get('nw_title'))
		    print('_______________________________________________')
		    print(' ')
		    print(cleanhtml(sorted_date[i].get('nw_text')))
		    print(' 			')
		    print(' 			')
		    print('===============================================')
	   

	print('Naciśnij dowolny przycisk aby kontynuować')
	x = input()
	#wyczyszczenie konsoli
	clear = lambda: os.system('cls')
	clear()
	#powrót do menu głównego
	mainMenu()
	
	
	
def printAsHTML():

	sorted_date = sorted(listaOgloszen, key=lambda x: datetime.strptime(x['nw_to_date'], '%Y-%m-%d'))
	htmlTemp = ' '
	htmlTable = '''<!DOCTYPE html>
<html>
<head>

<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>Tabela Wyszukiwania</h2><table>
  <tr>
    <th>Lokalizacja</th>
    <th>Data</th>
    <th>Godzina rozpoczęcia</th>
	<th>Ogłoszenie</th>
  </tr>'''	

	for i in range(0,len(sorted_date)):
  #REGEX dla miejsca wydarzenia
		pattern2 =r"na\s[A-Z]\S*\s[A-Z]\S*\s[A-Z]\S*|[przy|ul.]\s[A-Z]\S*\s[A-Z]\S*|na\s[A-Z]\S*\s[A-Z]\S*|na\s[A-Z]\S*\s[A-Z]\S*\s[A-Z]\S*"
		#REGEX dla czasu wydarzenia
		timePattern = r"od\s\d\d[:]\d\d|od\sgodziny\s\d\d[:]\d\d"
		#Przypisanie do zmiennej ogloszenie bieżacego tekstu danego ogłoszenia z listyOgloszen
		ogloszenie = listaOgloszen[i].get('nw_text')
		#Przypisanie do zmiennej dopasowanie wyników dziłania REGEX patern2
		dopasowanie = re.search(pattern2,ogloszenie)
		#Przypisanie do zmiennej time wyników działania REGEX timePattern
		time = re.search(timePattern,ogloszenie)
		#Wypisanie danych w konsoli
		if dopasowanie:
			htmlTemp = '<tr><td>'+dopasowanie.group()+'</td>' 
			htmlTable = htmlTable + htmlTemp 
		else:
			htmlTemp = '<td>Lokalizacja nie rozpoznana przez REGEX</td>' 
			htmlTable = htmlTable + htmlTemp 
			
		
		htmlTemp = '<td>'+listaOgloszen[i].get('nw_to_date')+'</td>'
		htmlTable = htmlTable + htmlTemp 
		if time:
			htmlTemp = '<td>'+time.group()+'</td>' 
			htmlTable = htmlTable + htmlTemp 
			
		else:
			htmlTemp = '<td>Czas nie rozpoznany przez REGEX</td>' 
			htmlTable = htmlTable + htmlTemp

		
		htmlTemp = '<td>'+cleanhtml(listaOgloszen[i].get('nw_text'))+'</td>' 
		htmlTable = htmlTable + htmlTemp 
		htmlTemp = '</tr>'
		htmlTable = htmlTable + htmlTemp 
		
	htmlTemp = '</table></body></html>'
	htmlTable = htmlTable + htmlTemp
	
	
	print(htmlTable)
	
	f = open('result.html','w')
	f.write(htmlTable)
	f.close()
 
	webbrowser.open_new_tab('result.html')
	
	print('Naciśnij dowolny przycisk aby kontynuować')
	x = input()
	#wyczyszczenie konsoli
	clear = lambda: os.system('cls')
	clear()
	#powrót do menu głównego
	mainMenu()
	
	
#Funkcja wypisujące menu w konsoli
def mainMenu():
	print('========================MENU========================')
	print('						 	   ')
	print('1.Sortuj po dacie     				   ')
	print('2.Sortuj po miejscu   				   ')
	print('3.Wyszukaj fraze      				   ')
	print('4.Drukuj wyszukiwania w HTML (otwarcie przeglądarki)')
	print('						 	   ')
	print('0.Naciśnij dowolny przycisk aby zakończyć     	   ')
	print('====================================================')
	select = input()
	
	if select == '1':
		clear = lambda: os.system('clear')
		clear()
    #W przypadku wybrania opcji "Sortuj po dacie" wywołanie funkcji dateSort()
		dateSort()
	elif select == '2':
		clear = lambda: os.system('cls')
		clear()
#W przypadku wybrania opcji "Sortuj po miejscu" wywołanie funkcji placeSort()
		placeSort()
	elif select == '3':
		clear = lambda: os.system('cls')
		clear()
		print('Wpisz szukaną frazę:')
		inputPharse = input()
		searchByPharse(inputPharse)
	elif select == '4':
		clear = lambda: os.system('cls')
		clear()
		printAsHTML()
	elif select == '0':
		clear = lambda: os.system('cls')
		clear()
		clear = lambda: os.system('clear')
		clear()
#W przypadku wybrania opcji "Sortuj po miejscu" wywołanie funkcji placeSort()
		placeSort()
	elif select == '0':
		clear = lambda: os.system('clear')
		clear()
		print("Poprawnie zakończono działanie programu")


#Wywołanie menu na początku dzialania programu
mainMenu()


