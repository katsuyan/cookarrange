import json
import falcon
import scraping_recipe

class HelloResource(object):
    def on_get(self, req, res):
        msg = scraping_recipe.get_recipe('2497431')
        res.body = msg

app = falcon.API()
app.add_route("/", HelloResource())

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
