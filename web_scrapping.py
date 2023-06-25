import requests
from bs4 import BeautifulSoup
import urllib.request
import os


class WebScrapper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def get_soup(self):
        page = requests.get(self.url)
        print('Conectando a la pagina...{}'.format(self.url))
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def get_image(self):
        self.get_soup()
        image_container = self.soup.find(id='comic')
        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print('Descargando imagen...{} ... del enlace ... {}'.format(image_name, image_url))
        # image = self.soup.find('img', class_='wide-image')['src']
        # Verificamos si existe la carpeta images
        if not os.path.exists('images'):
            os.makedirs('images')
        #Recuperamos la imagen y la guardamos en la carpeta images
        urllib.request.urlretrieve('https:{}'.format(image_url), 'images/'+image_name)
        print('Imagen descargada...{}'.format(image_name))

