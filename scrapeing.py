import urllib.request
from bs4 import BeautifulSoup

target_url = 'http://cookpad.com/recipe/3400255'
html = urllib.request.urlopen(target_url).read()
soup = BeautifulSoup(html, "lxml")

title = soup.select("#recipe-title > h1")[0].string.strip()
print(title)

img_tag = soup.select("#recipe-main > #main-photo")[0]
imgURL = img_tag.find('img')['src']
print(imgURL)

people = soup.select(".servings_for")[0].string.strip()
print(people)

foods = soup.select("#ingredients_list")[0]
foods = foods.find_all(class_='ingredient')
for food in foods:
    name = food.find(class_='name').string
    print(name)
    quantity = food.find(class_='ingredient_quantity').string
    print(quantity)

steps = soup.select('#steps')[0]
steps = steps.find_all(class_='step_text')
for step in steps:
    print(step.get_text().strip())
print()

advice = soup.select("#advice")[0]
print(advice.get_text().strip())
