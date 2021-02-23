from flask import Flask , render_template
app = Flask(__name__)

# @app.route('/')
# def Home():
#     return "<h1>Hello World! </h1>"

@app.route("/")
def home():
    return render_template("home.html")


@app.route('/John')
def John():
    return "<h1>Hello John! </h1>"

@app.route('/')
def hello():
    return 'Open a new tab and enter /Welcome/name for URL'

@app.route('/Welcome/<name>')
def Welcome_name(name):
    return 'Welcome ' + name + '!'  

    

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)