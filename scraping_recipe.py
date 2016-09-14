import urllib.request
from bs4 import BeautifulSoup
import json

def get_recipe(id):
    data = {}

    target_url = 'http://cookpad.com/recipe/' + id
    html = urllib.request.urlopen(target_url).read()
    soup = BeautifulSoup(html, "lxml")

    title = soup.select("#recipe-title > h1")[0].string.strip()
    data['title'] = title

    img_tag = soup.select("#recipe-main > #main-photo")[0]
    imgURL = img_tag.find('img')['src']
    data['imgURL'] = imgURL

    people = soup.select(".servings_for")[0].string.strip()
    data['people'] = people

    ingredients_html = soup.select("#ingredients_list")[0]
    ingredients_html = ingredients_html.find_all(class_='ingredient')

    ingredients = []
    ingredient = {'ingredient_category': 'none', 'ingredient_list': []}
    ingredient_one = {}
    for ingredient_html in ingredients_html:
        name_html = ingredient_html.find(class_='name')
        if name_html is None:
            ingredients.append(ingredient)
            ingredient_category = ingredient_html.find(class_='ingredient_category').get_text().strip().replace('■\n', '')
            ingredient = {'ingredient_category': ingredient_category, 'ingredient_list': []}
        else:
            name = name_html.string
            if name is None:
                name = ingredient_html.find('a').string
            quantity = ingredient_html.find(class_='ingredient_quantity').string
            ingredient_one['name'] = name
            ingredient_one['quantity'] = quantity
            ingredient['ingredient_list'].append(ingredient_one)
    ingredients.append(ingredient)
    data['ingredients'] = ingredients

    cook_steps = []
    steps = soup.select('#steps')[0]
    steps = steps.find_all(class_='step_text')
    for step in steps:
        cook_step = step.get_text().strip()
        cook_steps.append(cook_step)
    data['cook_steps'] = cook_steps

    advice = soup.select("#advice")[0]
    data['advice'] = advice.get_text().strip()

    return json.dumps(data)
