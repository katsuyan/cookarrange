import json
import falcon
import scraping_recipe
import scraping_menu

class HelloResource(object):
    def on_get(self, req, res, recipe_id):
        msg = scraping_recipe.get_recipe(recipe_id)
        res.body = msg

class GetMenu(object):
    def on_get(self, req, res):
        msg = scraping_menu.get_menu('人参 玉ねぎ')
        res.body = msg

app = falcon.API()
app.add_route("/recipe/{recipe_id}", HelloResource())
app.add_route("/menu", GetMenu())

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
