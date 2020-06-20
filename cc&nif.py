import requests
import time
from bs4 import BeautifulSoup
import webbrowser
import re
import os


url = ('https://cc.marcosantos.me/')
nif1 = ('https://nif.marcosantos.me/?i=1')
nif2 = ('https://nif.marcosantos.me/?i=2')
nif3 = ('https://nif.marcosantos.me/?i=3')
nif5 = ('https://nif.marcosantos.me/?i=5')
nif6 = ('https://nif.marcosantos.me/?i=6')
nif8 = ('https://nif.marcosantos.me/?i=8')
nif9 = ('https://nif.marcosantos.me/?i=9')




menu = 0
while menu != 3:
        print ('')
        menu = int(input(('''[ 1 ] : Nº C.C.
[ 2 ] : NIF
[ 3 ] : Sair
''')))

#numero de cidadao
        if menu == 1:
            os.system('cls')

            soup = BeautifulSoup(requests.get(url).text, 'lxml')

            for cc in soup.select('h2'):

                print('Nº C.C. ',cc.text)

#menu numero contribuinte
        elif menu == 2:
            menu = 0
            while menu != 8:
               print ('')
               
               menu = int(input(('''[ 1 ] : Pessoa singular 1
[ 2 ] : Pessoa singular 2
[ 3 ] : Pessoa singular 3
[ 4 ] : Pessoa colectiva
[ 5 ] : Pessoa colectiva pública
[ 6 ] : Empresário em nome individual
[ 7 ] : Pessoa colectiva irregular ou número provisório
[ 8 ] : Voltar
''')))

               if menu == 1:
                os.system('cls')
                soup = BeautifulSoup(requests.get(nif1).text, 'lxml')

                for ps1 in soup.select('h2#nif'):

                    print('NIF Nº ',ps1.text)

               elif menu == 2:
                os.system('cls')
                soup = BeautifulSoup(requests.get(nif2).text, 'lxml')
                for ps2 in soup.select('h2#nif'):

                    print('NIF Nº ',ps2.text)

               elif menu == 3:
                os.system('cls')
                soup = BeautifulSoup(requests.get(nif3).text, 'lxml')
                for ps3 in soup.select('h2#nif'):

                    print('NIF Nº ',ps3.text)

               elif menu == 4:
                os.system('cls')
                soup = BeautifulSoup(requests.get(nif5).text, 'lxml')
                for pc in soup.select('h2#nif'):

                    print('NIF Nº ',pc.text)

               elif menu == 5:
                os.system('cls')
                soup = BeautifulSoup(requests.get(nif6).text, 'lxml')
                for pcp in soup.select('h2#nif'):

                    print('NIF Nº ',pcp.text)

               elif menu == 6:
                os.system('cls')
                soup = BeautifulSoup(requests.get(nif8).text, 'lxml')
                for ei in soup.select('h2#nif'):

                    print('NIF Nº ',ei.text)

               elif menu == 7:
                os.system('cls')
                soup = BeautifulSoup(requests.get(nif9).text, 'lxml')
                for pci in soup.select('h2#nif'):

                    print('NIF Nº ',pci.text)

               elif menu == 8:
                os.system('cls')
                    
#opçao para sair
        elif menu == 3:
            quit ()
        else:
            print('Opção invalida')
