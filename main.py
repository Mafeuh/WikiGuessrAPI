import requests
from bs4 import BeautifulSoup


THEMES = [
    'science',
    'technologies',
    'medecine',
    'arts',
    'sport',
    'politique',
    'societe',
    'histoire',
    'geographie'
]

UNWANTED_CLASSES = [
    'bandeau-niveau-ebauche',
    'bandeau-niveau-modere'
]


def get_random_page_html():
    url = "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text

        while not check_is_page_valid(html):
            print("Ebauche détectée")
            print(response.url)
            url = "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"
            response = requests.get(url)
            html = response.text
        print(response.url)
        return html
    else:
        return False


def process_html(raw_html: str):
    soup = BeautifulSoup(raw_html, "html.parser")

    remove_all_href(soup)
    remove_all_img(soup)
    remove_all_table(soup)
    remove_all_style(soup)

    title = soup.title.text
    title = title[0:(title.rfind('—'))-1]

    tag_names = ['h3', 'p']
    tags = soup.find_all(tag_names)

    text = f'<h1>{title}</h1>'

    for tag in tags:
        tag_string = str(tag)
        print (tag_string)
        text += tag_string

    with open('C:\\Users\\mafma\\Downloads\\test.html', 'w', encoding="utf-8") as file:
        file.write(text)

    result = {
        'title': title
    }
    return result


def remove_all_img(soup: BeautifulSoup):
    for img in soup.find_all('img'):
        img.decompose()


def remove_all_href(soup: BeautifulSoup):
    for a in soup.find_all('a'):
        del a['href']


def remove_all_table(soup: BeautifulSoup):
    for table in soup.find_all('table'):
        table.decompose()


def remove_all_style(soup: BeautifulSoup):
    for tag in soup.find_all():
        del tag['style']


def check_is_page_valid(raw_html: str) -> bool:
    for class_name in UNWANTED_CLASSES:
        if class_name in raw_html:
            return False
    return True


html = get_random_page_html()
print(process_html(html))
