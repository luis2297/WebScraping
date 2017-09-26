# pip install bs4
from bs4 import BeautifulSoup

# Este no recuerdo si lo bajé con pip, si da error debe ser eso.
import requests

# pip install urlextract
from urlextract import URLExtract

def soup_it_up():
    # El URL puede ser cualquier perfil de banda en MA, -debería- funcionar. :D
    url = 'https://www.metal-archives.com/bands/At_the_Gates/43'

    # Va por el response usando el URL anterior.
    r = requests.get(url)

    # Convierte el response en un objeto BeautifulSoup para su uso.
    soup = BeautifulSoup(r.text, 'html.parser')

    # Un pequeño menú para facilitar el uso.
    while True:
        input_string = "¿Qué desea hacer?\n\t1. Obtener atributos generales."
        input_string += "\n\t2. Obtener discografía."
        input_string += "\n\t3. Obtener miembros."
        input_string += "\n\t4. Salir.\n"
        opt = input(input_string)
        if opt != '1' and opt != '2' and opt != '3':
            break
        elif opt == '1':
            get_band_attributes(soup)
            print(">>El contenido generado se encuentra en: band_info.txt")
        elif opt == '2':
            get_band_disco(soup)
            print(">>El contenido generado se encuentra en: disco_info.txt")
        elif opt == '3':
            get_band_members(soup)
            print(">>El contenido generado se encuentra en: member_info.txt")


def get_band_attributes(soup):
    # Del objeto "soup" (el contenido será parecido a band_page.html) que viene como parámetro:
    # -> Busca <h1 class="band_name">, que es el tag donde se encuentra el nombre de la banda.
    band_name = soup.find("h1", {"class": "band_name"})

    # Con un archivo de texto abierto para escritura:
    with open('band_info.txt', 'w') as bp:
        # -> Del tag resultante regresa sólo el texto (el nombre de la banda).
        bp.write(band_name.getText() + '\n')

        # -> Buscamos en <dd> que es donde se encuentran los atributos generales.
        # -> Regresa una lista de tags y su contenido.
        attributes = soup.find_all("dd")

        # -> Por cada elemento de la lista.
        for atr in attributes:
            # -> Separa los strings en listas.
            s_list = atr.getText().split()
            # -> Juntalos de nuevo como string pero con whitespaces normales.
            s = " ".join(map(str, s_list))
            # -> Escribe a archivo.
            bp.write(s + '\n')


def get_band_disco(soup):
    # Instancia de URLExtract.
    extractor = URLExtract()

    # Del objeto "soup" (el contenido será parecido a band_page.html) encuentra <div id="band_disco">.
    disco_finder = soup.find("div", {"id": "band_disco"})
    # Los tags resultantes pasan a string.
    s_disco_finder = str(disco_finder)
    # Extrae todos los URLs presentes.
    disco_url = extractor.find_urls(s_disco_finder)

    # Toma el primer URL y asignalo a una variable.
    url = disco_url[0]
    # Hace un request con dicho URL.
    r = requests.get(url)

    # Convierte el response en un objeto BeautifulSoup para su uso.
    disco_soup = BeautifulSoup(r.text, 'html.parser')

    # Del objeto "disco_soup" (el contenido será parecido a disco.html) obtiene todos los tags <tr>.
    disco_entries = disco_soup.find_all("tr")

    # Elimina el primero porque no se necesita.
    disco_entries.pop(0)

    # Con un archivo de texto abierto para escritura:
    with open('disco_info.txt', 'w') as di:
        # -> Por cada elemento en disco_entries:
        for item in disco_entries:
            # -> Con un ciclo de 0 a 3:
            for x in range(3):
                # -> Busca todos los tags <td> usando el índice 'x'.
                s = item.find_all("td")[x]
                # -> Toma el texto de cada uno de estos y escribe a archivo.
                di.write(str(s.getText()) + '\n')
            di.write('\n')


def get_band_members(soup):
    # Del objeto "soup" (el contenido será parecido a band_page.html) encuentra <div id="band_tab_members_current">.
    current_members = soup.find("div", {"id": "band_tab_members_current"})

    # De la búsqueda anterior encuentra todos los <a class="bold">.
    member_finder = current_members.find_all("a", {"class": "bold"})

    # Con un archivo de texto abierto para escritura:
    with open('member_info.txt', 'w') as mi:
        # -> Con un ciclo de 0 al tamaño de member_finder.
        for x in range(len(member_finder)):
            # -> Escribe a archivo el nombre de cada miembro de la banda.
            mi.write(str(member_finder[x].getText()) + '\n')



if __name__ == '__main__':
    soup_it_up()
