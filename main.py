import os
from web_scrapping import WebScrapper as ws

class Main:
    def __init__(self):
        self.url = 'https://xkcd.com'
        self.scrapper = ws(self.url)

    def run(self, init, end):
        for i in range(init, end):
            self.scrapper.url = self.url + '/' + str(i)
            self.scrapper.get_image()

if __name__ == '__main__':
    main = Main()
    inicio = int(input('Ingrese el numero de inicio: '))
    fin = int(input('Ingrese el numero de fin: '))
    if inicio > fin:
        print('El numero de inicio debe ser menor al numero de fin')
        exit()
    if inicio < 1:
        print('El numero de inicio debe ser mayor a 0')
        exit()
    if os.path.exists('images'):
        os.system('rm -rf images')
        print('Carpeta images eliminada...')
    main.run(inicio, fin)
