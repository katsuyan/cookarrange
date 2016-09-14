import urllib.request
from bs4 import BeautifulSoup
import json
import re
import urllib.parse

def get_menu(target):
    data = []

    target_url = 'http://cookpad.com/search/' + urllib.parse.quote(target, safe='')
    html = urllib.request.urlopen(target_url).read()
    soup = BeautifulSoup(html, "lxml")

    main_layout = soup.find(class_='main_layout')
    recipe_texts = main_layout.find_all(class_="recipe-text")

    for recipe_text in recipe_texts:
        recipe_id = recipe_text.find(class_='recipe-title')['id']
        data.append(re.match(r'recipe_title_(\d*)', recipe_id).group(1))

    return json.dumps({'recipe_ids': data})
