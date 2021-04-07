from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def Home():
     return "<h1>มนัสชนก เพ็งมีศรี 6006021612069</h1>"


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
