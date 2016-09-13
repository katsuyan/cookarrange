import json
import falcon
class HelloResource(object):
    def on_get(self, req, res):
        msg = {
            "message": "Welcome to the Falcon"
        }
        res.body = json.dumps(msg)
        
app = falcon.API()
app.add_route("/", HelloResource())

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
