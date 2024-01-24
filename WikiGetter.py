import json

import wikipediaapi
import random


CATEGORIES = [
    'sciences',
    'technologies',
    'medecine',
    'arts',
    'société',
    'sport',
    'politique',
    'histoire',
    'géographie'
]


def get_random_category():
    return CATEGORIES[random.randint(0, len(CATEGORIES) - 1)]


def get_random_page(seed: str = ""):
    if seed == "":
        seed = get_random_category()

    wiki_wiki = wikipediaapi.Wikipedia('WikiGuessrAPI (mafmaf14.official@gmail.com)', 'fr')
    search_results = wiki_wiki.page(seed)

    if not search_results.exists():
        print(f"La catégorie '{seed}' n'existe pas.")
        return

    random_page_title = random.choice(list(search_results.links.keys()))
    random_page = wiki_wiki.page(random_page_title)

    data = {
        'title': random_page.title,
        'paragraphs': [ random_page.summary ],
        'url': random_page.fullurl
    }
    return data