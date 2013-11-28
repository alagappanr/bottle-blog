import bottle

@bottle.route("/")
def home_page():
    return "Hello World"

bottle.run(host="localhost", port=8888)
